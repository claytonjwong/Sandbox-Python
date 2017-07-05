"""
Given two binary strings, return their sum (also a binary string). 

For example,
 a = "11"
 b = "1"
 Return "100". 
"""

class Solution(object):
    def addBinary(self, str_a, str_b):
        """
        :type str_a: str
        :type str_b: str
        :rtype: str
        """
        
        sum = ""
        
        carry_over = False
        
        #
        # iterate though each string from right-to-left
        #
        neg_len_a = -1 * len ( str_a )
        neg_len_b = -1 * len ( str_b )
        
        i = -1
        
        while ( i >= neg_len_a and i >= neg_len_b ):
            
            #
            # both digits to add up are 1, so the sum is 10,
            # append 0 for current right-most position and track carry over
            # if there was str_a previous carry over,
            # then append 1 for current right-most position
            #
            if ( str_a[i] == str_b[i] == "1" ):
                
                if ( carry_over ):
                    sum = "1" + sum 
                else:
                    sum = "0" + sum
                    
                carry_over = True
            
            #
            # both digits to add are 0, so the sum is 0
            # unless there was str_a previous carry over
            #
            elif ( str_a[i] == str_b[i] == "0"):
                
                if ( carry_over ):
                    sum = "1" + sum
                else:
                    sum = "0" + sum 
                    
                carry_over = False
            
            #
            # EITHER
            # str_a[i] is 0 and str_b[i] is 1
            # OR
            # str_a[i] is 1 and str_b[i] is 0
            #
            else:
                
                if ( carry_over ):
                    sum = "0" + sum
                    carry_over = True
                else:               
                    sum = "1" + sum
                    carry_over = False
            
                
            #
            # decrement i in order to move from right-to-left
            #
            i -= 1
        
        
        #
        # see if there is more A left over,
        # then more negative, the larger length
        # so if str_a < str_b, then len of str_a is larger than len of str_b
        #
        if ( neg_len_a < neg_len_b ):
            
            while ( i >= neg_len_a ):
                
                if ( carry_over ):
                    
                    #
                    # if there was a previous carry over,
                    # then add it here and track new potential carry overs
                    #
                    if ( str_a[i] == "0" ):
                        sum = "1" + sum 
                        carry_over = False
                    else:
                        sum = "0" + sum 
                        carry_over = True
            
                else:
                    
                    #
                    # if there are no more carry overs, then
                    # copy what is left of the left-most digits
                    # directly into the sum
                    #
                    sum = str_a[neg_len_a:i+1] + sum
                    break
            
                i -= 1
        
        #
        # otherwise there may be more B left over
        #
        else:
            
            while ( i >= neg_len_b ):
                
                if ( carry_over ):

                    #
                    # if there was a previous carry over,
                    # then add it here and track new potential carry overs
                    #
                    if ( str_b[i] == "0" ):
                        sum = "1" + sum 
                        carry_over = False
                    else:
                        sum = "0" + sum 
                        carry_over = True
            
                else:
                    
                    #
                    # if there are no more carry overs, then
                    # copy what is left of the left-most digits
                    # directly into the sum
                    #
                    sum = str_b[neg_len_b:i+1] + sum
                    break
            
            
                i -= 1
        
        #
        # at the very end if there is still a carry over,
        # then insert it here
        #
        if ( carry_over ):
            sum = "1" + sum    
        
        return sum
        
        
def main():
    
    
    
    solution = Solution()
    
    print ( "10 == " + str ( solution.addBinary("1", "1") ) )
    
    print ( "100 == " + str ( solution.addBinary("11", "1") ) )
    
    print ( "10101 == " + str ( solution.addBinary("1010", "1011") ) )
    
    print ( "110110 == " + str ( solution.addBinary("100", "110010") ) )
    
    print ( "110001 == " + str ( solution.addBinary("101111", "10") ) )
    
#     import pdb
#     pdb.set_trace()
    
    print ( "1001001 == " + str ( solution.addBinary("110010", "10111") ) )
    
    
    
    
if __name__ == "__main__":
    main()