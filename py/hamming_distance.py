"""

461. Hamming Distance

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 2^31.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.


"""

from collections import Counter

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        #
        # different bits are x XOR y
        #
        # use str.format() in order to create a string of 0s and 1s ( 32-bit binary number )
        #
        # use collections.Counter to create a new counter and return Counter['1'],
        # which is the amount of 1s ( different bits between x and y ) 
        #
        return Counter("{:032b}".format(x ^ y))['1']
    
    
def main():
    
    solution = Solution()
    
    print ( "2 == " + str ( solution.hammingDistance(1, 4) ))
    
    
if __name__ == '__main__':
    main()








