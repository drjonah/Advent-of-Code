with open("./input.txt") as f:
    raw_data = f.readlines()
    pids = [
        list(map(int, pid.split("-")) )
        for r in raw_data for pid in r.split(",")
    ]

pid_ranges = []
for pid_l, pid_u in pids:
    pid_range = range(pid_l, pid_u + 1)
    pid_ranges.extend(pid_range)


total = 0
for pid in pid_ranges:
    pid_str = str(pid)
    
    for i in range(2, len(pid_str) + 1):
        if len(pid_str) % i != 0:
            continue
        
        mid = len(pid_str) // i
        if pid_str[:mid] * i == pid_str:
            total += pid
            break
        
print(f"Day 2 Part 2: {total}") 