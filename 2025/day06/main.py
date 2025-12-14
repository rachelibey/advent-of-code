import pandas as pd

with open("input.txt", "r") as file:
    content = file.read().split('\n')

def day06(part_two):
    new_content = []
    for line in content:
        if part_two:
            line = list(line)
        else:
            line = line.split()
        new_content.append(line)

    new_content = pd.DataFrame(new_content).T.values.tolist()

    if part_two:
        total = 0
        i = 0
        op = ""
        sub_total = 0
        while i < len(new_content):
            num = ""
            if new_content[i][-1] in ('+', '*'):
                op = new_content[i][-1]
                sub_total = 1 if op == "*" else 0
                num = int("".join(new_content[i][:-1]))
            elif all(x == ' ' for x in new_content[i]):
                op = ""
                total += sub_total
            else:
                num = int("".join(new_content[i]))
            if op == "+":
                sub_total += num
            elif op == "*":
                sub_total *= num
            i += 1
        total += sub_total
        return total
    else:
        total = 0
        for lis in new_content:
            value = 0
            if lis[4] == '*':
                value = int(lis[0]) * int(lis[1]) * int(lis[2]) * int(lis[3])
            else:
                value = int(lis[0]) + int(lis[1]) + int(lis[2]) + int(lis[3])
            total += value
        return total



print("p1:", day06(False))
print("p1:", day06(True))