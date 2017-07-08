"""



633. Sum of Square Numbers

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
        """
        :type c: int
        :rtype: bool
        """
        
        #
        # a^2 + b^2 = c
        #
        # it follows that: b^2 = c - a^2, and so b = sqrt(c-a^2)
        #
        for a in range(0,int(math.sqrt(c)) + 1 ):
            
            b = int(math.sqrt( c - a*a ))
            
            if a*a + b*b == c:
                return True

        return False



def main():
    
    solution = Solution()
    
    print( "True == " + str ( solution.judgeSquareSum(5) ))
#     
#     import pdb
#     pdb.set_trace()
    
    print( "False == " + str ( solution.judgeSquareSum(3) ))
    
#     import pdb
#     pdb.set_trace()
    
    print( "True == " + str ( solution.judgeSquareSum(2) ))
    
    print( "False == " + str ( solution.judgeSquareSum(6) ))

if __name__ == '__main__':
    main()
    
    
    
    