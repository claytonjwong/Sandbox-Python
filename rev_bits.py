"""

190. Reverse Bits

Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

"""


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        bin = 0
        rev = 0
        
        #
        # use built-in format function in order to change the integer n
        # into a zero-filled 32 char string binary representation of n
        #
        # https://docs.python.org/2/library/string.html#format-specification-mini-language
        #
        bin = '{:032b}'.format(n)
        
        #
        # use extended slices in order to reverse the binary string
        #
        # https://docs.python.org/2.3/whatsnew/section-slices.html
        #
        rev = bin[::-1]
        
        #
        # convert to int from binary (base 2) string
        #
        return int ( rev, 2 )
    
    
def main():
    
    solution = Solution()
    
    import pdb
    pdb.set_trace()
    
    print ( "964176192 == " + str ( solution.reverseBits(43261596)))
    
if __name__ == "__main__":
    main()
    
    
    