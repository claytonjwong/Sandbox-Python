"""

215. Kth Largest Element in an Array


Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.


"""


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        min_val = float('-inf')
        largest = []
        
        #
        # largest is a list of the k largest values,
        # initially set all elements to the min val
        #
        # largest on the right
        # smallest on the left
        #
        i=0
        while i < k:
            largest.append(min_val)
            i+=1

        
        for num in nums:
            #
            # iterate through the largest list backwards,
            # and see if num is larger than any of the k largest values
            # if so, then insert num in the proper position, and
            # shift all over values in the largest list to the left
            #
            j = k - 1
            
            while j >= 0:
            
                if num > largest[j]:
                    largest.pop(0)
                    largest.insert(j, num)
                    break
                    
                j -= 1
    
        #
        # the kth largest will exist as the first element in the largest list
        #    
        return largest[0]
    
    
def main():
    
    import pdb
    
    solution = Solution()
    
    print ( "5 == " + str ( solution.findKthLargest([3,2,1,5,6,4], 2) )) 
    
    pdb.set_trace()
    print ( "-1 == " + str ( solution.findKthLargest([-1,-1], 2) )) 

if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
