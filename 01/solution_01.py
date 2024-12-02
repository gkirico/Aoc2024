from pathlib import Path

base_path = Path(__file__).parent

left = []
right = []

with open(base_path / "input.txt") as f:
    for line in f:
        data = line.split("   ")
        left.append(int(data[0].strip()))
        right.append(int(data[1].strip()))

sorted_left = sorted(left)
sorted_right = sorted(right)

result = 0

for li, ri in zip(sorted_left, sorted_right):
    result += abs(li - ri)

print(result)
