import time
import threading


class RateLimiter:
    def __init__(self, permits_per_sec: float):
        if permits_per_sec <= 0:
            raise ValueError("Rate must be positive!")

        self.last_refill_timestamp = time.monotonic()
        self.permits_per_sec = permits_per_sec
        self.max_capacity = max(1, permits_per_sec)
        self.tokens_available = self.max_capacity
        self.lock = threading.Lock()

    def acquire(self) -> None:
        return self.acquire(1)

    def acquire(self, permits: int) -> None:
        if permits < 0:
            raise ValueError("Can't request negative number of permits!")

        with self.lock:
            self._refill_tokens()
            wait_for_secs = self._consume(permits)
            if wait_for_secs > 0:
                print("Sleeping for ", wait_for_secs, "secs.")
                time.sleep(wait_for_secs)
                self._refill_tokens()
                wait = self._consume(permits)
                assert wait == 0
            else:
                print(f"Successfully acquired {permits} permits!")

    def try_acquire(self, permits: int, timeout_in_secs: int) -> bool:
        self._refill_tokens()
        wait_for_secs = self._consume(permits)
        return wait_for_secs <= timeout_in_secs

    def _refill_tokens(self):
        current_time_sec = time.monotonic()
        delta = current_time_sec - self.last_refill_timestamp
        new_tokens = self.permits_per_sec * delta
        if new_tokens > 0:
            self.last_refill_timestamp = current_time_sec
            self.tokens_available = min(
                self.tokens_available + new_tokens, self.max_capacity
            )

    def _consume(self, permits: int) -> float:
        new_tokens_available = self.tokens_available - permits
        if new_tokens_available >= 0:
            self.tokens_available = new_tokens_available
            return 0

        return -new_tokens_available / self.permits_per_sec


def simulate_acquisition(limiter: RateLimiter, prefix: str):
    global results
    total_permits_requested = 0

    start = time.monotonic()
    for i in range(100):
        permits = random.randint(1, 1)
        print(f"{prefix}: Attempting to get {permits} permits")
        # acquired = limiter.try_acquire(permits, 0)
        # total_permits_requested += permits if acquired else 0
        acquired = limiter.acquire(permits)
        total_permits_requested += permits

    end = time.monotonic()

    throughput = total_permits_requested / (end - start)
    stats = {
        "Throughput": throughput,
        "TotalPermits": total_permits_requested,
        "TimeElapsed": end - start,
    }
    results.append(stats)
    return stats


if __name__ == "__main__":
    import random

    limiter = RateLimiter(0.00000001)
    results = []
    t1 = threading.Thread(target=simulate_acquisition, args=(limiter, "t1"))
    t2 = threading.Thread(target=simulate_acquisition, args=(limiter, "t2"))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(results)
