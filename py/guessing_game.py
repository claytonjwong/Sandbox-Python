"""

374. Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example:
n = 10, I pick 6.

Return 6.

"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):
def guess(n):
    if n == 1:
        return 0
    elif n > 1:
        return -1
    elif n < 1:
        return 1

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.guessNumberHelper( 1, n, n )
    
    def guessNumberHelper(self, min_n, max_n, half_n ):
        """
        :type min_n: int
        :type max_n: int
        :type half_n: int
        :rtpye: int
        """
        
        ans = guess( half_n )
        
        if ans < 0:
            #
            # lower half
            #
            return self.guessNumberHelper( min_n, half_n, ( min_n + half_n ) // 2 )
        
        elif ans > 0:
            #
            # upper half
            #
            return self.guessNumberHelper( half_n, max_n, ( half_n + max_n ) // 2 )
        
        else:
            #
            # ans == 0
            #
            return half_n
            
    
    
def main():
    
    import pdb
    pdb.set_trace()

    solution = Solution()
    solution.guessNumber(1)

if __name__ == "__main__":
    main()















