"""

231. Power of Two

Given an integer, write a function to determine if it is a power of two.

"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #
        # each power of 2 has exactly one bit set,
        # so subtract 1 from n and bitwise-and with n
        # to ensure there is exactly one bit set
        #
        # example:
        #
        # 8 = 1000
        # 7 = 0111
        #
        return n & (n - 1) == 0 if n > 0 else False # return False when n is 0
    
    
def main():
    
    solution = Solution()
    
    print ( "True == " + str ( solution.isPowerOfTwo(8) ) ) 
    
    


if __name__ == "__main__":
    main()



