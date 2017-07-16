"""

643. Maximum Average Subarray I My SubmissionsBack to Contest

https://leetcode.com/contest/leetcode-weekly-contest-41/problems/maximum-average-subarray-i/

Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].

"""


class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        if len(nums) <= k:
            return sum(nums) / k

        i = 0
        csum = sum(nums[i:i+k]) # current sum
        mavg = csum / k         # max average = current sum / k
        
        while True:
            
            # iterate
            i += 1
            if (i > len(nums) - k):
                break
            
            # drop last, add next instead of inoking sum() here
            csum = csum - nums[i-1] + nums[i+k-1]  
                
            # update max average
            mavg = max ( mavg, csum / k )

        return mavg
    
if __name__ == '__main__':
    
    solution = Solution()
    
    
    print (str(solution.findMaxAverage([3,3,4,3,0], 3)))
    
