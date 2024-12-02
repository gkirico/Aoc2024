from pathlib import Path

base_path = Path(__file__).parent


def check_report(data: list) -> int:
    sign = -1
    if data[0] > data[1]:
        sign = 1

    for i in range(1, len(data)):
        res = (data[i - 1] - data[i]) * sign
        if 0 >= res or res > 3:
            return 0
    return 1


count = 0
with open(base_path / "input.txt") as f:
    for line in f:
        data = list(map(int, line.split(" ")))
        count += check_report(data)

print(count)
