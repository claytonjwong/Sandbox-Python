"""

518. Coin Change 2

https://leetcode.com/problems/coin-change-2/#/description

You are given coins of different denominations and a total amount of money.
Write a function to compute the number of combinations that make up that amount.
You may assume that you have infinite number of each kind of coin.

Note: You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer

"""


class Solution(object):
    def change(self, amount, coins):
        
        #
        # [0:amount]
        #
        dp = [0] * ( amount + 1 )
        
        #
        # there is one and only one way
        # to make change of amount 0
        # by using NO coins at all
        #
        dp[0] = 1
        
        #
        # find all solutions for each coin and add them up
        # as they overlap
        #
        for coin in coins:
            
            #
            # [1:amount]
            #
            for sub_amount in range(1, amount+1):

                #
                # += since the solutions per coin overlap
                #
                # i.e. for sub_amount = 2 and coins 1, 2
                # 
                #      for coin = 1, there is 1 solution for amount 2:
                #      (coin 1 + coin 1)
                #
                #      for coin = 2, there is 1 solution for amount 2:
                #      (coin 2)
                #
                if coin <= sub_amount:
                    dp[ sub_amount ] += dp [ sub_amount - coin ]
                
        return dp[amount]

def main():
    
    solution = Solution()
    
    
    print ( "4 == " + str ( solution.change(5, [1, 2, 5]) ))



if __name__ == '__main__':
    main()
    
    
    
    
    
