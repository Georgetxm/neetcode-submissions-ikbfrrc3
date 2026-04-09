class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminal = False     
    

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
                curr = curr.children[c]
            else:
                curr = curr.children[c]

        curr.terminal = True 


    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            else:
                curr = curr.children[c]

        if not curr.terminal:
            return False
        else:
            return True

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            else:
                curr = curr.children[c]

        return True
        