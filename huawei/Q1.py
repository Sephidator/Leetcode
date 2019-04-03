import sys


def print_result(group_num, string):
    result = []
    for i in range(group_num):
        one_group = string[9*i:9*i+9]
        if one_group[0] is 1:
            result.append(one_group[1:])
        else:
            result.append(one_group[-1:0:-1])
    print(" ".join(result))


group_num = int(sys.stdin.readline().strip())
string = sys.stdin.readline().strip()
print_result(group_num, string)

