"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321 

click to show spoilers.

Note:
 The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows
"""

import math
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        #
        # rev will be the reversed number returned
        #
        rev = 0
        
        #
        # calculate the max INT32 as 2^31 - 1
        #
        max = math.pow(2, 31) - 1
        
        #
        # get the absolute value of X, and remember if X was negative
        #
        negative = False
        
        if x < 0:
            negative = True
         
        x = abs ( x )
        
        #
        # mod X by 10 in order to get the right-most digit,
        # add that right-most digit to the reversed answer,
        # then divide X by 10 in order to shift right by one decimal position
        #
        while ( x != 0 ):
            
            #
            # shift the reversed answer left by one decimal position
            # only after the first iteration.  rev=0 initially,
            # so the first time this loop executes, there is no shift
            # there is also no shift if the digit to be reversed is 0
            # for example 1230 reversed is 0321 which is 321,
            # there is no need to left-shirt the leading 0
            #
            if ( rev > 0 ):
                rev *= 10
            
            #
            # add the right-most digit to the reversed answer,
            # this will be shifted left on the next iteration
            #
            rev += x % 10
            
            #
            # divide x by 10 in order to shift right by one decimal position
            #
            x = int ( x / 10 )


        #
        # python will automatically type cast a INT32 into a LONG,
        # so perform a bounds check for the range (2^31 - 1) to (-2^31)
        #
        if ( rev > max ) or ( negative and rev > max + 1 ):
                return 0
                
        #
        # if X was negative, then change the reversed value to negative as well
        #
        if ( negative ):
            rev *= -1
        
        
        return rev    
            



def main():
    
    x = 22987654321
    
    solution = Solution()
    
    print ( solution.reverse(x) )
    
if __name__ == "__main__":
    main()