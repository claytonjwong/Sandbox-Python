"""

647. Palindromic Substrings

https://leetcode.com/contest/leetcode-weekly-contest-42/problems/palindromic-substrings/

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.

"""


class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        
        if s is None or len(s)==0:
            return cnt
        
        i=0
        while i<len(s):
            
            cnt += 1 # this character itself is a palindrome always
            
            # try to find an even len palidrome
            #
            # 0 1 2 3   len=4
            # a b b a
            #   m m
            #   l r
            #
            left = i      # mid-left
            right = i+1   # mid-right
            
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    left-=1
                    right+=1
                    cnt+=1
                else:
                    break
            
            # try to find an odd len palindrome
            #
            # 0 1 2 3 4    len=5
            # a b c b a
            #   l i r
            #
            left = i-1
            right = i+1
                       
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    left-=1
                    right+=1
                    cnt+=1
                else:
                    break
                    
            i+=1
        
        return cnt
    
    def is_palindome(self,s):
        if len(s)==1:
            return True
        elif len(s)==2 and s[0] == s[-1]:
            return True
        else:
            return s[0] == s[-1] and self.is_palindome(s[1:len(s)-1])
            
    
if __name__ == '__main__':
    
    solution = Solution()
    
#     import pdb
#     pdb.set_trace()
    print ( "3 == " + str ( solution.countSubstrings("abc")))
    print ( "6 == " + str ( solution.countSubstrings("aaa")))
    

    solution.is_palindome("aba")
    
#     print ( "3 == " + str ( solution.countSubstrings("abc")))
    
    
    
    