# Valid Parentheses
# Solved

# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:

#     Every open bracket is closed by the same type of close bracket.
#     Open brackets are closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

# Return true if s is a valid string, and false otherwise.

# Example 1:

# Input: s = "[]"

# Output: true

# Example 2:

# Input: s = "([{}])"

# Output: true

# Example 3:

# Input: s = "[(])"

# Output: false

# Explanation: The brackets are not closed in the correct order.

# Constraints:

#     1 <= s.length <= 1000
class Solution:
    def isValid(self, s: str) -> bool:
        # create a dict of parentheses pairs
        # create arr
        # loop through s
        # 1) if first i is closed, return false
        # 2) if bracket is close, check arr
        # 2.1) if top of arr is open & matching
        # 2.1.a) remove top of arr, continue
        # 2.2) if top of arr is open & NOT matching
        # 2.2.a) return false
        # 3) if bracket is open, add to arr
        # return if arr is empty or not
        stack = []
        bracket_dict = {
            ")": "(",
            "}": "{",
            "]": "["
        }
    
        for i in s:
            if i in bracket_dict:
                if stack[-1] == bracket_dict[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False


