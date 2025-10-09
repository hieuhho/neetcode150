# Design Add and Search Word Data Structure

# Design a data structure that supports adding new words and searching for existing words.

# Implement the WordDictionary class:

#     void addWord(word) Adds word to the data structure.
#     bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

# Example 1:

# Input:
# ["WordDictionary", "addWord", "day", "addWord", "bay", "addWord", "may", "search", "say", "search", "day", "search", ".ay", "search", "b.."]

# Output:
# [null, null, null, null, false, true, true, true]

# Explanation:
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("day");
# wordDictionary.addWord("bay");
# wordDictionary.addWord("may");
# wordDictionary.search("say"); // return false
# wordDictionary.search("day"); // return true
# wordDictionary.search(".ay"); // return true
# wordDictionary.search("b.."); // return true

# Constraints:

#     1 <= word.length <= 20
#     word in addWord consists of lowercase English letters.
#     word in search consist of '.' or lowercase English letters.
#     There will be at most 2 dots in word for search queries.
#     At most 10,000 calls will be made to addWord and search.

class TrieNode:

    def __init__(self):
        self.child = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        tmp = self.root
        for c in word:
            if c not in tmp.child:
                tmp.child[c] = TrieNode()
            tmp = tmp.child[c]
        tmp.end = True


    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.child.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.child:
                        return False
                    cur = cur.child[c]
            return cur.end
        return dfs(0, self.root)