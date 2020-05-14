# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3329/

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.node = {c: None for c in list('abcdefghijklmnopqrstuvwxyz')}
        self.value = False
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if self.node[word[0]] is None:
            self.node[word[0]] = Trie()
        if len(word) == 1:
            self.node[word[0]].value = True
        else:
            self.node[word[0]].insert(word[1:])
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if len(word) == 1:
            return self.node[word[0]] and self.node[word[0]].value
        return self.node[word[0]] and self.node[word[0]].search(word[1:])
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if len(prefix) == 1:
            return self.node[prefix[0]] is not None
        return self.node[prefix[0]] and self.node[prefix[0]].startsWith(prefix[1:])
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)