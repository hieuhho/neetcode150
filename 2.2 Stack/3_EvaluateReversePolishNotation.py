# Evaluate Reverse Polish Notation
# Solved

# You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

# Return the integer that represents the evaluation of the expression.

#     The operands may be integers or the results of other operations.
#     The operators include '+', '-', '*', and '/'.
#     Assume that division between integers always truncates toward zero.

# Example 1:

# Input: tokens = ["1","2","+","3","*","4","-"]

# Output: 5

# Explanation: ((1 + 2) * 3) - 4 = 5

# Constraints:

#     1 <= tokens.length <= 1000.
#     tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-100, 100].
import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # make stack
        # for i in tokens
        # check i is alphanumeric
        # append to stack
        # else
        # check if stack has num
        # no -> return 0
        # yes -> stack_num operator i
        # add solution to stack
        ops = {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : lambda a, b: int(a / b) if a * b > 0 else -(-a // b)
        }
        ans = []
        for i in tokens:
            if i.isalnum():
                ans.append(int(i))
            else:
                if ans:
                    solved = ops[i](ans[-2], ans[-1])
                    ans.pop()
                    ans.pop()
                    ans.append(solved)
        return ans[0]

    # this fails with tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]