"""

26. Remove Duplicates from Sorted Array 

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory. 

For example,
 Given input array nums = [1,1,2], 

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length. 


"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums_len = len ( nums )
        
        if ( nums_len == 0 or nums_len == 1 ):
            return nums_len
        
        #
        # iterate through the list of nums
        # from 0 till len - 2, since we always
        # want to comapre the current index
        # with the current index + 1
        #
        i = 0    
        while ( i < nums_len - 1 ):
            
            #
            # if there is a duplicate, then remove it
            #
            if ( nums[i] == nums[i+1] ):
                nums.pop(i)
                nums_len -= 1
            else:
                i += 1
            
        return nums_len
    
    
def main():
    
    solution = Solution()
    print ( "4 == " + str ( solution.removeDuplicates([ 0,1,1,2,2,2,3 ]) ) )
    
    
if __name__ == "__main__":
    main()
