# https://leetcode-cn.com/explore/interview/card/bytedance/243/array-and-sorting/1036/
# 班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。
#
# 给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。
#
# 示例 1:
#
# 输入:
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# 输出: 2
# 说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
# 第2个学生自己在一个朋友圈。所以返回2。
# 示例 2:
#
# 输入:
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# 输出: 1
# 说明：已知学生0和学生1互为朋友，学生1和学生2互为朋友，所以学生0和学生2也是朋友，所以他们三个在一个朋友圈，返回1。
# 注意：
#
# N 在[1,200]的范围内。
# 对于所有学生，有M[i][i] = 1。
# 如果有M[i][j] = 1，则有M[j][i] = 1。


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        unvisited = list(range(len(M)))
        count = 0
        # 遍历未访问过的所有数字
        # 对于每一个数字to_visit，把所有和它有朋友关系的数字都设为已经访问
        # 这样就得到一个circle
        while unvisited:
            visit = [unvisited.pop()]  # 在未访问的数字中随便选一个，然后在下面访问所有和它有朋友关系的
            while visit:
                not_visited = []  # 保存还没有访问过的数字，因为for遍历中修改unvisited会很麻烦，所以使用备份，
                i = visit.pop()   # i = visit.pop()是同样道理，避免在for遍历中做修改
                for j in unvisited:
                    if M[i][j] == 1:
                        visit.append(j)
                    else:
                        not_visited.append(j)
                unvisited = not_visited
            count += 1
        return count

        # n = len(M)
        # if n == 1:
        #     return 1
        #
        # circle_list = []
        #
        # for i in range(0, n - 1):
        #     for j in range(i + 1, n):
        #         no_i = -1
        #         no_j = -1
        #         for index, circle in enumerate(circle_list):
        #             if i in circle:
        #                 no_i = index
        #             if j in circle:
        #                 no_j = index
        #             if no_i != -1 and no_j != -1:
        #                 break
        #
        #         if M[i][j] == 1:
        #             if no_i == -1 and no_j == -1:
        #                 circle_list.append({i, j})
        #             elif no_i == no_j:
        #                 continue
        #             elif no_i == -1:
        #                 circle_list[no_j].add(i)
        #             elif no_j == -1:
        #                 circle_list[no_i].add(j)
        #             else:
        #                 circle_list[no_i] = circle_list[no_i].union(circle_list[no_j])
        #                 circle_list.pop(no_j)
        #         else:
        #             if no_i == -1:
        #                 circle_list.append({i})
        #             if no_j == -1:
        #                 circle_list.append({j})
        # return len(circle_list)


s = Solution()
print(s.findCircleNum([[1,1,0], [1,1,0], [0,0,1]]))