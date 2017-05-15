"""

198. House Robber

You are a professional robber planning to rob houses along a street.

Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them

is that adjacent houses have security system connected and it will automatically contact the police

if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,

determine the maximum amount of money you can rob tonight without alerting the police.


"""

class Solution(object):
    def rob(self, nums):
        """
        
        robery is performed based on the following recursive algorithm:
        
        f(0) = n[0]
        f(1) = n[1]
        f(i) = max ( f(i-2) + n[i], f(i-1) )
        
        :type nums: List[int]
        :rtype: int
        
        """
        len_nums = len ( nums )
        
        i, prev, curr = 0, 0, 0

        while ( i < len_nums ):
            
            #
            # store current to set prev to this value later on
            # in order to prepare for the next iteration
            # which needs to keep track of previous previous current ( prev )
            #
            temp_curr = curr
            
            #
            # f(i): curr is the current current which is the max of:
            #
            # f(i-1): curr -- the previous current
            # f(i-2): prev -- the previous previous current
            #
            curr = max ( prev + nums[i], curr )
            
            #
            # store prev as the previous current
            #
            prev = temp_curr
            
            i += 1
            
        return curr

    
        
def main():
    solution = Solution()
    
    print ( "4 == " + str ( solution.rob([2,1,1,2]) ) )
    
if __name__ == "__main__":
    main()
    
    
    