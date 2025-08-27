# Permutation in String

# You are given two strings s1 and s2.

# Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

# Both strings only contain lowercase letters.

# Example 1:

# Input: s1 = "abc", s2 = "lecabee"

# Output: true

# Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

# Example 2:

# Input: s1 = "abc", s2 = "lecaabee"

# Output: false

# Constraints:

#     1 <= s1.length, s2.length <= 1000

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_alphabet = [0] * 26
        s2_alphabet  = [0] * 26
        for letter in s1:
            s1_alphabet[ord(letter) - ord("a")] += 1
        l = 0
        s1_len = len(s1)

        for r in range(len(s2)):
            s2_alphabet[ord(s2[r]) - ord("a")] += 1
            if s1_len < (r - l + 1):
                s2_alphabet[ord(s2[l]) - ord("a")] -= 1
                l += 1

            if s1_len == (r - l + 1):
                if s2_alphabet == s1_alphabet:
                    return True
        return False