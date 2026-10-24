class WordDictionary:
    class Node:
        def __init__(self):
            self.word = False
            self.children = {}

    def __init__(self):
        self.root = self.Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        # traverse till we get to the end of the word
        for i in range(len(word)):
            if word[i] not in curr.children:
                curr.children[word[i]] = self.Node()
            curr = curr.children[word[i]]
        curr.word = True

    def search(self, word: str) -> bool:
        def helper(node, i):
            if i == len(word):
                return node.word

            if word[i] == ".":
                return any(helper(other, i + 1) for _, other in node.children.items())
            
            if word[i] not in node.children:
                return False

            return helper(node.children[word[i]], i+1)
        
        return helper(self.root, 0)




        
