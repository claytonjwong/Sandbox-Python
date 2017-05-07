"""

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.
For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        zero_sum_list = []
        
        #
        # iterate through nums, after sorting, and try to add up the sum
        # of the current number, and two other numbers ( left and right )
        # left and right indexes are moved inward towards eachother in this sorted list
        # in order to attempt to add up the three number sum to 0
        #
        nums.sort()
        
        i=0
        nums_len = len ( nums )
        while ( i < nums_len ):

            curr_index = i
            left_index = i+1
            right_index = nums_len-1
            
            #
            # move forward so that the next current will be a different value,
            # this is required in order to ensure that duplicate numbers are NOT included in the solution
            #
            while ( i < nums_len -1 and nums[i] == nums[i+1] ):
                i += 1
            
            #
            # check for 2 numbers to the right side of the current number and iterate inwards towards eachother
            #
            while ( left_index < right_index ):
            
                sum = nums[curr_index] + nums[left_index] + nums[right_index]
            
                if ( sum == 0 ):
                    zero_sum_list.append( \
                        [ nums[curr_index], nums[left_index], nums[right_index] ] )
                    
                    while ( left_index < right_index
                        and nums[left_index] == nums[left_index+1] ):
                        #
                        # iterate inwards as long as the left-most number is the same.
                        # this is required in order to ensure that duplicate numbers
                        # are NOT included in the solution
                        #
                        left_index += 1
                        
                    while ( left_index < right_index
                        and nums[right_index] == nums[right_index-1]):
                        #
                        # iterate inwards as long as the right-most number is the same.
                        # this is required in order to ensure that duplicate numbers
                        # are NOT included in the solution
                        #
                        right_index -= 1

                    #
                    # increment indexes towards eachother by 1
                    #
                    left_index += 1
                    right_index -= 1
                
                #
                # the sum of the sorted numbers is less than 0, then move the left-index right,
                # since nums is ordered, the number to the right is >= the current left-index value
                #
                elif ( sum < 0 ):
                    left_index += 1
                #
                # the sum of the sorted numbers is greater than 0, move the right-index left,
                # since nums i ordered, the number to the left is <= the current right-index value
                #
                elif ( sum > 0 ):
                    right_index -= 1

            #
            # iterate i by 1 for checking the next current number
            #
            i += 1
        
        return zero_sum_list
    
def main():
    solution = Solution()
 
    import pdb
    pdb.set_trace()
    
    nums1 = [0,0,0]
    answer1 = solution.threeSum(nums1)
    
    nums2 = [-1, -1, 0, 1, 2, 4]
    answer2 = solution.threeSum(nums2)
    
    nums3 = [-4, -1, -1, 0, 1, 2]
    answer3 = solution.threeSum(nums3)

    nums4 = [-2, 0, 1, 1, 2]
    answer4 = solution.threeSum(nums4)
    
if __name__ == "__main__":
    main()