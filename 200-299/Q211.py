from collections import deque
class TrieNode:
  def __init__(self, children, isEnd = False) -> None:
    self.children = children
    self.isEnd = isEnd

class WordDictionary:
  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.words = TrieNode({})

  def addWord(self, word: str) -> None:
    node = self.words
    for c in word:
      if c not in node.children:
        node.children[c] = TrieNode({})
      node = node.children[c]
    node.isEnd = True
    
  def search(self, word: str) -> bool:
    queue = deque([self.words])
    for c in word:
      length = len(queue)
      for _ in range(length):
        node = queue.popleft()
        if c == '.':
          for key in node.children.keys():
            queue.append(node.children[key])
        elif c in node.children:
          queue.append(node.children[c])
    
    for item in queue:
      if item.isEnd:
        return True
    return False

# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord('bad')
obj.addWord('dad')
obj.addWord('mad')
print(obj.search('.ad'))