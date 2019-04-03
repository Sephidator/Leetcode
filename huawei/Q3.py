import sys


fruit_list = [[0] * 50 for i in range(40)]

N = int(sys.stdin.readline().strip())
for i in range(N):
    # 读取每一行
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    point = list(map(int, line.split()))
    fruit_list[point[0]][point[1]] = 1






