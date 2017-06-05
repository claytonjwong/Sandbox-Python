"""

220. Contains Duplicate III


Given an array of integers, find out whether there are two distinct indices
i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t
and the absolute difference between i and j is at most k.


"""


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        nearby_nums = {}
        
        #
        # compare each number within the current hash of nearby numbers
        # to see if the difference in the values is at most t
        #
        for i,curr_num in enumerate(nums):
            
            for nearby_num_idx in nearby_nums:
                 
                if abs( curr_num - nearby_nums[nearby_num_idx] ) <= t:
                    return True
            
            #
            # add entry to the hash table, the array index is used as the key,
            # and the value of the current number is stored as the value
            #
            nearby_nums[i] = curr_num
            
            #
            # delete nearby num which is no longer k indices away,
            # this allows the nearby_nums hash to become a sliding window
            #
            try:
                del nearby_nums[i-k]
            #
            # KeyError is thrown when i-k is < 0, since these entries do NOT exist
            #
            except KeyError:
                pass
        
        
        return False
    

def main():
    
    import pdb
    
    pdb.set_trace()
    
    solution = Solution()
    
    print ( "True == " + str ( solution.containsNearbyAlmostDuplicate([-1,-1], 1, 0) ) )
    

if __name__ == "__main__":
    main()
        
        
        
        
        
        
        
        
        
        
        