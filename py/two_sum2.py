"""

167. Two Sum II - Input array is sorted 

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2 


"""

class Solution(object):
    
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
            
        
        len_numbers = len ( numbers )
        
        if ( target == 0 and len_numbers > 1 ):
            if ( numbers[0] == numbers[1] == 0 ):
                return 1,2
        
        #
        # iterate from 0 to len_numbers - 2 inclusive
        #
        i = 0
        while ( i < len_numbers - 1 ):
            
            while ( numbers[i] == 0 ):
                i += 1
            
            #
            # iterate from i + 1  to len_numbers - 1 inclusive
            #            
            j = i + 1            
            while ( j < len_numbers ):
                
                if ( numbers[i] + numbers[j] == target ):
                    
                    #
                    # convert 0-based index to 1-based index
                    #
                    return i+1,j+1
                
                j += 1
            
            i += 1
    
        return -1,-1
    
def main():
    
    solution = Solution()
    
    index1, index2 = solution.twoSum([2,7,11,15], 9)
    
    print ( "index1=1: " + str ( index1 ) )
    print ( "index2=2: " + str ( index2 ) )
    
    
if __name__ == "__main__":
    main()