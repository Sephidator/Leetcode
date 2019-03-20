import sys

def roundTable(n, s, m):
    table = [i+1 for i in range(n)]
    index = s - 1
    num = 0
    result = []

    while table:
        num += 1

        if num == m:
            result.append(table[index])
            table.pop(index)
            num = 0
            n = n - 1
        elif n != 0:
            index = (index + 1) % n

    for code in result:
        print(code)


for line in sys.stdin:
    a = line.split()
    roundTable(int(a[0]), int(a[1]), int(a[2]))
