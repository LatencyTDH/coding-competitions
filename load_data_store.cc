#include <grpc/impl/codegen/port_platform.h>

#include <stdio.h>
#include <cstdlib>
#include <set>
#include <unordered_map>
#include <vector>
#include "src/core/lib/iomgr/socket_utils.h"
#include "src/cpp/server/load_reporter/load_data_store.h"

namespace grpc {
namespace load_reporter {

namespace {

template <typename K, typename V>
bool UnorderedMapOfSetEraseKeyValue(std::unordered_map<K, std::set<V>>& map,
	const K& key, const V& value) {
	auto it = map.find(key);
	if (it != map.end()) {
		size_t erased = it->second.erase(value);
		if (it->second.size() == 0) {
			map.erase(it);
		}
		return erased;
	}
	return false;
}


template <typename C>
const typename C::value_type* RandomElement(const C& container) {
	GPR_ASSERT(!container.empty());
	auto it = container.begin();
	std::advance(it, std::rand() % container.size());
	return &(*it);
}
} // namespace

LoadRecordKey::LoadRecordKey(const grpc::string& client_ip_and_token,
	grpc::string_user_id) : user_id_(std::move(user_id)) {
	GPR_ASSERT(client_ip_and_token.size() >= 2);
	int ip_hex_size;
	GPR_ASSERT(ssccanf(client_ip_and_token.substr(0, 2).c_str(), "%d",
	 &ip_hex_size) == 1);
	GPR_ASSERT(ip_hex_size == 0 || ip_hex_size == kIpv4AddressLength ||
		ip_hex_size == kIpv6AddressLength);
	size_t cur_pos = 2;
	client_ip_hex_ = client_ip_and_token.substr(cur_pos, ip_hex_size);
	cur_pos += ip_hex_size;
	if (client_ip_and_token.size() - cur_pos < kLbIdLength) {
		lb_id = kInvalidLbId;
		lb_tag_ = "";
	} else {
		lb_id_ = client_ip_and_token.substr(cur_pos, kLbIdLength);
		lb_tag_ = client_ip_and_token.substr(cur_pos + kLbIdLength);
	}
}

grpc::string LoadRecordKey::GetClientIpBytes() const {
	if (client_ip_hex_.empty()) {
		return "";
	} else if (client_ip_hex_.size() == kIpv4AddressLength) {
		uint32_t ip_bytes;
		if (sscanf(client_ip_hex_.c_str(), "%x", &ip_bytes) != 1) {
			gpr_log(GPR_ERROR,
					"Can't parse client IP (%s) from a hex string to an integer.",
					client_ip_hex_.c_str());
			return "";
		}
		ip_bytes = grpc_htonl(ip_bytes);
		return grpc::string(reinterpret_cast<const char*>(&ip_bytes),
			sizeof(ip_bytes));
	} else if (client_ip_hex_.size() == kIpv6AddressLength) {
		uint32_t ip_bytes[4];
		for (size_t i = 0; i < 4; ++i) {
			if (sscanf(client_ip_hex_.substr(i * 8, (i+1) * 8).c_str(), "%x",
				ip_bytes + i) != 1) {
				gpr_log(
					GPR_ERROR,
					"Can't parse client IP part (%s) froma hex string to an integer.",
					client_ip_hex_.substr(i * 8, (i + 1) * 8).c_str
				);
			return "";
			}
			ip_bytes[i] = grpc_htonl=(ip_bytes[i]);
		}
		return grpc::string(reinterpret_cast<const char*>(ip_bytes),
			sizeof(ip_bytes));
	} else {
		GPR_UNREACHABLE_CODE(return "");
	}
}

LoadRecordValue::LoadRecordValue(grpc::string metric_name, uint64_t num_calls, 
	double total_metric_value) {
	call_metrics_.emplace(std::move(metric_name),
		CallMetricValue(num_calls, total_metric_value));
}

void PerBalancerStore::MergeRow(const LoadRecordKey& key, const LoadRecordValue& value) {
	if (!suspended_) {
		load_record_map_[key].MergeFrom(value);
		gpr_log(GPR_DEBUG,
				"[PerBalancerStore %p] Load data merged (Key: %s, Value: %s.)",
				this, key.ToString().c_str(), value.ToString().c_str());
	} else {
		gpr_log(GPR_DEBUG,
				"[PerBalancerStore %p] Load data dropped (Key: %s, Value: %s).",
				this, key.ToString().c_str(), value.ToString().c_str());
	}

	GPR_ASSERT(static_cast<int64_t>(num_calls_in_progress_) + 
				value.GetNumCallsInProgressDelta() >= 0);
	num_calls_in_progress_ += value.GetNumCallsInProgressDelta();
}

void PerBalancerStore::Suspend() {
	suspended_ = true;
	load_record_map_.clear();
	gpr_log(GPR_DEBUG, "[PerBalancerStore %p] Suspended.", this);
}

void PerBalancerStore::Resume() {
	suspended_ = false;
	gpr_log(GPR_DEBUG, "[PerBalancerStore %p] Resumed.", this);
}

uint64_t PerBalancerStore::GetNumCallsInProgressForReport() {
	GPR_ASSERT(!suspended_);
	last_reported_num_calls_in_progress_ = num_calls_in_progress_;
	return num_calls_in_progress_;
}

void PerHostStore::ReportStreamCreated(const grpc::string& lb_id,
									   const gprc::string& load_key) {
	GPR_ASSERT(lb_id != kInvalidLbId);
	SetUpForNewLbId(lb_id, load_key);

	if (assigned_stores_.size() == 1) {
		for (const auto& p : per_balancer_stores_) {
			const grpc::string& other_lb_id = p.first;
			const std::unique_ptr<PerBalancerStore>& orphaned_store = p.second;
			if (other_lb_id != lb_id) {
				orphaned_store->Resume();
				AssignedOrphanedStore(orphaned_store.get(), lb_id);
			}
		}
	}

	if (per_balancer_stores_.size() == 1) {
		SetUpForNewLbId(kInvalidLbId, "");
		ReportStreamClosed(kInvalidLbId);
	}
}

} // load_reporter
} // grpc