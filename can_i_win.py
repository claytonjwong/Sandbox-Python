"""

Input:
maxChoosableInteger = 10
desiredTotal = 11

Output:
false

Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.

"""

class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        
        #
        # check to see if the sum of all ints
        # from ( 1 to maxChoosableInteger ) inclusive
        # can reach the desired total
        #
        # sum of ( 1 to n ) = n(n+1)/2
        #
        n = maxChoosableInteger
        if ( n * ( n + 1 ) / 2 < desiredTotal ):
            return False
        
        
        return False
    
    
def main():
    
    solution = Solution()
    
    print ( "false == " + str ( solution.canIWin(10, 11)))
    
if __name__ == "__main__":
    main()