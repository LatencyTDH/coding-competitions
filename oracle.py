def best_bus_sizes(friends):
    n = len(friends)
    cumulative = [0] * n
    for i, friend_size in enumerate(friends):
        cumulative[i] = cumulative[i-1] + friend_size
    
    valid_sizes = set(cumulative)
    possible_sizes = []
    total_people = cumulative[-1]
    
    for candidate in cumulative:
        running_partition_size = candidate
        while running_partition_size <= total_people:
            if running_partition_size not in valid_sizes:
                break
            if running_partition_size == total_people:
                possible_sizes.append(candidate)
                break
            running_partition_size += candidate
            
    return possible_sizes
    
# 
# Your previous Markdown content is preserved below:
# 
# def say_hello():
#     print('Hello, World')
# 
# for i in range(5):
#     say_hello()
# 
# """
# Description
# ===========
# There are `n` **groups of friends**, and each group is numbered from `1` to `n` . The `i`-th group contains `a_i` people.
# They live near a bus stop, and only a single bus operates on this route. An empty bus arrives at the bus stop and all the groups want to travel by the bus.
# 
# However, **group of friends** do not want to get separated. So they enter the bus only if the bus can carry the entire group.
# 
# Moreover, the groups do not want to change their relative positioning while travelling.
# In other words, group `3` cannot travel by bus, unless group `1` and group `2` have either:
# 1. already traveled by the bus in the previous trip;
# 2. they are also sitting inside the bus at present.
# 
# You are given that a bus of size `x` can carry `x` people simultaneously.
# 
# Find the size `x` of the bus so that:
# 1. the bus can transport all the groups;
# 2. every time when the bus starts from the bus station, there is no empty space in the bus (i.e. the total number of people present inside the bus is equal to `x`).
# 
# Input Format
# ============
# The first line contains an integer `n`(`1` <= `n` <= `10^5`). The second line contains `n` space-separated integers `a_1`, `a_2`, ..., `a_n` (`1` <= `a_i` <= `10^4`).
# 
# Output Format
# =============
# Print all possible sizes of the bus in an increasing order.
# 
# Sample Input
# ------------
# ```
# 8
# 1_ 2| 1_ 1 _1 |2_ 1| 3
# 
# 1 3 4 5 6 8 9 12
# 1 2 3 4 5 6 7 8
#1 1 2 2 2 2 2
#1 2 4 6 

# Sample Output
# -------------
# ```
# 3 4 6 12
# ```
# 
# Sample Explanation
# ------------------
# 
# In the above example:
# `a_1` = 1, 
# `a_2` = 2, 
# `a_3` = 1, 
# `a_4` = 1,
# `a_5` = 1,
# `a_6` = 2,
# `a_7` = 1,
# `a_8` = 3.
# 
# If `x` = 1 : In the first trip, `a_1` go by the bus. There will be no second trip because the bus cannot accommodate group `a_2`. Hence "x = 1" is not the required answer.
# 
# If `x` = 2 : No bus trip is possible. That's because `a_1` cannot go alone, as one seat will be left vacant in the bus. And, `a_1` & `a_2` cannot go together, because the bus cannot accommodate both groups simultaneously.
# 
# If `x` = 3 : In the first trip, `a_1` & `a_2` go by the bus. In the second trip, `a_3`, `a_4` & `a_5` go by the bus. In the third trip, `a_6` & `a_7` go by the bus. In the fourth trip, `a_8` go by the bus.
# 
# If x = 4 : In the first trip, `a_1`, `a_2` & `a_3` go by the bus. In the second trip, `a_4`, `a_5` & `a_6` go by the bus. In the third trip, `a_7` & `a_8` go by the bus.
# 
# Similarly you can figure out the output for `x` = 5, 6 & 7.
# """
