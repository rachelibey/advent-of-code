
with open("input", "r") as file:
    content = file.read().split('\n')


roll_indexes = set([(i // len(content), i % len(content)) for i in range(len(content)*len(content)) if content[i // len(content)][i % len(content)] == "@"])
adjs = set([(0,1), (0,-1), (-1,-1), (-1,0), (-1,1), (1,-1), (1,0), (1,1)])

def count_neighbors(idx, roll_idxs):
    total = 0
    for adj in adjs:
        dx, dy = idx[0] + adj[0], idx[1] + adj[1]
        if (dx,dy) in roll_idxs:
            total += 1
    return total

def remove_rolls(roll_idxs):
    to_remove = set()
    for idx in roll_indexes:
        if count_neighbors(idx, roll_idxs) < 4:
            to_remove.add(idx)
    return to_remove

def day04(part2):
    if not part2:
        return len(remove_rolls(roll_indexes))
    roll_idxs = roll_indexes.copy()
    last_len = -1
    while last_len != len(roll_idxs):
        last_len = len(roll_idxs)
        to_remove = remove_rolls(roll_idxs)
        roll_idxs = roll_idxs.difference(to_remove)
    return len(roll_indexes) - len(roll_idxs)

part_one, part_two = day04(False), day04(True)
print("p1:", part_one)
print("p2:", part_two)


    
