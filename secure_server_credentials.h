#ifndef GRPC_INTERNAL_CPP_SERVER_SECURE_SERVER_CREDENTIALS_H
#define GRPC_INTERNAL_CPP_SERVER_SECURE_SERVER_CREDENTIALS_H

#include <memory>
#include <grpcpp/security/server_credentials.h>
#include <grpc/grpc_security.h>
#include "src/cpp/server/thread_pool_interface.h"

namespace grpc_impl {
	class SecureServerCredentials;
}

namespace grpc {
	typedef ::grpc_impl::SecureServerCredentials SecureServerCredentials;

	class AuthMetadataProcessorAsyncWrapper final {
	public:
		static void Destroy(void* wrapper);
		static void Process(void* wrapper, grpc_auth_context* context,
			const grpc_metadata* md, size_t num_md, grpc_process_auth_metadata_done_cb cb,
			void *user_data);
		AuthMetadataProcessorAsyncWrapper(
			const std::shared_ptr<AuthMetadataProcessor>& processor)
			: thread_pool_(CreateDefaultThreadPool()), processor_(processor) {}

	private:
		void InvokeProcessor(grpc_auth_context* context, const grpc_metadata* md,
			size_t num_md, grpc_process_auth_metadata_done_cb cb, void* user_data);
		std::unique_ptr<ThreadPoolInterface> thread_pool_;
		std::shared_ptr<AuthMetadataProcessor> processor_;
	}
}
#endif