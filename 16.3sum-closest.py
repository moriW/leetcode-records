#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
# https://leetcode.cn/problems/3sum-closest/description/
#
# algorithms
# Medium (44.78%)
# Likes:    1626
# Dislikes: 0
# Total Accepted:    564.8K
# Total Submissions: 1.3M
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# 给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。
#
# 返回这三个数的和。
#
# 假定每组输入只存在恰好一个解。
#
#
#
# 示例 1：
#
#
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
#
#
# 示例 2：
#
#
# 输入：nums = [0,0,0], target = 1
# 输出：0
#
#
#
#
# 提示：
#
#
# 3 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# -10^4 <= target <= 10^4
#
#
#


from typing import List


# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        best_value = 1 << 20

        for i in range(len(nums) - 2):
            # cur = nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                res = nums[i] + nums[l] + nums[r]
                if abs(target - res) < abs(target - best_value):
                    best_value = res

                if res < target:
                    l += 1
                else:
                    r -= 1

        return best_value


# @lc code=end

print(
    Solution().threeSumClosest(
        [1,1,1,1],
        3,
    )
)
