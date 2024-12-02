from copy import deepcopy
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


def dampener(data: list) -> int:
    for i in range(len(data)):
        d = deepcopy(data)
        d.pop(i)
        if check_report(d):
            return 1
    return 0


count = 0
with open(base_path / "input.txt") as f:
    for line in f:
        data = list(map(int, line.split(" ")))
        count += max(check_report(data), dampener(data))

print(count)
