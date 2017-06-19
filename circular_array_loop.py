"""

457. Circular Array Loop


You are given an array of positive and negative integers. If a number n at an index is positive, then move forward n steps. Conversely, if it's negative (-n), move backward n steps. Assume the first element of the array is forward next to the last element, and the last element is backward next to the first element. Determine if there is a loop in this array. A loop starts and ends at a particular index with more than 1 element along the loop. The loop must be "forward" or "backward'.

Example 1: Given the array [2, -1, 1, 2, 2], there is a loop, from index 0 -> 2 -> 3 -> 0.

Example 2: Given the array [-1, 2], there is no loop.

Note: The given array is guaranteed to contain no element "0".

Can you do it in O(n) time complexity and O(1) space complexity?

"""

class Solution(object):
    
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        #
        # iterate through each number, checking for a loop at each of these starting indexes
        #
        for i, num in enumerate(nums):
            
            #
            # skip elements which have already been found to be a part of an invalid loop
            #
            if num == 0:
                continue
            
            #
            # start at index i, and increment next index until a loop or invalid loop is found
            #
            start_idx, next_idx = i, i
            
            #
            # only traverse forward or backwards by len(nums) "hops"
            # this is the worse case amount of hops needed to traverse
            # forward one hop at a time [ 1, 1, 1, etc... ] or
            # backward one hop at a time [ -1, -1, -1, etc... ] 
            #
            hops = 0
            while hops < len(nums):
                
                #
                # current index for this iteration
                # is the next index calculated from the previous iteration
                #
                curr_num = nums[next_idx]
                
                #
                # calculate the next hop's index by adding the current index's
                # value onto the current index, mod by len for wrap-arounds
                #
                next_idx = ( next_idx + curr_num ) % len(nums)

                #
                # before we hop forward/backwards, ensure that we continue
                # moving in the same direction as the starting direction
                #
                if not self.same_direction( nums[next_idx], nums[start_idx] ):
                    #
                    # invalid loop, set this value to 0 in order to bypass
                    # this value when checking for future loops
                    #
                    nums[next_idx] = 0
                    break

                #
                # loop found, see how many hops are included in hte loop
                #
                if next_idx == start_idx:
                
                    #
                    # we did NOT move at all ( hops==0 )
                    # we moved forward to wrap-around one hop to same index
                    # or we moved backwards to wrap-around one hop to the same index
                    #
                    # this is NOT a loop, since a loop starts and ends at a particular index
                    # with more than 1 element along the loop.
                    #
                    # If hops == 0, then there is 0 elements along the "fake loop"
                    #
                    if hops == 0:
                        #
                        # invalid loop, set this value to 0 in order to bypass
                        # this value when checking for future loops
                        #
                        nums[next_idx] = 0
                        break
                    
                    else:
                        #
                        # loop found with 1 or more elements along the loop
                        #
                        return True
                
                #
                # we have moved one hop without finding a loop yet,
                # increment hop count and iterate again
                #
                hops += 1
        
        #
        # no loop found
        #
        return False
    
    
    def same_direction(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: bool
        """
        return ( a > 0 and b > 0 ) or ( a < 0 and b < 0 )
    
    
def main():
    
    solution = Solution()
    
#     
#     import pdb
#     pdb.set_trace()
    print ("True == " + str ( solution.circularArrayLoop([-2,-1,1,-2,2]) ))
                                                          
    print ("False == " + str ( solution.circularArrayLoop([-1,2]) ))          
    
    print ("True == " + str ( solution.circularArrayLoop([3,1,2]) ))            

if __name__ == '__main__':
    main()







