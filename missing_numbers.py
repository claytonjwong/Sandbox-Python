"""

448. Find All Numbers Disappeared in an Array

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]


"""



class Solution(object):
    
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        missing = []
        
        #
        # mark indexes corresponding to each number n as negative
        # for numbers found in the array, so missing numbers are 
        # the remaining indices which contain positive number values
        #
        for num in nums:
            
            #
            # nums are 1 to n inclusive, so subtract by 1 for 0-based indexing
            #
            index = abs(num) - 1
            
            nums[index] = -1 * abs ( nums[index] )
        

        #
        # find all remaining positive valued indexes
        #
        for i, num in enumerate(nums):
            
            if num > 0:
                
                #
                # nums are 1 to n inclusive, so add by 1 for 1-based indexing
                #
                missing.append(i + 1)
            
        
        return missing
    
    
def main():
    
    solution = Solution()
    print ( "[ 5, 6 ] == " + str ( solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]) ))
    
if __name__ == "__main__":
    main()











