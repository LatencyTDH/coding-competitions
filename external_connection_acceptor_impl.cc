#include "src/cpp/sesrver/external_connection_acceptor_impl.h"

#include <memory>

#include <grpcpp/server_builder_impl.h>
#include <grpcpp/support/channel_arguments.h>

namespace grpc {
	namespace internal {
		namespace {
			class AcceptorWrapper : public experimental::ExternalConnectionAcceptor {
			public:
				explicit AcceptorWrapper(std::shared_ptr<ExternalConnectionAcceptorImpl> impl)
				: impl_(std::move(impl)) {}
				void HandleNewConnection(NewConnectionParameters* p) override {
					impl_->HandleNewConnection(p);
				}
			private :
			std::shared_ptr<ExternalConnectionAcceptorImpl> impl_;
			};
		} //namespace

	ExternalConnectionAcceptorImpl::ExternalConnectionAcceptorImpl(
		const grpc::string& name,
		ServerBuilder::experimental_type::ExternalConnectionType type,
		std::shared_ptr<ServerCredentials> creds)
		: name_(name), creds_(std::move(creds)) {
			GPR_ASSERT(type ==
				ServerBuilder::experimental_type::ExternalConnectionType::FROM_FD);
		}

	std::unique_ptr<experimental::ExternalConnectionAcceptor>
	ExternalConnectionAcceptorImpl::GetAcceptor() {
		std::lock_guard<std::mutex> lock(mu_);
		GPR_ASSERT(!has_acceptor_);
		has_acceptor_ = true;
		return std::unique_ptr<experimental::ExternalConnectionAcceptor>(
			new AcceptorWrapper(shared_from_this())
		);
	}

	void ExternalConnectionAcceptorImpl::HandleNewConnection(
		experimental::ExternalConnectionAcceptor::NewConnectionParameters* p) {
		std::lock_guard<std::mutex> lock(mu_);
		if (shutdown_ || !started_) {
			gpr_log(GPR_ERROR, 
					"Not handling external connection wth fd %d, started %d, shutdown %d",
					p->fd, started_, shutdown_
			);
			return;
		}
		if (handler_) {
			handler_->Handle(p->listener_fd, p->fd, p->read_buffer.c_buffer());
		}
	}

	void ExternalConnectionAcceptorImpl::Start() {
		std::lock_guard<std::mutex> lock(mu_);
		GPR_ASSERT(!started_);
		GPR_ASSERT(has_acceptor_);
		GPR_ASSERT(!shutdown_);
		started_ = true;
	}

	void ExternalConnectionAcceptorImpl::SetToChannelArgs(ChannelArguments* args) {
		args->SetPointer(name_.c_str(), &handler_);
	}

	} // namespace internal
} //nnamespace grpc