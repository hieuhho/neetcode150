# Longest Palindromic Substring

# Given a string s, return the longest substring of s that is a palindrome.

# A palindrome is a string that reads the same forward and backward.

# If there are multiple palindromic substrings that have the same length, return any one of them.

# Example 1:

# Input: s = "ababd"

# Output: "bab"

# Explanation: Both "aba" and "bab" are valid answers.

# Example 2:

# Input: s = "abbc"

# Output: "bb"

# Constraints:

#     1 <= s.length <= 1000
#     s contains only digits and English letters.

class Solution:
        ans = ""
        ans_len = 0
        # check from middle
        for i in range(len(s)):
            # check odd palindrome
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > ans_len:
                    ans = s[l:r + 1]
                    ans_len = r - l + 1
                l -= 1
                r += 1

            # check even palindrome
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > ans_len:
                    ans = s[l:r + 1]
                    ans_len = r - l + 1
                l -= 1
                r += 1
        return ans