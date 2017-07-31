"""

208. Implement Trie (Prefix Tree)

https://leetcode.com/problems/implement-trie-prefix-tree/description/

Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.

""" 

class TrieNode(object):
    def __init__(self,val):
        self.val = val
        self.links = [None] * 26
        self.isEnd = False

    def put(self, ch, trie):
        self.links[ord(ch)-ord('a')]=trie

    def get(self, ch):
        return self.links[ord(ch)-ord('a')]


class Trie(object):
    
    def __init__(self, val=""):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(val)
        


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for ch in word:
            if not curr.get(ch): # add if TrieNode(ch) does NOT exist
                curr.put(ch,TrieNode(ch))
            curr = curr.get(ch) # iterate along with current child for ch
        curr.isEnd = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.startsWithHelper(word) # returns last node of word if found, None otherwise
        if node and node.isEnd:
            return True
        else:
            return False 
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return True if self.startsWithHelper(prefix) else False
        
    def startsWithHelper(self, prefix):
        """
        Returns the last Node in the prefix (if found), otherwise None
        :type prefix: str
        :rtype: TrieNode ( or None )
        """
        curr = self.root
        for ch in prefix:
            curr = curr.get(ch)
            if not curr:
                return None
            
        return curr

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == '__main__':
    

    obj = Trie()
    obj.insert("le")
    obj.insert("leet")
    param_2 = obj.search("leet")
    param_3 = obj.startsWith("lee")
    
    import pdb
    pdb.set_trace()   
    
    
    
    
    
    
