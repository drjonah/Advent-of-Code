
with open("input.txt") as file:
    f = file.readlines()
    cleaned = [ff.strip() for ff in f]


n = 12
total = 0

for bank in cleaned:
    
    remaining = len(bank) - n
    ptr = 0
    temp = ""
    
    while ptr < len(bank) - remaining:
        group = bank[ptr:ptr+remaining+1]
        biggest = max(group)
        
        temp += biggest
        
        skipped = group.index(biggest)
        ptr += group.index(biggest) + 1

        if remaining > 0:
            remaining -= skipped

    total += int(temp)   
        
print(f"part 2: {total}")