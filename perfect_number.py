"""

507. Perfect Number My SubmissionsBack To Contest

We define the Perfect Number is a positive integer that is equal
to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when
it is a perfect number and false when it is not.

Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)

"""

import math

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        #
        # bounds check 
        #
        if ( num <= 0 ):
            return False

        #
        # a perfect number is the sum of all divisors which
        # is itself evenly divible by 2, until 1
        # continue dividing the number by 2 and adding those values into the sum
        #
        sum = 0
        i = num
       
        while ( i > 1 ):
            
            i = math.ceil ( i / 2 )
            
            if ( num % i == 0 ):
                sum += i
            else:
                return False
           
        #
        # if the sum of the divisors is equal to the number,
        # then return True, since this is a perfect number,
        # otherwise return False
        #
        if ( sum == num ):
            return True
        else:
            return False
        

def main():
    solution = Solution()
    
    print ( "28: " + str ( solution.checkPerfectNumber(28) ) )

if __name__ == "__main__":
    main()