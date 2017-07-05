"""

169. Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

"""


class Solution(object):
    
    def __init__(self):
        self.hashTable = {}
    
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len ( nums )
        
        #
        # intialize all values of the hash table to 0
        #
        for num in nums:
            self.hashTable[num] = 0
        
        #
        # go through each number and incremen the count
        # in the has table
        #
        for num in nums:
            
            self.hashTable[num] += 1
            
            #
            # check if this is the majority element
            #
            if ( self.hashTable[num] > len_nums / 2 ):
                return num
                
        return None
    
def main():
    
    solution = Solution()
    
    import pdb
    pdb.set_trace()
    
    solution.majorityElement([1])

if __name__ == "__main__":
    main()
        