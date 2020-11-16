#include "src/cpp/server/dynamic_thread_pool.h"

#include <mutex>
#include <grpc/support/log.h>
#include <grpcpp/impl/codegen/sync.h>
#include "src/core/lib/gprpp/thd.h"

namespace grpc {
	DynamicThreadPool::DynamicThread::DynamicThread(DynamicThreadPool* pool)
	: pool_(pool),
	thd_("grpcpp_dynamic_pool",
		[](void* th) {
			static_cast<DynamicThreadPool::DynamicThread*>(th)->ThreadFunc();
		},
		this) {
		thd_.Start();
	}

	DynamicThreadPool::DynamicThread::~DynamicThread() { thd_.Join(); }

	void DynamicThreadPool::DynamicThread::ThreadFunc() {
		pool_->ThreadFunc();
		grpc_core::MutexLock lock(&pool_->mu_);
		pool_->nthreads_--;
		pool_->dead_threads_.push_back(this);
		if ((pool_->shutdown_) && (pool_->nthreads_ == 0)) {
			pool_->shutdown_cv_.Signal();
		}
	}

	void DynamicThreadPool::ThreadFunc {
		for (;;) {
			grpc_core::ReleasableMutexLock lock(&mu_);
			if (!shutdown_ && callbacks_.empty()) {
				if (threads_waiting_ >= reserve_threads_) {
					break;
				}
			}
			threads_waiting_++;
			cv_.Wait(&mu_);
			threads_waiting_--;
		}

		if(!callbacks_.empty()) {
			auto cb = callbacks_.front();
			callbacks_.pop();
			lock.Unlock();
			cb();
		} else if (shutdown_) {
			break;
		}
	}

	DynamicThreadPool::DynamicThreadPool(int reserve_threads)
		: shutdown_(false),
		reserve_threads_(reserve_threads),
		nthreads_(0),
		threads_waiting_(0) {
			for (int i = 0; i < reserve_threads_; i++) {
				grpc_core::MutexLock lock(&mu_);
				nthreads_++;
				new DynamicThread(this);
			}
		}

	void DynamicThreadPool::ReapThreads(std::list<DynamicThread*>* tlist) {
		for (auto t = tlist->begin(); t != tlist->end(); t = tlist->erase(t)) {
			delete *t;
		}
	}

	DynamicThreadPool::~DynamicThreadPool() {
		grpc_core::MutexLock lock(&mu_);
		shutdown_ = true;
		cv_.Broadcast();
		while (nthreads_ != 0) {
			shutdown_cv_.Wait(&mu_);
		}
		ReapThreads(&dead_threads_);
	}

	void DynamicThreadPool::Add(const std::function<void()>& callback) {
		grpc_core::MutexLock lock(&mu_);
		callbacks_.push(callback);
		if (threads_waiting_ == 0) {
			nthreads_++;
			new DynamicThread(this);		
		} else {
			cv_.Signal();
		}

		if (!dead_threads_.empty()) {
			ReapThreads(&dead_threads_);
		}
	}
} //namespace grpc
