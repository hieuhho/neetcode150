# Word Break

# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of dictionary words.

# You are allowed to reuse words in the dictionary an unlimited number of times. You may assume all dictionary words are unique.

# Example 1:

# Input: s = "neetcode", wordDict = ["neet","code"]

# Output: true

# Explanation: Return true because "neetcode" can be split into "neet" and "code".

# Example 2:

# Input: s = "applepenapple", wordDict = ["apple","pen","ape"]

# Output: true

# Explanation: Return true because "applepenapple" can be split into "apple", "pen" and "apple". Notice that we can reuse words and also not use all the words.

# Example 3:

# Input: s = "catsincars", wordDict = ["cats","cat","sin","in","car"]

# Output: false

# Constraints:

#     1 <= s.length <= 200
#     1 <= wordDict.length <= 100
#     1 <= wordDict[i].length <= 20
#     s and wordDict[i] consist of only lowercase English letters.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] = True if substring s[i:] can be segmented into words from wordDict
        dp = [False] * (len(s) + 1)

        # base case: empty string at the end is always "breakable"
        dp[len(s)] = True

        # fill dp backwards: from the end of s to the start
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                # check if the word fits starting at position i
                if i + len(word) <= len(s) and s[i:i + len(word)] == word:
                    # If "word" is a valid chunk at s[i:],
                    # then the question becomes: can the rest, s[i+len(word):], also be segmented?
                    # That is exactly dp[i + len(word)].
                    dp[i] = dp[i + len(word)]
                # if we already found a valid break, no need to check further
                if dp[i]:
                    break

        # answer: can we segment the entire string s?
        return dp[0]