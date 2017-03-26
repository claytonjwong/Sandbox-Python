class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        #
        # keep track of the sum of the divisors
        #
        sum = 0
        

        for i in range ( 1, int ( num / 2 ) + 1 ):
            
            #
            # if num is evenly divisible by i,
            # then add i onto the sum
            #
            if ( num % i == 0 ):
                sum += i
        
        #
        # if the sum of the divisors is equal to the number,
        # then return True, since this is a perfect number,
        # otherwise return False
        #        
        if ( sum == num ):
            return True
        else:
            return False
        

def main():
    solution = Solution()
    
    print ( "28: " + str ( solution.checkPerfectNumber(28) ) )

if __name__ == "__main__":
    main()