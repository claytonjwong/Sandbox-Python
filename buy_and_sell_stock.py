"""

121. Best Time to Buy and Sell Stock


Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.


"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        len_prices = len ( prices )
        
        #
        # there must be at least 2 prices
        # in order to buy and sell
        #
        if ( len_prices < 2 ):
            return 0
        
        #
        # use Kadane's algorithm ( https://en.wikipedia.org/wiki/Maximum_subarray_problem )
        # in order to find the maximum sub-array difference
        #
        curr_diff = max_diff = 0
        i=1
        while ( i < len_prices ):
            
            #
            # find max sub-array difference
            # either the current price is included
            # in the current sub-array or it is not
            #
            # current difference =   previous difference ( this is why += is used here )
            #                      + the price difference between curr and prev array elements
            #
            curr_diff += prices[i] - prices[i-1]
            
            #
            # if there is no profit ( i.e. current diff < 0 ), then do NOT sell
            # instead, count the current difference as 0 ( since we are holding the stock )
            #
            curr_diff = max ( 0, curr_diff  )
            
            #
            # check if the current difference is greater than the max difference
            #
            max_diff = ( max ( max_diff, curr_diff ) )
            
            #
            # iterate to next position
            #
            i += 1
            
        #
        # return the maximum difference
        #
        return max_diff

    
def main():
    
    solution = Solution()
    
    print ( "5 == " + str( solution.maxProfit([7, 1, 5, 3, 6, 4])))
    print ( "0 == " + str( solution.maxProfit([7, 6, 4, 3, 1])))
    
    
    
if __name__ == "__main__":
    main()
    
    
    