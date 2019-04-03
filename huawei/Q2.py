# import sys
# from math import sqrt, floor
# from typing import List
#
#
# def min_dis(start, end, points):
#     def distance(p1, p2):
#         return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
#
#     if len(points) is 1:
#         return distance(start, points[0]) + distance(end, points[0])
#     else:
#         result = -1
#         for i in range(len(points)-1):
#             for j in range(i+1, len(points)):
#                 n1 = points[i]
#                 n2 = points[j]
#                 tmp = distance(start, n1) + distance(end, n2) + min_dis(n1, n2, points[:i] + points[i+1:j] + points[j+1:])
#                 if result < 0 or tmp < result:
#                     result = tmp
#         return result
#
#
# for i in range(4):
#     for j in range()
#
#
#
# line = sys.stdin.readline().strip()
# myinput = list(map(int, line.split()))
# Ax = myinput[0]
# Ay = myinput[1]
# Bx = myinput[2]
# By = myinput[3]
# Cx = myinput[4]
# Cy = myinput[5]
# Dx = myinput[6]
# Dy = myinput[7]
# Ex = myinput[8]
# Ey = myinput[9]
# print(int(floor(min_dis((0, 0), (0, 0), [(Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy), (Ex, Ey)]))))
#
#
# print(int(floor(min_dis((0, 0), (0, 0), [(200, 0), (200, 10), (200, 50), (200, 30), (200, 25)]))))
#
#
