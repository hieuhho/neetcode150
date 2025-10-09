# Word Search II

# Given a 2-D grid of characters board and a list of strings words, return all words that are present in the grid.

# For a word to be present it must be possible to form the word with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

# Example 1:

# Input:
# board = [
#   ["a","b","c","d"],
#   ["s","a","a","t"],
#   ["a","c","k","e"],
#   ["a","c","d","n"]
# ],
# words = ["bat","cat","back","backend","stack"]

# Output: ["cat","back","backend"]

# Example 2:

# Input:
# board = [
#   ["x","o"],
#   ["x","o"]
# ],
# words = ["xoxo"]

# Output: []

# Constraints:

#     1 <= board.length, board[i].length <= 12
#     board[i] consists only of lowercase English letter.
#     1 <= words.length <= 30,000
#     1 <= words[i].length <= 10
#     words[i] consists only of lowercase English letters.
#     All strings within words are distinct.

class TrieNode():
    def __init__(self):
        self.child = {}
        self.end = False

    def add_word(self, word):
        cur = self
        for c in word:
            if c not in cur.child:
                cur.child[c] = TrieNode()
            cur = cur.child[c]
        cur.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.add_word(word)

        ROWS, COLS = len(board), len(board[0])
        ans, visited = set(), set()

        def dfs(r, c, node, current_word):
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                (r, c) in visited or
                board[r][c] not in node.child):
                return
            visited.add((r, c))

            node = node.child[board[r][c]]
            current_word += board[r][c]

            if node.end:
                ans.add(current_word)

            dfs(r - 1, c, node, current_word)
            dfs(r + 1, c, node, current_word)
            dfs(r, c- 1, node, current_word)
            dfs(r, c + 1, node, current_word)

            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(ans)