"""

LeetCode contest 39: find derangement


"""




class Solution(object):
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        
        if n == 1:
            return 0
        
        #
        # https://en.wikipedia.org/wiki/Derangement
        #
        # !n=(n-1)(!(n-1)+!(n-2))
        #
        # where !n, known as the subfactorial,
        # represents the number of derangements,
        # with the starting values !0 = 1 and !1 = 0.
        #
        
        dp = []
        dp.append(1) #dp[0] = 1
        dp.append(0) #dp[1] = 0
        
        for i in range(2, (n+1) ):
            dp.append ( ( (i-1)*(dp[1]+dp[0]) ) % (10**9+7) )
            dp.pop(0)
        
        return dp[1]
    
    def findDerangement2(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans, a, b = 1, 1, 0
        for i in range(2, n):
            ans, a, b = i * (a+b) % 1000000007, i * (a+b) % 1000000007, a
        return ans if n > 1 else 0
    
def main():
    
    solution = Solution()
    
#     import pdb
#     pdb.set_trace()

    num = 2323
    
    print ( "0 == " + str ( solution.findDerangement(2323) ) + " ==?== " + str ( solution.findDerangement2(2323)))
    
if __name__ == '__main__':
    main()
    
    
    