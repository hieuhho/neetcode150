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


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # init len(s1) count for s1 and s2:
        # s1="ab"
        # s2="lecabee"
        # s1Count [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # s2Count [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # init # of matches between s1 & s2
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            new_letter = ord(s2[r]) - ord('a')
            s2Count[new_letter] += 1
            # if s2 has same # of letter, increase matches
            if s1Count[new_letter] == s2Count[new_letter]:
                matches += 1
            # if s2 has more letter WITH new letter, decrease matches
            elif s1Count[new_letter] + 1 == s2Count[new_letter]:
                matches -= 1

            # shrink the window, as new letter enter, old letter exit
            old_letter = ord(s2[l]) - ord('a')
            # remove the old letter from count
            s2Count[old_letter] -= 1
            # since now the window has slided, increase the matches if equal
            if s1Count[old_letter] == s2Count[old_letter]:
                matches += 1
            # if s1 has more letter after sliding, decrease the matches
            elif s1Count[old_letter] - 1 == s2Count[old_letter]:
                matches -= 1
            l += 1
        return matches == 26