"""

29. Divide Two Integers


Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.

"""


import math

#
# 2147483647
#
MAX_INT = int( math.pow(2,31) - 1 )

#
# 2147483648
#
MAX_NEG_INT = MAX_INT + 1


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        #
        # change dividend and divisor to positive numbers
        # keep track of the negativity, and multiple the
        # result by -1 if the result should be negative
        #
        is_neg = False
        
        if dividend < 0 and divisor > 0:
            is_neg = True
        elif dividend > 0 and divisor < 0:
            is_neg = True
        
        dividend = abs( dividend )
        divisor = abs( divisor )
        
        #
        # dividend checks
        #
        if dividend == 0 or dividend < divisor:
            return 0
        
        elif dividend == divisor:
            return 1 if not is_neg else -1 * dividend
        
        #
        # divisor checks
        #
        if divisor == 0:
            return MAX_INT
        
        elif divisor == 1:
            
            #
            # 2147483647
            #
            if dividend > MAX_INT and not is_neg:
                return MAX_INT
            
            #
            # 2147483648
            #
            elif dividend > MAX_NEG_INT and is_neg:
                return -1 * MAX_NEG_INT
            
            else:
                return dividend if not is_neg else -1 * dividend
        
        
        result=0
        while dividend > divisor:
            
            #
            # find the largest power of 2 "chunk" by left shifting
            # and count the amount of "current shifts"
            #
            curr_shift=0
            while dividend >= ( divisor << (curr_shift+1) ):
                curr_shift += 1
    
            #
            # subtract the largest power of 2 "chunk"
            # keep track of the shift count
            # by adding up the 2^(current shifts)
            #
            chunk = divisor << curr_shift
            dividend -= chunk
            
            #
            # sum the 2^curr_shift
            #
            result += int( math.pow(2, curr_shift) )
            
        #
        # multiple by -1 in order to make the result negative if needed
        #
        return result if not is_neg else -1 * result
    
    
def main():
    
    solution = Solution()
    
    print ( " MAX_INT == " + str ( solution.divide(10, 0) ))
    
    print ( "10 == " + str ( solution.divide(10, 1)))
    
    print ( "0 == " + str ( solution.divide(0, 10)))
    



    print ( "3 == " + str ( solution.divide(7, 2)))
    

    
    print ( "4 == " + str ( solution.divide(24, 5)))
    
    
    print ( "-1 == " + str ( solution.divide(1,-1)))
    
    
    print ( "2147483647 == " + str ( solution.divide(-2147483648,-1)))

    print ( "-2147483648 == " + str ( solution.divide(2147483648,-1)))   
   
    print ( "1073741823 == " + str ( solution.divide(2147483647,2)))

    print ( "-1073741824 == " + str ( solution.divide(-2147483648,2)))
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    