"""

263. Ugly Number

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.


"""


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        #
        # zero is NOT an ugly number
        #
        if num == 0:
            return False
        
        #
        # while the number is evenly divisible by 2, 3, and 5, divide it by 2, 3, and 5
        #
        for v in [2,3,5]:
            while num % v == 0:
                num /= v
            
        #
        # ugly numbers are evenly divisible by 2, 3, and 5,
        # when we can no longer evenly divide
        # by these numbers, then we should be left with 1
        #
        return num == 1
        
        
def main():
    
    solution = Solution()
    
    print ( "False == " + str ( solution.isUgly(14) ) )
    

if __name__ == "__main__":
    main()
    
    
    