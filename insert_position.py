"""

35. Search Insert Position 
 

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 ==> 2
[1,3,5,6], 2 ==> 1
[1,3,5,6], 7 ==> 4
[1,3,5,6], 0 ==> 0 


"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        #
        # iterate through the sorted array and return when the number
        # is greater than or equal to the target
        #
        i = 0
        for num in nums:
            if num >= target:
                return i

            i += 1
                
        #
        # above loop iterates from 0 to n-1
        # if no position was found, then this target
        # is the largest value in the array,
        # and would belong at  the end of the array
        #
        return len(nums)
    
    
def main():
    
    solution = Solution()
    
    print ( "2 == " + str ( solution.searchInsert([1,3,5,6], 5) ))
    print ( "1 == " + str ( solution.searchInsert([1,3,5,6], 2) ))
    print ( "4 == " + str ( solution.searchInsert([1,3,5,6], 7) ))
    print ( "0 == " + str ( solution.searchInsert([1,3,5,6], 0) ))
    
    
if __name__ == "__main__":
    main()
    
    