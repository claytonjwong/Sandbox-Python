"""

Given two integers, swap the right-most N bits

"""

class Solution(object):
    
    def swap(self, x, y, n):
        """
        :type x,y,n: int
        :rtype: List[int]
        """
        
        #
        # bounds check to ensure n >= 1,
        # ( the minimum amount of bits to swap is 1 )
        #
        if ( n <= 0 ):
            return [x,y]
        
        #
        # optimization for large N and small x,y
        # we can simply return these integers swapped completely
        # rather than swapping bit-by-bit in piecemeal fashion
        #
        largest = pow ( 2, n )
        if ( x < largest and y < largest ):
            return [y,x]
        
        #
        # optimization if x == y, then simply return these values
        # there is no swapping to be performed for this use case
        #
        if ( x == y ):
            return [x,y]
        
        #
        # use i in order to iterate through each bit position
        # from right-to-left and swap the bits between x and y
        #
        i = 0
        while ( i < n ):
            
            #
            # calculate the current bit position by raising 2^i
            #
            curr_bit = pow ( 2, i )
            
            #
            # only perform bit swap if the bits are NOT equal
            #
            # either x=0 and y=1
            #     or x=1 and y=0
            #
            if ( x & curr_bit != y & curr_bit ):
                
                #
                # x=1 and y=0
                #
                if ( x & curr_bit ):
                    x = x ^ curr_bit # 1 ^ 1 = 0
                    y = y | curr_bit # 0 | 1 = 1
                                              
                #
                # x=0 and y=1
                #
                else:
                    x = x | curr_bit # 0 | 1 = 1
                    y = y ^ curr_bit # 1 ^ 1 = 0
            
            #
            # increment i to check on the next bit position
            #
            i += 1
        
        
        return [x, y]

#
# test cases
#
def unit_test(solution):
    
    x = 7 # 0111
    y = 8 # 1000
    
    #
    # swap last 2 bits
    #
    # x = 7 = 0111 ==> 0100 = 4
    # y = 8 = 1000 ==> 1011 = 11 
    #
    new_x, new_y = solution.swap(x,y,2)
    
    print ("swap last 2 bits...")
    print ("x = 7 = 0111 ==> 0100 = 4: " + str(new_x) )
    print ("y = 8 = 1000 ==> 1011 = 11: " + str(new_y) )
    print ("\n\n\n")
    
    #
    # swap last 3 bits
    #
    # x = 7 = 0111 ==> 0000 = 0
    # y = 8 = 1000 ==> 1111 = 15 
    #
    new_x, new_y = solution.swap(x,y,3)
    
    print ("swap last 3 bits...")
    print ("x = 7 = 0111 ==> 0000 = 0: " + str(new_x) )
    print ("y = 8 = 1000 ==> 1111 = 15 : " + str(new_y) )
    print ("\n\n\n")
    
    #
    # swap all 4 bits
    #
    # x = 7 = 0111 ==> 1000 = 8
    # y = 8 = 1000 ==> 0111 = 7 
    #
    new_x, new_y = solution.swap(x,y,4)
    
    print ("swap last 4 bits...")
    print ("x = 7 = 0111 ==> 1000 = 8: " + str(new_x) )
    print ("y = 8 = 1000 ==> 0111 = 7: " + str(new_y) )
    print ("\n\n\n")
    
    #
    # swap equal numbers ( n is any arbitrary value >= 1 )
    #
    x = 15
    y = 15
    new_x, new_y = solution.swap(x,y,1)
    print ("swap equal numbers...")
    print ("x = 15: " + str(new_x) )
    print ("y = 15: " + str(new_y) )
    print ("\n\n\n")
    
    
def main():
    
    solution = Solution()
    
    unit_test ( solution )
    
    
if __name__ == "__main__":
    main()