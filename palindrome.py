"""

Determine whether an integer is a palindrome. Do this without extra space.

"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        #
        # negative numbers are NOT palindromes
        #
        if ( x < 0 ):
            return False
        
        #
        # single digit numbers are palindromes
        #
        if ( x < 10 ):
            return True
                
        #
        # x > 10, calculate the start divisor
        # by multiplying by 10 in order to shift-left by 0
        #
        decimal_divisor = 1
        
        while ( x >= decimal_divisor ):
            decimal_divisor *= 10
            
        #
        # we overshot by 1, so backup
        #
        decimal_divisor /= 10
        
        while ( decimal_divisor >= 10 ):
            
            #
            # check to see if the left-most digit does NOT exist the right-most digit
            # if so, then return False
            #
            if ( int ( x / decimal_divisor ) != x % 10 ):
                return False
            
            #
            # iterate to the next decimal position by removing the first and last digits from X
            # and dividing the decimal divisor by 100
            #
            x = int ( ( x % decimal_divisor ) / 10 )
            decimal_divisor /= 100
            
        return True
        

def main():
    
    solution = Solution()
    
    print ( "1: " + str ( solution.isPalindrome(1) ) )
    print ( "10: " + str ( solution.isPalindrome(10) ) )
    print ( "11: " + str ( solution.isPalindrome(11) ) )
    print ( "121: " + str ( solution.isPalindrome(121) ) )
    print ( "12321: " + str ( solution.isPalindrome(12321) ) )
    print ( "-2147447412: " + str ( solution.isPalindrome(-2147447412) ) )

if __name__ == "__main__":
    main()