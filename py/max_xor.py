"""

I THINK MY ORIGINAL THOUGHT WAS INCORRECT


421. Maximum XOR of Two Numbers in an Array


Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.

01010101010101010101010101010101
10987654321098765432109876543210
00000000000000000000000000011001
00000000000000000000000000000101
00000000000000000000000000011100

"""


class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #
        # use a mask to check for the max "odd" bit value and max "even" bit
        #
        # even 32-bit mask is 0x55555555 ( since 0x5 = 0101 )
        # odd 32-bit mask is 0xAAAAAAAA ( since 0xA = 1010 )
        #
        curr_max_even, prev_max_even, curr_max_odd, prev_max_odd = 0, 0, 0, 0
        
        
        for num in nums:
            
            even_val = num & 0x55555555
            odd_val  = num & 0xAAAAAAAA
            
            #
            # store this value as the max even/odd,
            # whichever is largest, in case of a tie,
            # choose whichever odd/even bucket that
            # contains the smaller prev max
            #
            if even_val > odd_val and even_val > curr_max_even:
                
                #
                # even > odd, update even max
                #
                prev_max_even = curr_max_even
                curr_max_even = num
                
                #
                # check if prev max even > curr max odd,
                # if so, then update curr max odd
                #
                if prev_max_even > curr_max_odd:
                    prev_max_odd = curr_max_odd
                    curr_max_odd = prev_max_even
                
            elif odd_val > even_val:
                
                #
                # odd > even, update odd max
                #
                prev_max_odd = curr_max_odd
                curr_max_odd = num
                
                #
                # check if the prev odd max > curr max even
                # if so, then update the curr max even
                #
                if prev_max_odd > curr_max_even:
                    prev_max_even = curr_max_even
                    curr_max_even = prev_max_odd
    
            else: # even_val == odd_val
                
                #
                # set the max to the odd/even bucket which has the smallest prev max
                #
                if curr_max_even > curr_max_odd:
                    curr_max_odd = num
                else:
                    curr_max_even = num
                
        return curr_max_even ^ curr_max_odd
    
def main():
    
    import pdb
    pdb.set_trace()
    
    solution = Solution()

    print ( "28 == " + str ( solution.findMaximumXOR([3, 10, 5, 25, 2, 8]) ))
    

if __name__ == '__main__':
    main()







