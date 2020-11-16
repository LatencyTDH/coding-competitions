"""
- Reservation
    - reserve(startTime, endTime) -> int: 
    - cancel(identifier): Handle situations where the resource is not already reserved
    
    R (1, 13) -> 0
    R (2, 13) -> 1
    R (3, 13) -> 2
    C (0)
    
    -> n = 2
    100 resources
    1 <= n <= big
    Single threaded
"""
from typing import List
from collections import defaultdict
    
class ReservationSystem(object):
    def __init__(self, total_resources: int):
        self.id_tracker = {}
        self.unique_id = 0
        self.n = total_resources
            
    def assign_requests(self, requests: List[Request]):
        for req in requests:
            if type(req) == ReserveRequest:
                self.id_tracker[self.unique_id] = (req.start, req.end)
                self.unique_id += 1
            else:
                to_delete_id = req.identifier
                if to_delete_id in self.id_tracker:
                    del self.id_tracker[to_delete_id]
                else:
                    raise ValueError("Invalid argument. Id does not exist as an existing request!")
    
    def is_assignment_valid(self):
        """Go through the id tracker of reservation requests and verify that we can actually make the assignment."""
        start_times = [start for start, _ in self.id_tracker.values()]
        end_times = [end for _, end in self.id_tracker.values()]
        
        start_times.sort()
        end_times.sort()
        
        start_ptr = 0
        end_ptr = 0
        
        total_times = len(start_times)
        resources_in_use = 0
        
        while start_ptr < total_times and end_ptr < total_times:
            if end_times[end_ptr] <= start_times[start_ptr]:
                resources_in_use -= 1
                end_ptr += 1
            else:
                resources_in_use += 1
                if resources_in_use > self.n:
                    return False
                start_ptr += 1
        
        return True
    
    def reserve(self, start_time: int, end_time: int) -> int:
        self.id_tracker[self.unique_id] = (start_time, end_time)
        if self.is_assignment_valid():
            allocated_id = self.unique_id
            self.unique_id += 1
            return allocated_id
        else:
            return -1

    def cancel(self, identifier: int) -> bool:
        if identifier in self.id_tracker:
            del self.id_tracker[identifier]
            return True
        else:
            return False
                  
"""
st = [1,2,3]
et = [13,13,13]
total_resources = 2
reserve -> R (1, 13) -> 0
reserve -> R (2, 13) -> 1
reserve -> R (3, 13) -> 2 -> fail
"""

if __name__ == "__main__":
    system = ReservationSystem(2)
    id1 = system.reserve(1, 13)
    id2 = system.reserve(13, 17)
    was_cancel_successful = system.cancel(5)
    print("Cancel status:", was_cancel_successful)
    print(id1, id2)
    