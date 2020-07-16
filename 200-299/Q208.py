class TrieNode:
    def __init__(self):
        self.R = 26
        self.next = [None for _ in range(self.R)]
        self.end = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        node = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not node.next[i]:
                node.next[i] = TrieNode()
            node = node.next[i]
        node.end = True

        # if word:
        #     i = ord(word[0]) - ord('a')
        #     if not self.next[i]:
        #         self.next[i] = Trie()
        #     self.next[i].insert(word[1:])
        # else:
        #     self.end = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not node.next[i]:
                return False
            node = node.next[i]
        return node.end


        # if word:
        #     i = ord(word[0]) - ord('a')
        #     if self.next[i]:
        #         return self.next[i].search(word[1:])
        #     return False
        
        # return self.end
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if not node.next[i]:
                return False
            node = node.next[i]
        return True

        # if prefix:
        #     i = ord(prefix[0]) - ord('a')
        #     if self.next[i]:
        #         return self.next[i].startsWith(prefix[1:])
        #     return False
        
        # return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

obj = Trie()
obj.insert("apple")
obj.insert("aples")
print(obj.search("apple"))
print(obj.search("app"))
print(obj.search("apples"))
print(obj.search("aple"))
print(obj.search("a"))

print(obj.startsWith("apple"))
print(obj.startsWith("app"))
print(obj.startsWith("apples"))
print(obj.startsWith("aple"))
print(obj.startsWith("a"))


