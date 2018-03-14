n, q = map(int, raw_input().split())
intervals = [[0, n-1, 1]]

def find_intervals(a, b):
    for i in range(len(intervals)):
        begin, end, value = intervals[i]
        if begin <= a <= end:
            first_interval = i
        if begin <= b <= end:
            last_interval = i
            break
    return first_interval, last_interval

def update_intervals(begin, end):
    global intervals
    

for i in range(1, q+1):
    a, b = map(int, raw_input().split())
    print find_intervals(a, b)

"""
5 3
1 2
0 4
0 2
0, 4,1
1 1 1 1 1
0, 0, 1 + 1, 2, 2 + 3, 4, 1 
1 2 2 1 1
0, 0, 2 + 1, 2, 3 + 3, 4, 2 
2 3 3 2 2
0, 0, 5 + 1, 2, 6 + 3, 4, 2
5 6 6 2 2
"""
