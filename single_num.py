"""

Given an array of integers, every element appears twice except for one.
Find that single one.

Note:
 Your algorithm should have a linear runtime complexity.
 Could you implement it without using extra memory? 


"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        single = 0
        
        #
        # XOR all nums then each pair should "cancel" eachother out
        #
        # ( x ^ x = 0 ) 
        #
        for num in nums:
            single ^= num
    
        return single
    
def main():
    
    solution = Solution()
    
    print ( "2 == " + str ( solution.singleNumber([0,0,1,1,2]) ) )