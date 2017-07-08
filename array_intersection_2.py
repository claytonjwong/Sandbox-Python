"""

350. Intersection of Two Arrays II


Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?


"""

import collections

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if nums1 is None or nums2 is None:
            return []
        
        result = []
        
        #
        # count instances of each number
        #
        c1 = collections.Counter(nums1)
        c2 = collections.Counter(nums2)

        
        #
        # find the counter of smaller length
        # to optimize the array intersection check
        # by iterating through the smaller length list
        # and checking if those values exist
        # in the larger length list
        #
        if len(c1) < len(c2):
            
            smaller_counter = c1
            larger_counter = c2
            
        else: # len(c1) >= len(c2)
            
            smaller_counter = c2
            larger_counter = c1
        
        
        #
        # iterate through the smaller length counter first
        #
        for num in smaller_counter:
        
            #
            # see if the value also exists in the larger length counter
            #
            if num in larger_counter:
                
                #
                # append the number onto the result
                #
                i = min ( smaller_counter[num], larger_counter[num] )
                while i > 0:
                    result.append(num)
                    i -= 1
    
        #
        # return the array intersection
        #
        return result
    
def main():
    
    solution = Solution()
    print ( "[2,2] == " + str ( solution.intersect([1,2,2,1], [2,2]) ))
    
if __name__ == '__main__':
    main()








