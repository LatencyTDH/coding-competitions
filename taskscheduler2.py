class Solution:
    def taskSchedulerII(self, tasks: list[int], space: int) -> int:
        last_exec_by_taskid = {}
        current_day = 1
        for task in tasks:
            current_day = max(
                current_day, last_exec_by_taskid.get(task, -space) + space + 1
            )
            last_exec_by_taskid[task] = current_day
            current_day += 1

        return current_day - 1
