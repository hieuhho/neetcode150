# Minimum Window Substring

# Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

# You may assume that the correct output is always unique.

# Example 1:

# Input: s = "OUZODYXAZV", t = "XYZ"

# Output: "YXAZ"

# Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

# Example 2:

# Input: s = "xyz", t = "xyz"

# Output: "xyz"

# Example 3:

# Input: s = "x", t = "xy"

# Output: ""

# Constraints:

#     1 <= s.length <= 1000
#     1 <= t.length <= 1000
#     s and t consist of uppercase and lowercase English letters.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        # init the count and size of res
        t_count, window_count = {}, {}
        res_window, res_len = [0, 0], float("infinity")

        # get the t count
        for letter in t:
            t_count[letter] = 1 + t_count.get(letter, 0)

        have, need = 0, len(t_count)
        l = 0
        for r in range(len(s)):
            letter = s[r]
            window_count[letter] = 1 + window_count.get(letter, 0)

            # compare t count and window count
            if letter in t_count and window_count[letter] == t_count[letter]:
                have += 1

            while have == need:
                # update the res if the window len is less than res_len
                if (r - l + 1) < res_len:
                    res_window = [l, r]
                    res_len = r - l + 1

                # continue resize window
                window_count[s[l]] -= 1
                if s[l] in t_count and window_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
        l, r = res_window
        return s[l: r + 1] if res_len != float("infinity") else ""