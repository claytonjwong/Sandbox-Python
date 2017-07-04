"""

326. Power of Three


Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?


"""



class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        while n > 1:
            
            if n % 3 == 0:
                n /= 3
            else:
                return False
            
        return n == 1
    
def main():
    
    solution = Solution()
    
    print ( "True == "  + str ( solution.isPowerOfThree(27) ) )
    

        

if __name__ == "__main__":
    main()



