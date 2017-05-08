"""

Given an integer array nums, find the sum of the elements between indices i and j (i <= j), inclusive.

Example:

Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3


"""


class NumAndSum(object):
    
    def __init__(self, num, sum):
        self.num = num
        self.sum = sum

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.sums = {}
                
    def get_sum(self, index):
        
        if ( index < 0 ):
            return 0
        
        len_sums = len ( self.sums )
        len_nums = len ( self.nums )
        
        #
        # if the index is less than the lenth of the sums,
        # then we have already calculated this value
        # simply return it here
        #
        if ( index < len_sums ):
            return self.sums[index]        
        
        #
        # we have NOT yet calculated the sum up to this index
        # go ahead and calculate it now
        #
        i = len_sums
        while ( i <= index and i < len_nums ):
            
            if ( i == 0 ):
                self.sums[0] = self.nums[0]
            else:
                #
                # the current sum = the current num + the previous sum
                #
                self.sums[i] = ( self.nums[i] + self.sums[i-1])
            
            i += 1
            
        return self.sums[index]


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.get_sum(j) - self.get_sum(i-1)

        
def main():
    
    nums = [-2, 0, 3, -5, 2, -1]
    
    obj = NumArray(nums)
    
    print ( "1 == " + str ( obj.sumRange(0, 2) ) )
    print ( "-1 == " + str ( obj.sumRange(2, 5) ) )
    print ( "-3 == " + str ( obj.sumRange(0, 5) ) )

if __name__ == "__main__":
    main()
    
    
