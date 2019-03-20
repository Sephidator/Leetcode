import sys


def look(student_list):
    result = [0] * len(student_list)

    for i in range(len(student_list) - 1, -1, -1):
        index = i + 1
        if index < len(student_list) and student_list[index] > student_list[i]:
            result[i] = index + 1
            continue
        while index < len(student_list):
            if student_list[result[index] - 1] > student_list[i]:
                result[i] = result[index]
                break
            else:
                index = result[index] - 1
                if index == -1:
                    break
    return result

n = int(sys.stdin.readline().strip())
student_list = []
for i in range(n):
    # 读取每一行
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    height = list(map(int, line.split()))[0]
    student_list.append(height)

for result in look(student_list):
    print(result)
