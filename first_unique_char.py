"""

387. First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.


"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        #
        # intially set the index to an invalid index range ( len(s) )
        #
        len_s = len (s)
        index = len_s
        
        #
        # iterate from a to z inclusive, and see if the char count is 1
        #
        for i in range( ord('a'), ord('z')+1 ):
            
            ch = chr(i)
            
            #
            # the char is unique, update the index for this unique char
            # if it occurs before any previous index
            #
            if s.count(ch) == 1:
                
                index = min ( index, s.index(ch) )
        
        #
        # return the index if it has been updated, if not, then there is no unique char, return -1
        #
        return index if index < len_s else -1
    
    
def main():
    

    
    solution = Solution()
    print ( "2 == " + str ( solution.firstUniqChar("loveleetcode") ) )
    
if __name__ == "__main__":
    main()
        
        
        

