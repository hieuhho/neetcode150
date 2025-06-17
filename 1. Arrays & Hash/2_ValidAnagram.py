# Valid Anagram
# Solved

# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true

# Example 2:

# Input: s = "jar", t = "jam"

# Output: false

# Constraints:

#     s and t consist of lowercase English letters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_table = {}
        t_table = {}
        for i in s:
            s_table[i] = s_table.get(i, 0) + 1
        for i in t:
            t_table[i] = t_table.get(i, 0) + 1
        return s_table == t_table

