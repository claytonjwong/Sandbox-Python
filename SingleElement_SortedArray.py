"""
540. Single Element in a Sorted Array

Given a sorted array consisting of only integers where every element appears twice except
for one element which appears once. Find this single element that appears only once.
"""

class Solution(object):
    
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len ( nums ) - 1
        
        while ( lo < hi ):
            
            mid = ( hi + lo ) / 2
            
            #
            # base case #1
            #
            # [ 1, 1, 2 ]
            #
            if nums [ lo ] == nums [ mid ]:
                return nums [ hi ]
            
            #
            # base case #2
            #
            # [ 1, 2, 2 ]
            #
            elif nums [ mid ] == nums [ hi ]:
                return nums [ lo ]
            
            #
            # base case #3
            #
            # [ 1, 1, 2, 3, 3 ]
            #
            elif nums [ mid - 1 ] != nums [ mid ] and nums [ mid ] != nums [ mid + 1 ]:
                return nums [ mid ]
            
            #
            # check to see if the two digits from the first half and middle are the same
            #
            elif nums [ mid - 1 ] == nums [ mid ]:
                
                #
                # if the middle index is even,
                # then the first half is an odd length ( which contains the single digit )
                # so further check the first half, otherwise, further check the second half
                #
                if mid % 2 == 0:
                    #
                    # further check the first half
                    #
                    hi = mid
                else:
                    #
                    # further check the second half
                    #
                    lo = mid + 1
            
            #
            # check to see if the two digits from the second half and middle are the same
            #
            elif nums [ mid ] == nums [ mid + 1 ]:
                
                #
                # if the middle index is even,
                # then the first half is an even length ( which does NOT contain the single digit )
                # so further check the second half, otherwise, further check the first half
                #
                if mid % 2 == 0:
                    #
                    # further check the second half
                    #
                    lo = mid
                else:
                    #
                    # further check the first half
                    #
                    hi = mid - 1                

      

def main():
    
    import pdb
    pdb.set_trace()
    
    nums = [0,1,1,2,2,5,5]

    solution = Solution()
    print ( solution.singleNonDuplicate(nums) )

            

if __name__ == "__main__":
    main()
    
