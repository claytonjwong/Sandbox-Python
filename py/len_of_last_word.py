"""

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.

"""

class Solution(object):
    def lengthOfLastWord(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        i = -1
        last_word = ""
        
        #
        # iterate from -1 to -len (str) inclusive
        #
        while ( i >=  -1 * ( len ( str ) ) ):
            
            #
            # if whitespace is found, then check
            # if we have found a last word 
            #
            # if this is just trailing whitespace,
            # then last_word is an empty string with len 0
            #
            if ( str[i] == ' ' ):
                
                length = len ( last_word )
                
                if ( length > 0 ):
                    return length
                
            #
            # append the character in front of the string last_word
            #
            elif ( str[i] != ' '):
                last_word = str[i] + last_word
            
            i -= 1

            
            
        return len ( last_word )
    
    
def main():
    

    solution = Solution()
    
    import pdb
    pdb.set_trace()
    
    print ( solution.lengthOfLastWord("a") )
    
if __name__ == "__main__":
    main()
    
    