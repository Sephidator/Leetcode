import sys

line = sys.stdin.readline().strip()
nums = list(map(int, line.split()))
n = nums[0]
m = nums[1]

line = sys.stdin.readline().strip()
y_list = list(map(int, line.split()))

y_list.sort()
record = {}
for index in range(len(y_list)):
    try:
        record[y_list[index] - index - 1] += 1
    except KeyError:
        record[y_list[index] - index - 1] = 1

for i in range(m):
    k = int(sys.stdin.readline().strip())
    try:
        print(record[k])
    except KeyError:
        print(0)

