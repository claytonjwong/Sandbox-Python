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
        
        #
        # there is no nearby duplicate which is 0 indices away, 
        # this would just be the same number
        #
        if k == 0:
            return False
        
        #
        # compare each number within the current hash of nearby numbers
        # to see if the difference in the values is at most t
        #
        nearby_nums = {}
        for i,curr_num in enumerate(nums):
            
            #
            # add the current number into a nearby bucket, these buckets are used as the key
            # in the dict nearby_nums, since the difference between nums[i] and nums[j] can be
            # at most t, divide the value of the current number by t in order to decide which
            # bucket the number goes into, if t is 0, then the key is the number value itself
            #
            nearby_bucket = curr_num // t if t > 0 else curr_num
            
            #
            # we only need to check the current bucket, and the bucket to the left and right
            # in order to see if there is a number whose absolute difference with the current number
            # is at most t
            #
            for nearby_bucket_idx in [nearby_bucket - 1, nearby_bucket, nearby_bucket + 1 ]:
                
                if  nearby_bucket_idx is not None \
                and nearby_bucket_idx in nearby_nums \
                and abs( curr_num - nearby_nums[nearby_bucket_idx] ) <= t:
                    return True
            
            #
            # add entry to the hash table, the nearby_bucket is used as the key,
            # and the value of the current number is stored as the value
            #
            nearby_nums[nearby_bucket] = curr_num
            
            #
            # delete nearby num which is no longer k indices away,
            # this allows the nearby_nums hash to become a sliding window
            #
            # calculate the index to remove as the value of the number
            # k indices away divided by t
            #
            k_indices_away = i - k
            
            if ( k_indices_away >= 0 ):
                no_longer_nearby_bucket = nums [ k_indices_away ] // t if t > 0 else nums [ k_indices_away ]
                del nearby_nums[ no_longer_nearby_bucket ]

        #
        # no numbers match the nearby duplicate criteria
        #
        return False
    

def main():
    
    import pdb
    
    pdb.set_trace()
    
    solution = Solution()
    
    print ( "True == " + str ( solution.containsNearbyAlmostDuplicate([1,3,1], 1, 1) ) )
    

if __name__ == "__main__":
    main()
        
        
        
        
        
        
        
        
        
        
        