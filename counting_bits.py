"""

338. Counting Bits


Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.


"""

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
    
        """
        dynamic programming plan:
        
        whenever the num is a power of 2,
        the bit count is reset back to 1
        so subtract by the largest power of 2 <= the current index
        in order to find the previously calculated value's index, and add 1 to that value,
        in order to account for the previously caculated value
        along with this new left-most bit set 
        
        
        dp[index] = dp[ index - largest_power_of_2 <= index ] + 1
        
        dp[0] = 0000 0000 = 0
        
        
        Largest power of 2 <= index is 1
        
        dp[1] = 0000 0001 = 1 = dp[1-1] + 1 = dp[0] + 1  
        
        
        Largest power of 2 <= index is 2
        
        dp[2] = 0000 0010 = 1 = dp[2-2] + 1 = dp[0] + 1
        dp[3] = 0000 0011 = 2 = dp[3-2] + 1 = dp[1] + 1
        
        dp[4] = 0000 0100 = 1 = dp[4-4] + 1 = dp[0] + 1
        dp[5] = 0000 0101 = 2 = dp[5-4] + 1 = dp[1] + 1
        dp[6] = 0000 0110 = 2 = dp[6-4] + 1 = dp[2] + 1
        dp[7] = 0000 0111 = 3 = dp[7-4] + 1 = dp[3] + 1
        
        
        Largest power of 2 <= index is 8
        
        dp[8] = 0001 0000 = 1 = dp[8-8] + 1 = dp[0] + 1
        dp[9] = 0001 0001 = 2 = dp[9-8] + 1 = dp[1] + 1
        dp[10]= 0001 0010 = 2 = dp[10-8] + 1 = dp[2] + 1
        dp[11]= 0001 0011 = 3 = dp[11-8] + 1 = dp[3] + 1
        
        """
        
        #
        # iterate from ( 1 to num ) inclusive
        #
        dp = [0] # dp[0] = 0
        
        largest_power_of_2 = 1
        
        for index in range(1, num+1):
            
            if index & (index-1) == 0:
                largest_power_of_2 = index
            
            dp.append( dp[ index - largest_power_of_2 ] + 1 )
            
        return dp[num]
    
    
def main():
    
    solution = Solution()
    
    print ( "dp[0] == 0 == " + str ( solution.countBits(0) ))
    print ( "dp[1] == 1 == " + str ( solution.countBits(1) ))
    print ( "dp[2] == 1 == " + str ( solution.countBits(2) ))
    print ( "dp[3] == 2 == " + str ( solution.countBits(3) ))
    
    print ( "dp[16] == 1 == " + str ( solution.countBits(16) ))
    
    print ( "dp[31] == 5 == " + str ( solution.countBits(31) ))
    
if __name__ == '__main__':
    main()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

