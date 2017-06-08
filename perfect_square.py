"""

367. Valid Perfect Square

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False

"""


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        #
        # subtract odds numbers 1, 3, 5, 7, etc
        # and see if the number is 0, if so, it is a perfect square
        #
        #
        # formula any odd element in the series as: 2n-1
        #
        # example:
        #
        # n = 1, 2n-1 = 1
        # n = 2, 2n-1 = 3
        # n = 3, 2n-1 = 5
        #
        # the sum of the series is n(n+1)/2, plugging in the formula above,
        # the sum of the odd series is n([2n-1]+1)/2 = = 2n^2/2 = n^2
        #
        i = 1
        while num > 0:
            
            #
            # subtract current odd number
            #
            num -= i
            
            #
            # next odd number
            #
            i += 2
            
        return num == 0
            
            
            

def main():
    
    import pdb
    
    pdb.set_trace()
    
    solution = Solution()

    print ( "True == " + str ( solution.isPerfectSquare(16) ) )
    
if __name__ == "__main__":
    main()
    
    
    

