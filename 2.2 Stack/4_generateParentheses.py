# # Generate Parentheses
# # Solved

# # You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

# # Example 1:

# # Input: n = 1

# # Output: ["()"]

# # Example 2:

# # Input: n = 3

# # Output: ["((()))","(()())","(())()","()(())","()()()"]

# # You may return the answer in any order.

# # Constraints:

# #     1 <= n <= 7

# Recommended Time & Space Complexity

# You should aim for a solution as good or better than O(4^n / sqrt(n)) time and O(n) space, where n is the number of parenthesis pairs in the string.

# Hint 1

# A brute force solution would be to generate all possible strings of size 2n and add only the valid strings. This would be an O(n * 2 ^ (2n)) solution. Can you think of a better way? Maybe you can use pruning to avoid generating invalid strings.

# Hint 2

# We can use backtracking with pruning. But what makes a string invalid? Can you think of a condition for this?

# Hint 3

# When the count of closing brackets exceeds the count of opening brackets, the string becomes invalid. Therefore, we can maintain two variables, open and close, to track the number of opening and closing brackets. We avoid exploring paths where close > open. Once the string length reaches 2n, we add it to the result.


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
