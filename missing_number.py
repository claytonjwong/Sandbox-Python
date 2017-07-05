"""

268. Missing Number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #
        # using the formula for the sum from 0 to n as: n(n+1)/2
        #
        len_nums = len ( nums )
        sum_of_series = len_nums * ( len_nums + 1 ) / 2
        
        sum_of_nums = 0
        for num in nums:
            sum_of_nums += num
        
        #
        # the missing number is the sum of the series minus the sum of the actual array
        #
        return sum_of_series - sum_of_nums
    
def main():
    
    solution = Solution()
    
    print ( "2 == " + str ( solution.missingNumber([0,1,3]) ) )


if __name__ == "__main__":
    main()




