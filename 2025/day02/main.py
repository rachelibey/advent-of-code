import math 

with open("input", "r") as file:
    content = file.read().split(",")

def day02():
    part_one_counter = 0
    part_two_counter = 0
    for id_range in content:
        start, stop = map(int, id_range.split("-"))
        for i in range(start, stop + 1):
            str_i = str(i)
            len_str_i = len(str_i)
            part_one, part_two = True, True
            for j in range(1, len_str_i//2 + 1):
                if len_str_i % j == 0:
                    divisors = len_str_i//j
                    if (str_i[:j] * divisors) == str_i:
                        if part_two:
                            part_two_counter += i
                            part_two = False
                        if divisors == 2 and part_one:
                            part_one_counter += i
                            part_one = False
    return part_one_counter, part_two_counter

part_one, part_two = day02()
print("p1:", part_one)
print("p2:", part_two)


    
