"""

Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

"""

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        #
        # see how many mutliples of 5, 5x5, 5x5x5 there are
        # since trailing zeros are 2x5, 5 is the limiting factor
        #
        multiples_of_5x = 5
        
        while ( multiples_of_5x < n ):
            
            if ( n < 5 ):
                return i
            
            multiples_of_5x *= 5

        
    
def main():
    
    #
    # I looked through the first 5! values and found that 5 is the first instance with a trailing 0
    #
    # then 10! is the first instance with two trailing 0
    #
    # I anticiapted that 15! would be the first instance with three trailing 0, and that was correct
    #
    # so we simply need to find how many multiples of 5 will fit
    #
    solution = Solution()
    
    print ( "1 == " + str ( solution.trailingZeroes(5) ) )
    print ( "2 == " + str ( solution.trailingZeroes(10) ) )
    print ( "3 == " + str ( solution.trailingZeroes(15) ) )

if __name__ == "__main__":
    main()
    
    
    
    