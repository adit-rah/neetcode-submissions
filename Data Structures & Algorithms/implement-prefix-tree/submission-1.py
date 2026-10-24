class Node:
        def __init__(self):
            self.is_word = False 
            self.children = {}

class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        n = len(word)
        for i in range(n):
            if word[i] not in curr.children:
                curr.children[word[i]] = Node()
            curr = curr.children[word[i]]
        curr.is_word = True


    def search(self, word: str) -> bool:
        curr = self.root
        n = len(word)
        for i in range(n):
            if word[i] not in curr.children:
                return False
            curr = curr.children[word[i]]
        return curr.is_word
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        n = len(prefix)
        for i in range(n):
            if prefix[i] not in curr.children:
                return False
            curr = curr.children[prefix[i]]

        
        return True
        
        