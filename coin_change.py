"""

You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1. 

Example 1:
 coins = [1, 2, 5], amount = 11
 return 3 (11 = 5 + 5 + 1) 

Example 2:
 coins = [2], amount = 3
 return -1. 

Note:
 You may assume that you have an infinite number of each kind of coin


"""

 




class Solution(object):
    
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if ( len ( coins ) == 0 ):
            return -1
        
        if ( amount <= 0 ):
            return 0
        
        coins.sort(reverse=True)
        return self.coinChangeHelper(coins, amount)
    
            
    def coinChangeHelper(self, coins, amount):
        """
        
        assume coins is sorted in reverse order
        
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        #
        # change amount is the value of the index of this dict
        #
        # the value stored in this dict is the coin count
        # which corresponds to the amount of coins used
        # to make up this demoniation
        #
        # example with coins [1,2,5]
        #
        # change_coin_count [ 8 ] = 3  ( 3 coins used: 5,2,1)
        # change_coin_count [ 10 ] = 2  ( 2 coins used: 5,5)
        #
        # initialize all to -1
        #
        change_coin_count = {}
        
        #
        # i is the current amount of change,
        # iterate from ( 1 to amount ) inclusive
        #
        for i in range(1, amount+1):
            
            #
            # initialize to -1 to assume there is no coin solution for this i amount
            #
            change_coin_count[i] = -1
            
            #
            # go through each coin in reverse order
            #
            for coin in coins:

                #
                # see if the current i amount is equal to this coin
                #    
                if ( i == coin ):
                    
                    #
                    # there is one solution ( this coin )
                    #
                    change_coin_count[i] = 1
                    break
                   
                #
                # see if there is a previous solution minus this coin
                #
                elif ( i - coin >= 1 and change_coin_count[ i - coin ] != -1 ):
                    
                    #
                    # with the addition of this coin,
                    # there is the previous solution count
                    #
                    # + 1 ( this coin )
                    #
                    change_coin_count[i] = 1 + change_coin_count[ i - coin ]
                    break
                    
        
        return change_coin_count [ amount ]
                
        
def main():

    solution = Solution()
    print ( "20 == " + str ( solution.coinChange([419, 408, 186, 83], 6249) ) )
    
    
if __name__ == "__main__":
    main()
    
    
    