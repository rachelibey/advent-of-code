with open("input.txt", "r") as file:
    content = file.readlines()

def day01():
    dial_value = 50
    zeroes_p1 = 0
    zeroes_p2 = 0
    for turn in content:
        num = int(turn[1:])
        if "R" in turn:
            total = dial_value + num
            dial_value = total % 100
        else:
            total = ((100 - dial_value) % 100) + num
            dial_value = (100 - (total % 100)) % 100
        zeroes_p1 += dial_value == 0
        zeroes_p2 += total // 100
    return zeroes_p1, zeroes_p2

part1, part2 = day01()
print("p1:", part1)
print("p2:", part2)