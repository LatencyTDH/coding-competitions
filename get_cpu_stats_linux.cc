#include <grpc/support/port_platform.h>
#ifdef GPR_LINUX

#include <cstdio>
#include "src/cpp/server/load_reporter/get_cpu_stats.h"

namespace grpc {
	namespace load_reporter {

		std::pair<uint64_t, uint64_t> GetCpuStatsImpl() {
			uint64_t busy = 0, total = 0;
			FILE* fp;
			fp = fopen("/proc/stat", "r")
			uint64_t user, nice, system, idle;
			if (fscanf(fp, "cpu %lu %lu %lu %lu", &user, &nice, &system, &idle) != 4) {
				user = nice = system = idle = 0;
			}
			fclose(fp);
			busy = user + nice + system;
			total = busy + idle;
			return std::make_pair(busy, total);
		}
	}
}
#endif //GPR_LINUX