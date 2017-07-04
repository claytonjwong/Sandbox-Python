"""

3. Longest Substring Without Repeating Characters


Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""
from IPython.core.debugger import Pdb

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        max_len = 0
        
        curr_word = set()
        
        prev_letter = None
        
        for letter in s:
            
            try:
                
                #
                # see if this letter exists in the current word
                #
                if ( letter in curr_word ):
                    max_len = max ( max_len, len ( curr_word ) )
                    curr_word = set ( letter )
                    
                    #
                    # append the previous letter if it is NOT the same
                    #
                    if ( prev_letter and prev_letter not in curr_word ):
                        curr_word.add ( prev_letter )
                #
                # add letter onto current word
                #
                else:
                    curr_word.add ( letter )
                    
                #
                # keep track of the previous letter
                # in case it may be used for the next word
                #
                prev_letter = letter
                
            except:
                pass
            
        return max ( max_len, len ( curr_word ) )
    
def main():
    solution = Solution()
    
    import pdb
    pdb.set_trace()
    
    print ( "3 == " + str ( solution.lengthOfLongestSubstring("abcabcbb")))
    print ( "1 == " + str ( solution.lengthOfLongestSubstring("bbbbb")))
    print ( "3 == " + str ( solution.lengthOfLongestSubstring("pwwkew")))
    
if __name__ == "__main__":
    main()