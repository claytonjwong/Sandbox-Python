"""

459. Repeated Substring Pattern



Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"

Output: True

Explanation: It's the substring "ab" twice.
Example 2:
Input: "aba"

Output: False
Example 3:
Input: "abcabcabcabc"

Output: True

Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)


"""


class Solution(object):
    
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None or s == "":
            return False
        
        
        #
        # check for repeated substrings of length 1 to len(s)/2 inclusive
        #
        ss_len = 1
        
        while ss_len <= len(s) // 2:
            
            ss = s[:ss_len]
            
            #
            # shift i and j over by the substring length to check for each
            # substring equality, if there is NOT a repeated substring, then
            # exit this inner loop, and check for the next largest substring
            #
            i = ss_len
            j = i + ss_len
            while j <= len(s):
                
                if ss == s[i:j]:
                    i += ss_len
                    j = i + ss_len
                    
                else:
                    break
            
            #
            # i / j have iterated through the entire string,
            # so a repeated substring has been found
            #
            if i == len(s):
                return True
            
            #
            # check for next largest substring
            #
            ss_len += 1
    
        #
        # no repeated substring was found
        #
        return False
    
    
    
def main():
    
    import pdb
    pdb.set_trace()
    
    solution = Solution()
    print ( "True == " + str ( solution.repeatedSubstringPattern("abcabc") ))
    
if __name__ == "__main__":
    main()











