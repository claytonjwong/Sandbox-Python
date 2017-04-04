"""

Implement int sqrt(int x).

Compute and return the square root of x.


"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        i = x
        
        while ( i * i > x ):
            
            i = ( i + x/i ) / 2
            
        return i
    
    
def main():
    
    solution = Solution()
    print ( "5 == " + str ( solution.mySqrt(25) ) )
    print ( "12 == " + str ( solution.mySqrt(144) ) )
    
if __name__ == "__main__":
    main()