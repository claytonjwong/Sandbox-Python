"""

414. Third Maximum Number


Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.


"""


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #
        # max_num is a list of the 3 maximum numbers, smallest on the left, first_max on the right,
        # when new maximums are found, slide left by removing the smallest on the left,
        # and inserting on the right, based on which previous value this current number is greater than
        #
        first_max = 2
        second_max = 1
        third_max = 0
        
        min_val = float('-inf')
        
        max_num = [ min_val, min_val, min_val ]
    
        #
        # iterate through distinct numbers to find the first, second, and third max
        #
        nums = set(nums)
        for num in nums:
            
            #
            # see if num is > first max num
            #
            if num > max_num[first_max]:
                
                max_num.pop(third_max)
                max_num.insert(first_max, num)
            
            #
            # see if num is > second max num
            #
            elif num > max_num[second_max]:
                
                max_num.pop(second_max)
                max_num.insert(second_max, num)
        
            #
            # see if num is > third max num,
            # it does NOT make sense to check for >= here,
            # since if it is equal, we would remove
            # and insert the same value at this same position
            #
            # it makes sense for >= for the previous 2 comparisions
            # ( for first max and second max )
            # because the other max_nums slide to the left
            #
            elif num > max_num[third_max]:
                
                max_num.pop(third_max)
                max_num.insert(third_max, num)
        
        #
        # third max does NOT exist, return first max
        #
        if max_num[third_max] == min_val:
            return max_num[first_max]
        
        #
        # return third max
        #
        else:
            return max_num[third_max]
            
        
def main():
    
    solution = Solution()
    
    print ( "0 == " + str ( solution.thirdMax([0]) ) )
    
    print ( "0 == " + str ( solution.thirdMax([0,1,2]) ) )
    
    print ( "1 == " + str ( solution.thirdMax([0,1,2,3]) ) )
    
    print ( "1 == " + str ( solution.thirdMax([3,2,1,0]) ) )
    
    print ( "1 == " + str ( solution.thirdMax([2, 2, 3, 1]) ) )
    
    
if __name__ == "__main__":
    main()
    
    
    