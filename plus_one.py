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
                
                #
                # insert a 0 as a placehold since carry over occurs
                #
                digits_plus_one.insert(0, 0)
                
                #
                # since carry over occurred, we need to increment
                # the next most significant digit, see if we are already
                # at the most significant digit,
                # if so, insert 1 in that newly created position
                #
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
            
            #
            # carry over did NOT occur, simply insert the value
            #        
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