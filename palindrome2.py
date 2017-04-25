"""

Given a string, determine if it is a palindrome, considering only
alphanumeric characters and ignoring cases. 

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome. 

"""

class Solution(object):

    ascii_a = ord('a')
    ascii_z = ord('z')
    
    ascii_A = ord('A')
    ascii_Z = ord('Z') 
    
    ascii_0 = ord('0')
    ascii_9 = ord('9')
    
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #
        # begin/end chars to compare
        #
        begin_char = None
        end_char = None
        
        #
        # lower case
        #
        s = s.lower()
        
        #
        # iterate through the string from front(i) and back(j)
        #
        i = 0
        j = len(s) - 1
        while ( i < j ):
            
            #
            # find the first alpha numeric character
            #
            begin_char = s[i]
            while ( not self.isCharAlphaNumeric ( begin_char ) \
                    and i < j ):
                i += 1
                begin_char = s[i]
            
            #
            # find the second alpha numeric character
            #
            end_char = s[j]
            while ( not self.isCharAlphaNumeric ( end_char ) \
                    and j > i ):
                j -= 1
                end_char = s[j]
            
            #
            # if the alpha numeric chars are NOT the same,
            # then return False
            #
            if ( begin_char != end_char ):
                return False
            
            #
            # iterate from front/back
            #
            i += 1
            j -= 1
            
        
        #
        # the string is a palindrome
        #    
        return True
             
            
                
    def isCharAlphaNumeric(self, character):
        """
        assume that character is lower case or a digit
        """
        
        c = ord(character)
        
        return ( c >= Solution.ascii_a and c <= Solution.ascii_z ) \
            or ( c >= Solution.ascii_0 and c <= Solution.ascii_9 )
        
        
def main():
    
    solution = Solution()
    
    import pdb
    pdb.set_trace()
    
    print ( "True == " + str ( solution.isPalindrome("ab") ) )
    

if __name__ == "__main__":
    main()
    
    
