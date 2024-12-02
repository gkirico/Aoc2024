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

similarity = 0
i = 0
for num in sorted_left:
    count = 0
    while num >= sorted_right[i]:
        if num == sorted_right[i]:
            count += 1
        i += 1
    similarity += count * num

print(similarity)
