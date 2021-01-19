class Trie:

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.trie = {}
    

  def insert(self, word: str) -> None:
    """
    Inserts a word into the trie.
    """
    node = self.trie
    for c in word:
      if c in node:
        node = node[c]
      else:
        node[c] = {}
        node = node[c]
    node['#'] = True 
      

  def search(self, word: str) -> bool:
    """
    Returns if the word is in the trie.
    """
    node = self.trie
    for c in word:
      if c in node:
        node = node[c]
      else:
        return False
    return '#' in node
    

  def startsWith(self, prefix: str) -> bool:
    """
    Returns if there is any word in the trie that starts with the given prefix.
    """
    node = self.trie
    for c in prefix:
      if c in node:
        node = node[c]
      else:
        return False
    return True
    


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

trie = Trie();

print(trie.insert("apple"))
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
print(trie.insert("app"))
print(trie.search("app"))