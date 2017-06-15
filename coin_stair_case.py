"""

441. Arranging Coins

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.

"""

class Solution(object):
    
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        
        while True:
            
            #
            # see if we can make a stair by subtracting
            # the amount of coins needed for this stair
            # if n is NOT negative, then we had enough coins
            #
            n -= i
            
            if n < 0:
                break
            
            #
            # the next stair will take i+1 coins to fill
            #
            i += 1
    
        #
        # we had sufficient coins up to, but NOT including this stair
        #
        return i - 1
    
    
def main():
    
    solution = Solution()
    print ( "3 == " + str ( solution.arrangeCoins(8) ))
    
if __name__ == "__main__":
    main()












