"""

624. Maximum Distance in Arrays


Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a-b|. Your task is to find the maximum distance.

Example 1:
Input: 
[[1,2,3],
 [4,5],
 [1,2,3]]
Output: 4
Explanation: 
One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Note:
Each given array will have at least 1 number. There will be at least two non-empty arrays.
The total number of the integers in all the m arrays will be in the range of [2, 10000].
The integers in the m arrays will be in the range of [-10000, 10000].


"""


import math

class Solution(object):
    
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        
        #
        # find the minimum of all array values, then subtract that
        # from each of the maximums of each array
        #
        # this helps us to find the max min minus all other maxes
        #
        max_min_minus_all_other_maxes = int ( -1 * pow(2,31) )
        min_val = int( pow(2,31) )
        min_index = -1
        
        #
        # find the maximum of all array values, then subtract that
        # from each of the minimums of each array
        #
        # this helps us to find the max max minus all other mins
        #
        max_max_minus_all_other_mins = int ( -1 * pow(2,31) )
        max_val = int ( -1 * pow(2,31) )
        max_index = -1
    
        #
        # find the min value and max value, keep track of the array index
        #
        for i, array in enumerate(arrays):
            
            if array[0] < min_val:
                min_val = array[0]
                min_index = i
                
            if array[-1] > max_val:
                max_val = array[-1]
                max_index = i
                
        #
        # track the min - all other max
        # track the max - all other mins
        #
        # return the max of these 2 values
        #
        for i, array in enumerate(arrays):
            
            #
            # only check rows other that the row which contains min
            #
            if i != min_index:
                max_min_minus_all_other_maxes = \
                    max ( max_min_minus_all_other_maxes, abs ( min_val - array[-1] ) )
                
            #
            # only check rows other than the row which contains max
            #
            if i != max_index:
                max_max_minus_all_other_mins = \
                    max ( max_max_minus_all_other_mins, abs ( max_val - array[0] ) )
        
        return max ( max_min_minus_all_other_maxes, max_max_minus_all_other_mins )
    
        
def main():
    
    solution = Solution()
    
    arrays = [
            [1,2,3],
            [-4,5],
            [-3,1,2,3]
        ]
    
    print ( "8 == " + str ( solution.maxDistance(arrays) ))

    arrays = [
            [0],
            [1],
        ]
    
    print ( "1 == " + str ( solution.maxDistance(arrays) ))

if __name__ == '__main__':
    main()
    
    
    