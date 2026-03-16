
with open("input.txt") as file:
    f = file.readlines()
    cleaned = [ff.strip() for ff in f]
    
    
total = 0

for bank in cleaned:
    
    largest = 0
    for i in range(len(bank) - 1):
        battery_1 = bank[i]
        battery_2 = max(bank[i+1:])
        joltage = int(str(battery_1) + str(battery_2))
        
        if joltage > largest:
            largest = joltage
            
    total += largest
    
print(f"part 1: {total}")