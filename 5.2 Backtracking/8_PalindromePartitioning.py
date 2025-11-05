# Palindrome Partitioning
# Given a string s, split s into substrings where every substring is a palindrome. Return all possible lists of palindromic substrings.

# You may return the solution in any order.

# Example 1:

# Input: s = "aab"

# Output: [["a","a","b"],["aa","b"]]
# Example 2:

# Input: s = "a"

# Output: [["a"]]
# Constraints:

# 1 <= s.length <= 20
# s contains only lowercase English letters.

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        current = []

        def backtrack(i):
            if i >= len(s):
                res.append(current.copy())
                return

            for j in range(i, len(s)):
                if self.valid_palindrome(s, i, j):
                    current.append(s[i:j+1])
                    backtrack(j + 1)
                    current.pop()
        backtrack(0)
        return res


    def valid_palindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True