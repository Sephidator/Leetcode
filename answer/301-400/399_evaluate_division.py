"""
https://leetcode-cn.com/problems/evaluate-division/description/

给出方程式 A / B = k, 其中 A 和 B 均为代表字符串的变量， k 是一个浮点型数字。
根据已知方程式求解问题，并返回计算结果。如果结果不存在，则返回 -1.0。

示例 :
给定 a / b = 2.0, b / c = 3.0
问题: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
返回 [6.0, 0.5, -1.0, 1.0, -1.0 ]

输入为:
vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries
(方程式，方程式结果，问题方程式)，
其中 equations.size() == values.size()，即方程式的长度与方程式结果长度相等（程式与结果一一对应），并且结果值均为正数。
以上为方程式的描述。 返回vector<double>类型。

基于上述例子，输入如下：
equations(方程式) = [ ["a", "b"], ["b", "c"] ],
values(方程式结果) = [2.0, 3.0],
queries(问题方程式) = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].

输入总是有效的。你可以假设除法运算中不会出现除数为0的情况，且不存在任何矛盾的结果。
"""


class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        def bfs(dic, x, y, visited):
            if x not in dic or y not in dic:
                return -1.0
            elif x in visited:
                return -1.0
            elif y in dic[x]:
                return dic[x, y]
            else:
                for p in dic[x]:
                    visited.append(x)
                    temp = bfs(dic, p, y, visited)
                    visited.pop()
                    if temp != -1.0:
                        return dic[x, p] * temp
                return -1.0

        dic = {}
        res = []

        for i in range(len(equations)):
            first = equations[i][0]
            second = equations[i][1]
        
            if first not in dic:
                dic[first] = []
            if second not in dic:
                dic[second] = []
            dic[first].append(second)
            dic[second].append(first)
            dic[first, second] = values[i]
            dic[second, first] = 1 / values[i]

        for x, y in queries:
            res.append(bfs(dic, x, y, []))

        return res


    def calcEquation1(equations, values, queries):
        from collections import defaultdict
        def dfs(d, x, y, visited):
            if x in visited:
                return -1.0
            for p in d[x].items():
                visited.append(x)
                if p[0] == y:
                    return p[1]
                else:
                    temp = dfs(d, p[0], y, visited)
                    if temp and temp != -1:
                        return p[1] * temp
                visited.pop()
            return -1.0

        d = defaultdict(dict)
        res = []

        for x in range(len(equations)):
            d[equations[x][0]][equations[x][1]] = values[x]
            d[equations[x][1]][equations[x][0]] = 1 / values[x]
        for x, y in queries:
            if x not in d or y not in d:
                res.append(-1.0)
            elif x == y:
                res.append(1.0)
            else:
                visited = []
                res.append(dfs(d, x, y, visited))
        return res



s = Solution();
ad = s.calcEquation([["a","b"],["e","f"],["b","e"]],
               [3.4,1.4,2.3],
               [["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"], ["x", "x"]])

print(ad)