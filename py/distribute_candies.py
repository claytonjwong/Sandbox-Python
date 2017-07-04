"""



"""





class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        if candies is None or len(candies)==0:
            return 0
    
        #
        # amount of unique candies
        #
        cnt_unique = len( set(candies) )
    
        #
        # maximum amount of unique candies which can be evenly shared
        #
        max_unique = len(candies)//2
        
        #
        # if more than half are unique, we can only
        # equally distribute half anyhow, so at most
        # return candies//2
        #
        # and at the least return the amount
        # of candies in the unique set
        #
        return min( cnt_unique, max_unique )
    
    
def main():
    
    solution = Solution()
    
    print ( "0 == " + str ( solution.distributeCandies(None)))
    
    print ( "0 == " + str ( solution.distributeCandies([])))
    
    print ( "1 == " + str ( solution.distributeCandies([0,0])))
    
    print ( "1 == " + str ( solution.distributeCandies([0,0,0,0])))
    
    print ( "2 == " + str ( solution.distributeCandies([0,0,0,1])))
    
    print ( "2 == " + str ( solution.distributeCandies([0,0,1,2])))
    
    print ( "2 == " + str ( solution.distributeCandies([0,1,2,3])))
        
        
        
if __name__ == '__main__':
    main()
    
    
    