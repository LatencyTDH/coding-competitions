from math import inf
# Enter your code here. Read input from STDIN. Print output to STDOUT

# 1. ["20:01", "11:34", "23:57", "14:29"] -> 175
# 2. ["10:22", "09:10", "00:10", "23:50"] -> 20

TOTAL_MINUTES = 1440
    
def closest_times(timestamps):
    return counting_sort(convert_timestamps(timestamps))

def convert_timestamps(ts):
    out = []
    for timestamp in ts:
        hour, minute = map(int, timestamp.split(':'))
        out.append(hour * 60 + minute)
    return out
    
def counting_sort(ints):
    output = [0] * TOTAL_MINUTES
    min_diff = inf
    prev = None
    smallest = inf
    for num in ints:
        output[num] += 1
    for num, freq in enumerate(output):
        if freq > 0:
            if prev is None:
                prev = num
                smallest = num
            elif num - prev <= min_diff:
                min_diff = num - prev
            
            if freq > 1 and 0 <= min_diff:
                min_diff = 0
            prev = num
    return min(min_diff, (smallest - prev) % TOTAL_MINUTES)

if __name__ == "__main__":
    ts = ["20:01", "11:34", "23:57", "14:29"]
    ts2 =  ["10:22", "09:10", "00:10", "23:50"]
    ts3 = ["20:01", "11:34", "23:57", "14:29", "11:34"]
    ts4 = ["20:01", "20:00"]
    ts5 = ["00:10", "23:59", "00:20", "00:00", "00:40"]

    assert closest_times(ts) == 175
    assert closest_times(ts2) == 20
    assert closest_times(ts3) == 0 # 0, two timestamps same
    assert closest_times(ts4) == 1
    assert closest_times(ts5) == 1
