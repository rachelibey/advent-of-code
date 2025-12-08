
with open("input", "r") as file:
    content = file.read().split('\n')
    ranges = set()
    line_index = 0
    for line in content:
        if line == '':
            break
        ranges.add(tuple(map(int, line.split("-"))))
        line_index += 1

    

def day05_1():
    counter = 0
    for i in range(line_index + 1, len(content)):
        for (low, hi) in ranges:
            if (low <= int(content[i]) <= hi):
                counter += 1
                break
    return counter

def day05_2():
    discrete_ranges = ranges.copy()
    while True:
        new_discrete_ranges = set()
        my_ranges = list(discrete_ranges)
        while len(my_ranges) > 0:
            ran = my_ranges.pop(0)
            j = 0
            while j < len(my_ranges):
                if my_ranges[j][0] <= ran[0] and my_ranges[j][1] >= ran[1]:
                    ran = my_ranges[j]
                elif my_ranges[j][0] > ran[0] and my_ranges[j][1] < ran[1]:
                    my_ranges.pop(j)
                    continue
                elif my_ranges[j][0] <= ran[0] and my_ranges[j][1] >= ran[0]:
                    ran = (my_ranges[j][0], ran[1])
                    my_ranges.pop(j)
                    continue
                elif my_ranges[j][1] >= ran[1] and my_ranges[j][0] <= ran[1]:
                    ran = (ran[0], my_ranges[j][1])
                    my_ranges.pop(j)
                    continue
                j += 1
            new_discrete_ranges.add(ran)
        if len(new_discrete_ranges) == len(discrete_ranges):
            total = 0
            for ran in discrete_ranges:
                total += ran[1] - ran[0] + 1
            return total
        discrete_ranges = new_discrete_ranges
        

                
part_one, part_two = day05_1(), day05_2()
print("p1:", part_one)
print("p2:", part_two)


    
