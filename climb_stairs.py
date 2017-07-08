"""

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? 

Note: Given n will be a positive integer. 


"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        #
        # base cases
        #
        if ( n <= 0 ):
            #
            # [];
            #
            return 0
        
        elif ( n == 1 ):
            #
            # [1];
            #
            return 1
        
        elif ( n == 2 ):
            #
            # [1,1]; [2];
            #
            return 2
        
        #
        # else n >= 3
        #
        solution = [ 0 for i in range(0,n+1)]
        
        solution[0] = 0
        solution[1] = 1
        solution[2] = 2
        
        i = 3
        
        while ( i <= n ):
            #
            # current solution is equal to
            # the sum of the previous 2 solutions
            #
            solution[i] = solution[i-1] + solution[i-2]
            
            #
            # increment i until n inclusive
            #
            i+=1
            
        
        return solution[n]
     
        
def main():
    solution = Solution()
    print ( "0 == " + str ( solution.climbStairs(0) ) )
    print ( "1 == " + str ( solution.climbStairs(1) ) )
    print ( "2 == " + str ( solution.climbStairs(2) ) )
    print ( "3 == " + str ( solution.climbStairs(3) ) )
    print ( "4 == " + str ( solution.climbStairs(4) ) )
    print ( "5 == " + str ( solution.climbStairs(5) ) )
    
if __name__ == "__main__":
    main()