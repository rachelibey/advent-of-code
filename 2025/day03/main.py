
with open("input", "r") as file:
    content = file.read().split('\n')
    
def day03(batteries):
    total_jolts = 0
    for line in content:
        # Make sorted tuple
        order = [(int(line[i]), i) for i in range(len(line))]
        order.sort(key=lambda x: x[0], reverse=True)
        jolt = ""
        last_idx = -1
        i = 0
        while len(jolt) < batteries:
            if order[i][1] > last_idx and (len(line) - order[i][1]) >= (batteries - len(jolt)):
                jolt += str(order[i][0])
                last_idx = order[i][1]
                i = 0
            else:
                i += 1
        total_jolts += int(jolt)
    return total_jolts

                
part_one, part_two = day03(2), day03(12)
print("p1:", part_one)
print("p2:", part_two)


    
