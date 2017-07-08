"""

633. Sum of Square Numbers

https://leetcode.com/problems/sum-of-square-numbers/#/description

Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:
Input: 3
Output: False

"""


import math

class Solution(object):
    def judgeSquareSum(self, c):
        
        #
        # a^2 + b^2 = c
        #
        for a in range(int(math.sqrt(c))+1):
            
            aa = a*a
                    
            bb = int ( math.sqrt(c - aa) ) * int ( math.sqrt(c - aa) )
                
            if aa + bb == c:
                return True
            
        return False
    
    
def main():
    
    solution = Solution()
     
    import pdb
    pdb.set_trace()
     
    print("True == " + str ( solution.judgeSquareSum(5) ))
    
    print("False == " + str ( solution.judgeSquareSum(3) ))
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    