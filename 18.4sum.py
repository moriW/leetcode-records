#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
# https://leetcode.cn/problems/4sum/description/
#
# algorithms
# Medium (36.61%)
# Likes:    1921
# Dislikes: 0
# Total Accepted:    593.6K
# Total Submissions: 1.6M
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a],
# nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：
#
#
# 0 <= a, b, c, d < n
# a、b、c 和 d 互不相同
# nums[a] + nums[b] + nums[c] + nums[d] == target
#
#
# 你可以按 任意顺序 返回答案 。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,0,-1,0,-2,2], target = 0
# 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#
#
# 示例 2：
#
#
# 输入：nums = [2,2,2,2,2], target = 8
# 输出：[[2,2,2,2]]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 200
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
#
#
#

from typing import List


# @lc code=start
class Solution:
    # def tryFindNextNumber(self, nums: List[int], target: int):
    #     rest = target - nums[0]
    #     self.tryFindNextNumber(nums[1:], rest)
        # finded_num = nums[0]
        # if nums[1:]
        # nums

    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        if len(nums) < 2:
            return result

        i, j = 0, len(nums)
        while i < j:


    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        ...

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        for i in nums:
            target - i
            # nums[i]
            # result.append(nums[i])


# @lc code=end
