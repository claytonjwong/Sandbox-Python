"""

581. Shortest Unsorted Continuous Subarray

https://leetcode.com/problems/shortest-unsorted-continuous-subarray/#/description

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.

"""



class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #
        # sanity check
        #
        if nums is None:
            return 0
        
        #
        # snums = sorted nums
        #
        snums = sorted(nums)
        
        #
        # see if nums is already sorted
        #
        if snums == nums:
            return 0
        
        #
        # there must be at least two differences
        # between nums and snums
        #
        # track the min and max indexes of those differences by
        # setting max / min to invalid values out of range
        #
        # then check the differences between the sorted / unsorted
        # one index position at a time, update min/max
        #
        maxi, mini = -1, len(nums) + 1
        
        for i in range(len(nums)):
            
            if nums[i] != snums[i]:
                
                mini = min ( mini, i )
                maxi = max ( maxi, i )
            
        return maxi - mini + 1

    
def main():
    
    solution = Solution()
    
    print ("0 == " + str ( \
        solution.findUnsortedSubarray(None)))

    print ("0 == " + str ( \
        solution.findUnsortedSubarray([])))
    
    print ("5 == " + str ( \
        solution.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])))

    print ("0 == " + str ( \
        solution.findUnsortedSubarray([1,2,3,4])))
    
    print ("2 == " + str ( \
        solution.findUnsortedSubarray([1,3,2,4])))
    

    print ("4 == " + str ( \
        solution.findUnsortedSubarray([1,3,2,2,2])))
    

    print ("3 == " + str ( \
        solution.findUnsortedSubarray([2,3,3,2,4])))

    print ("4 == " + str ( \
        solution.findUnsortedSubarray([3,3,3,2,5])))
    
    import pdb
    pdb.set_trace()
    
    print ("3 == " + str ( \
        solution.findUnsortedSubarray([1,2,4,5,3])))
    
    
    
    
if __name__ == '__main__':
    main()
    
    
