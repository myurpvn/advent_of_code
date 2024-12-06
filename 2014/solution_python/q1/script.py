from collections import defaultdict

lines = []

with open("input.txt", "r") as f:
    lines: list[str] = f.readlines()

size = len(lines)

lhs_list: list[int] = []
rhs_list: list[int] = []
count_map = defaultdict(int)
diff: list[int] = []

for line in lines:
    lhs_str, rhs_str = line.split()

    count_map[int(rhs_str)] += 1

    lhs_list.append(int(lhs_str))
    rhs_list.append(int(rhs_str))

lhs_list.sort()
rhs_list.sort()

score: list[int] = []

for id in range(size):
    lhs = lhs_list[id]
    rhs = rhs_list[id]

    diff.insert(id, abs(lhs - rhs))
    score.insert(id, lhs * count_map.get(lhs, 0))

print(f"diff: {sum(diff)}")
print(f"score: {sum(score)}")
