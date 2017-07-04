"""

476. Number Complement

Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.


"""

import math

class Solution(object):
    
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        #
        # "{:032b}".format(5)  = '00000000000000000000000000000101'
        #
        # "{:032b}".format(5).find('1') = 29, and 32 - 29 = 3
        #
        # bit_mask = 2^3 = 8   = '00000000000000000000000000001000'
        #
        # bit_mask = 8 - 1 = 7 = '00000000000000000000000000000111'
        #
        # 7 XOR 5 = 2          = '00000000000000000000000000000010'
        #
        left_most_bit_pos = 32 - int ( "{:032b}".format(num).find('1') )
    
        bit_mask = int( math.pow(2, left_most_bit_pos) ) - 1
        
        return bit_mask ^ num
    
    
def main():
    
    solution = Solution()
    
    print ( "2 == " + str ( solution.findComplement(5) ))
    
if __name__ == '__main__':
    main()
    
    
    
    