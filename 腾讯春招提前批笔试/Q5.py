import sys

line = sys.stdin.readline().strip()
nums = list(map(int, line.split()))
n = nums[0]
v = nums[1]

sister_list = []
max_distance = 0

for i in range(n):
    line = sys.stdin.readline().strip()
    nums = list(map(int, line.split()))
    sister_list.append([nums[0], nums[1]])


def count_distance(i, v):
    if i < 0 or i >= n:
        return 0

    dis = sister_list[i][1] - sister_list[i][0]
    if i == n - 1:
        dis += min(v, 1000000000 - sister_list[i][1])
    else:
        speed_down_dis = sister_list[i+1][0] - sister_list[i][1]
        if speed_down_dis >= v:
            dis += v
        else:
            dis = dis + speed_down_dis + count_distance(i + 1, v - speed_down_dis)
    return dis


if n == 0:
    print(v)
else:
    for i in range(n):
        dis = count_distance(i, v)
        max_distance = max(max_distance, dis)
    print(max_distance)


