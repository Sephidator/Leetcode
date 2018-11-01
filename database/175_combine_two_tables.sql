-- https://leetcode-cn.com/problems/combine-two-tables/description/
--
-- 175. 组合两个表
-- 题目描述提示帮助提交记录社区讨论阅读解答
-- 表1: Person
--
-- +-------------+---------+
-- | 列名         | 类型     |
-- +-------------+---------+
-- | PersonId    | int     |
-- | FirstName   | varchar |
-- | LastName    | varchar |
-- +-------------+---------+
-- PersonId 是上表主键
-- 表2: Address
--
-- +-------------+---------+
-- | 列名         | 类型    |
-- +-------------+---------+
-- | AddressId   | int     |
-- | PersonId    | int     |
-- | City        | varchar |
-- | State       | varchar |
-- +-------------+---------+
-- AddressId 是上表主键
--
--
-- 编写一个 SQL 查询，满足条件：无论 person 是否有地址信息，都需要基于上述两表提供 person 的以下信息：
--
-- FirstName, LastName, City, State
--
--
-- 解答思路：left join

# Write your MySQL query statement below

SELECT p.FirstName, p.LastName, a.City, a.State
FROM Person p LEFT JOIN Address a on p.PersonId = a.PersonId;