"""

628. Maximum Product of Three Numbers

Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.


"""

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if nums is None or len(nums)==0:
            return 0
        
        nums.sort()
        
        #
        # for the max product, it is either going to be
        #
        # 1) all the largest values on the right hand side
        #    multiplied together
        #
        # OR
        #
        # 2) two largest negative values on the left
        #    multiplied by the largerst value on the right
        #
        if len(nums) >= 3:
            return max ( nums[-1] * nums[-2] * nums[-3],
                         nums[0] * nums[1] * nums[-1] )
        
        #
        # less than 3 numbers, we have no options other than
        # to multiply these numbers and return the value
        #
        else:
            
            prod = nums[0]
            i=1
            while i < len(nums):
                
                prod*=nums[i]
                
                i+=1
            
            return prod
        
def main():
    
    solution = Solution()
    
    print ( "6 == " + str ( solution.maximumProduct([1,2,3]) ))
    
    print ( "24 == " + str ( solution.maximumProduct([1,2,3,4]) ))
    
    
    print ( "720 == " + str ( solution.maximumProduct([-4,-3,-2,-1,60]) ))
    
    
    
if __name__ == '__main__':
    main() 
    
    