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
    if len(pid_str) % 2 == 0 and pid_str[:len(pid_str) // 2] == pid_str[len(pid_str) // 2:]:
        total += pid
        
print(f"Day 2 Part 1: {total}")