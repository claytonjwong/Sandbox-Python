"""

283. Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        len_nums = len ( nums )
        
        #
        # use i to iterate forward for each non-zero number
        # use j to iterate backwards for each 0 moved to the back
        #
        i=0
        j = len_nums - 1
        while i < j:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                j -= 1
            else:
                i += 1
    
def main():
    
    test_list = [0, 1, 0, 3, 12]
    
    solution = Solution()
    
    solution.moveZeroes( test_list )
    
    print ( "[1, 3, 12, 0, 0] == " + str (  test_list ) ) 


if __name__ == "__main__":
    main()








