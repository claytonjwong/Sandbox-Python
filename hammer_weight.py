"""

191. Number of 1 Bits

Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.

"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        #
        # count of the amount of 1s in the binary representation of n
        #
        count = 0
        
        #
        # binary string representation of n
        #
        binary_string = "{:032b}".format(n)
        
        #
        # go through each char in the string, if it is 1, then increment the count by 1
        #
        for bit in binary_string:
            if bit == "1":
                count += 1
                
        return count


def main():
    solution = Solution()
    print ( "3 == " + str ( solution.hammingWeight(11)))

if __name__ == "__main__":
    main()
    
    
    
    