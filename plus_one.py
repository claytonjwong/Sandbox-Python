"""

Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        digits_plus_one = []
        
        #
        # flag used to keep track of wrap around ( base 10 )
        #        
        carry_over = False
        
        #
        # iterate from right to left ( n-1 to 0 )
        #
        
        i = len ( digits ) - 1
        
        #
        # add one onto the right-most digit
        #
        digits[i] += 1
        
        while ( i >= 0 ):

            #
            # see if carry over occurs
            #
            if ( digits[i] == 10 ):
                
                digits_plus_one.insert(0, 0)
                
                if ( i == 0 ):
                    #
                    # left-most digit, append 1 onto new position
                    #
                    digits_plus_one.insert(0, 1)

                else:
                    #
                    # increment next digit if not the left-most digit
                    #
                    digits[i-1] += 1
                    
            else:
                digits_plus_one.insert(0, digits[i])    
            
            #
            # decrement i moving from n-1 to 0
            #
            i -= 1

        return digits_plus_one
    
    
def main():
    
#     import pdb
#     pdb.set_trace()
#     
    solution = Solution()
    print ( "10 == " + str ( solution.plusOne([9]) ) )
            
if __name__ == "__main__":
    main()