"""

326. Power of Three


Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?


"""

import math

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return self.isPowerOfX(n, 3)
    
    def isPowerOfX(self, n, x):
        
        if n <= 0:
            return False
        
        #
        # find the max base power of X
        #
        base = x
    
        max_int = math.pow(2,31)
    
        i=2
        while True:
            
            if math.pow(base, i) > max_int:
                break
            
            i += 1
            
        max_base = math.pow(base, i-1)
        
        #
        # n is a power of X if the max base of that power is evenly divisible by n
        #
        return max_base % n == 0
    
def main():
    
    solution = Solution()
    
    print ( "True == "  + str ( solution.isPowerOfThree(27) ) )
    

        

if __name__ == "__main__":
    main()



