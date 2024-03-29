"""

645. Set Mismatch

https://leetcode.com/contest/leetcode-weekly-contest-42/problems/set-mismatch/

The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.

"""


class Solution:
    
    
    def findErrorNums(self, nums):
        return [sum(nums) - sum(set(nums)), sum(range(1,len(nums)+1)) - sum(set(nums))]
    
    def findErrorNums2(self, nums):
        return [sum(nums) - sum(set(nums)), len(nums)*(len(nums)+1)//2 - sum(set(nums))]

    
    def findErrorNums3(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        duplicate = 0
        
        # add all into set to find the dup and later the sum of the actual series
        unique = set()
        
        unqiue_len = 0
        for num in nums:
            unique.add(num)
            unqiue_len += 1
            
            # only set duplicate once ( 0 is an invalid entry )
            # val was NOT added into the unique set, so this is the duplicate
            if duplicate == 0 and len(unique) != unqiue_len:
                duplicate = num

        # missing number is sum of series minus sum of actual
        # (without the duplicate counted twice)
        sum_of_actual = 0
        for val in unique:
            sum_of_actual += val
        
        # n(n+1)/2
        sum_of_series = len(nums) * ( len(nums) + 1 ) // 2
        
        missing_number = sum_of_series - sum_of_actual
        
        return [ duplicate, missing_number ]
    
        
if __name__ == '__main__':

    solution = Solution()
    
    nums = []
    
    n = 10000000
    for i in range(1,n+1):
        nums.append(i)
    nums[1] = 3 # change 2 to 3 ( 3 is a duplicate and 2 is missing )
        
    from timeit import default_timer as timer

    start = timer()
    solution.findErrorNums(nums)
    end = timer()
    print(end - start) 

    start = timer()
    solution.findErrorNums2(nums)
    end = timer()
    print(end - start) 
    
    
    
        
        