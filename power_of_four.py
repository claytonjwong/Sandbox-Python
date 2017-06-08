"""

342. Power of Four

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?

"""




class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        #
        # continue dividing by 4 as long as the number is evenly divisible by 4
        #
        while num > 1:
            
            if num % 4 == 0:
                num /= 4
            else:
                return False
                
        return num == 1
    
def main():
    pass


if __name__ == "__main__":
    main()
    
    
    
    
    
        