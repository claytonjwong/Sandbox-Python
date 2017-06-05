"""

219. Contains Duplicate II

Given an array of integers and an integer k, find out whether there are two distinct indices
i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.



"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        len_nums = len ( nums )
        hash = {}
        
        #
        # go through each number and see if it exists in the hash table
        #
        # if the lookup fails, KeyError exception is thrown,
        # so add the num to hash
        #
        i=0
        for i in range(0,len_nums):
            try:
                #
                # see if duplicate already exists
                # which is at most k indices away
                #
                if ( i - hash[ nums[i] ] <= k ):
                    return True
                #
                # see if duplicate already exists
                # which is greater than k indices away
                #
                elif ( hash[ nums[i] ] is not None ):
                    #
                    # update the hash vaue as the current index
                    #
                    hash [ nums[i] ] = i
                
            except KeyError:
                #
                # add entry by setting the hash value as the current index
                #
                hash[ nums[i] ] = i
    
        return False
    
def main():
    
    import pdb
    pdb.set_trace()
    
    solution = Solution()
    print("False == " + str ( solution.containsNearbyDuplicate([0,1,0],1) ) )
    

if __name__ == "__main__":
    main()







