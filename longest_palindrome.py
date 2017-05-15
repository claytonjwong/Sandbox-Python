"""

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example: 
Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.



Example: 
Input: "cbbd"

Output: "bb"


"""


class Solution(object):
    def longestPalindrome(self, string_to_check):
        """
        :type s: str
        :rtype: str
        """
        
        if ( string_to_check is None ):
            return None
        
        if ( string_to_check == "" ):
            return ""
        
        longest_string = string_to_check[0]
        
        #
        # iterate through the indices of string,
        # and expand outwards while the substring is still
        # a palindrome
        #
        

        i=0
        len_string_to_check = len ( string_to_check )
        
        while ( i < len_string_to_check ):
            
            #
            # odd case: "aba", "aabaa"
            #
            try:
                expand_by_value = 1
                
                while ( \
                        i - expand_by_value >= 0
                    and i + expand_by_value < len_string_to_check
                    and string_to_check [ i - expand_by_value ]
                     == string_to_check [ i + expand_by_value] ):
                
                    curr_len = ( 2 * expand_by_value ) + 1 
                
                    if ( curr_len > len ( longest_string ) ):
                        longest_string = \
                            string_to_check[ (i - expand_by_value):
                                             (i + expand_by_value + 1) ]
                
                    expand_by_value += 1
                    
            except:
                pass
            
            #
            # even case: "aa", "abba", "aabbaa"
            #
            try:
                j=i+1
                expand_by_value = 0
                
                
                while ( i - expand_by_value >= 0
                    and j < len_string_to_check
                    and string_to_check [ i - expand_by_value ]
                     == string_to_check [ j + expand_by_value ] ):
                    
                    curr_len = ( 2 * expand_by_value ) + 2
                    
                    if ( curr_len > len ( longest_string ) ):
                        longest_string = string_to_check[ (i - expand_by_value):
                                                          (j + expand_by_value + 1 ) ]

                    expand_by_value += 1
                    
            except:
                pass

            i += 1
        
        
        return longest_string
    
def main():
    
    solution = Solution()
    

    
    print ( "bab == " + str ( solution.longestPalindrome("babad") ) )
    print ( "bb == " + str ( solution.longestPalindrome("cbb") ) )
    print ( "bb == " + str ( solution.longestPalindrome("bbc") ) )
    print ( "bb == " + str ( solution.longestPalindrome("cbbc") ) )
    print ( "bb == " + str ( solution.longestPalindrome("bb") ) )
#     import pdb
#     pdb.set_trace()
    
    print ( "aba == " + str ( solution.longestPalindrome("aba") ) )
    print ( "tattarrattat == " + str ( solution.longestPalindrome("tattarrattat") ) )
    
    
    
if __name__ == "__main__":
    main()