#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode.cn/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (38.29%)
# Likes:    7185
# Dislikes: 0
# Total Accepted:    1.7M
# Total Submissions: 4.4M
# Testcase Example:  '"babad"'
#
# 给你一个字符串 s，找到 s 中最长的回文子串。
#
# 如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。
#
#
#
# 示例 1：
#
#
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
#
#
# 示例 2：
#
#
# 输入：s = "cbbd"
# 输出："bb"
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 1000
# s 仅由数字和英文字母组成
#
#
#
#
from pprint import pprint


# @lc code=start
class Solution:

    # def isPalindrome(self, sub_s: str) -> bool:
    #
    #     l, r = 0, len(sub_s)
    #
    #     if r == 1:
    #         return True
    #
    #     if r == 2:
    #         return sub_s[0] == sub_s[1]
    #
    #     return (sub_s[l] == sub_s[r]) and self.isPalindrome(sub_s[1 : r - 1])

    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        dp = [[None for _ in range(s_len)] for _ in range(s_len)]

        max_len, last_max_str = 0, ""
        for i in range(s_len):
            max_len = 1
            last_max_str = s[i]
            dp[i][i] = True

        for r in range(1, s_len):
            for l in range(r - 1, -1, -1):
                last_dp_l = min(l + 1, r - 1)
                last_dp_r = max(r - 1, 0)
                if dp[last_dp_l][last_dp_r] and s[l] == s[r]:
                    dp[l][r] = True
                    if (r + 1 - l) >= max_len:
                        max_len = r + 1 - l
                        last_max_str = s[l : r + 1]

                else:
                    dp[l][r] = False
        return last_max_str


# @lc code=end


print(Solution().longestPalindrome("abbd"))
