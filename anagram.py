"""

242. Valid Anagram

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.


"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        #
        # invalid anagram if the length of the two strings are NOT equal
        #
        len_str = len ( s )
        
        if len_str != len (t):
            return False
        
        #
        # start with a hash from a-z
        # increment count for each instance of each letter found in s
        # decrement count for each instance of each letter found in t
        #
        q = {}
        for i in range ( ord('a'), ord('z') + 1 ):
            q [ i ] = 0
        
        for ch in s:
            q [ ord(ch) ] += 1
    
        for ch in t:
            try:
                q [ ord(ch) ] -= 1
            except KeyError:
                return False
    
        for i in range ( ord('a'), ord('z') + 1 ):
            if q [ i ] != 0:
                return False
    
        return True
    
    
    
def main():
    
    solution = Solution()
    
    print ( "True == " + str ( solution.isAnagram("iceman", "cinema") ) )


if __name__ == "__main__":
    main()










