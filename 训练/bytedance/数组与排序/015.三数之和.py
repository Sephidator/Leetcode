# https://leetcode-cn.com/explore/interview/card/bytedance/243/array-and-sorting/1020/
#
# 三数之和
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        triplets = []

        # The key is to sort the list upfront.
        # The cost for that is O(n logn), which we recoup as it allows us to
        # search the sorted list in O(n^2) time
        nums.sort()

        # Use 3 pointers (indices): left, middle, right
        # middle starts at left+1
        # right starts at n-1

        for left in range(n - 2):
            middle = left + 1
            right = n - 1

            # shortcuts
            if nums[left] > 0:
                break

            # skip possible duplicates on the left
            if left > 0 and nums[left - 1] == nums[left]:
                continue

            # as long as there's room
            # we'll be moving right and middle depending on the current sum:
            # right index will move left (down)
            # middle index will move right (up)
            while middle < right:

                current_sum = nums[left] + nums[middle] + nums[right]

                # shortcuts
                if nums[right] < 0:
                    break

                # we're too low
                elif current_sum < 0:

                    # increment middle index only
                    middle += 1

                # we're too high
                elif current_sum > 0:

                    # decrement right index only
                    right -= 1

                # we're at 0
                else:
                    # add current values to solution
                    triplets.append([nums[left], nums[middle], nums[right]])

                    # skip possible duplicates on the right index
                    while middle < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # skip possible duplicates on the middle index
                    while middle < right and nums[middle] == nums[middle + 1]:
                        middle += 1

                    # now move both right and middle index towards each other
                    right -= 1
                    middle += 1

        return triplets


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))

