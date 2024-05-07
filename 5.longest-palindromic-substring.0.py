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


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not len(s) or len(s) == 1:
            return s
        l, r = 0, 1
        max_len_sub_str = ""
        current_sub_str = ""
        while l < r and r < len(s):
            current_sub_str = s[l:r]
            if current_sub_str == reversed(current_sub_str):
                max_len_sub_str = (
                    current_sub_str
                    if len(current_sub_str) > len(max_len_sub_str)
                    else max_len_sub_str
                )
                r += 1
            else:
                l += 1

        return current_sub_str


# @lc code=end
#


print(Solution().longestPalindrome("babad"))
