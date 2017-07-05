"""

475. Heaters

https://leetcode.com/problems/heaters/#/description


Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:
Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
As long as a house is in the heaters' warm radius range, it can be warmed.
All the heaters follow your radius standard and the warm radius will the same.
Example 1:
Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
Example 2:
Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.



Runtime Error Message:
Line 36: IndexError: list assignment index out of range
Last executed input:
[1,5]
[10]



"""


import math

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        
        #
        # sanity checks
        #
        if houses is None or heaters is None:
            return 0
        
        if len(houses)==0 or len(heaters)==0:
            return 0

        #
        # hh is houses with heaters
        # set houses in the same positions as
        # heaters to 1, and all other house positions remain 0 ( no heater )
        #
        heaters.sort()
        houses.sort()
        
        max_position = max( heaters[-1], houses[-1] )
        
        hh = [0] * max_position
        
        for heater in heaters:
            hh[heater-1] = 1
        
        #
        # between houses case:
        #
        # count the maximum number of 0s between the 1s
        # and ceil divide that by 2 in order to get the min
        # radius
        #
        
        #
        # corner house case:
        #
        # check for houses on the "edge" (left-most and right-most homes)
        # count the number of 0s between the left-most and right-most homes
        # and their closest heater.  The max number of 0s is the radius required
        # to heat these homes
        #
        
        #
        # iterate from 1 to len(hh) inclusive, use curr and prev to keep
        # track of the current and previous heater positions in order
        # to calculate how many houses are between the heaters
        #
        # use max_edge to track the max distance between the left-most
        # and right-most homes, and use max_mid to track the max distance
        # between homes
        #
        curr = -1
        prev = -1
        max_edge = 0
        max_mid = 0
        for i in range(0,len(hh)):
            
            #
            # new heater found, update curr/prev positions
            #
            if hh[i]==1:
                prev = curr
                curr = i

                #
                # left-most edge-case
                #
                if prev==-1 and curr>=0:
                    max_edge = max( max_edge, i )

                #
                # between houses case
                #
                if prev>=0 and curr>=0:
                    #
                    # non-inclusive bounds, so substract 1
                    #
                    max_mid = max( max_mid, (curr-prev-1)//2 )
            
            #
            # right-most edge-case, subtract the most current
            # heater position from i in order to count the homes
            # on this edge
            #
            if i==len(hh)-1:
                max_edge = max( max_edge, i-curr )
                
        return max( max_edge, max_mid )
    
    
def main():
    
    solution = Solution()
    
    print ( "0 == " + str ( solution.findRadius(None, []) ))
    print ( "0 == " + str ( solution.findRadius([], []) ))
    

    
    print ( "4 == " + str ( solution.findRadius([1,5], [5]) ))
    
    print ( "9 == " + str ( solution.findRadius([1,5], [10]) ))
    
    
    print ( "3 == " + str ( solution.findRadius([1,2,3,4,5,6,7,8,9,10], [3,10]) ))
    
    
    print ( "1 == " + str ( solution.findRadius([1,2,3,4],[1,4])))
    
    print ( "1 == " + str ( solution.findRadius([1,2,3],[2])))
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
        