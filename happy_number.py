"""

202. Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1


"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prev_dict = {}
        
        while ( True ):
            
            #
            # happy numbers will turn into 1 eventually
            #
            if ( n == 1 ):
                return True
            
            #
            # un-happy numbers will wrap-around, so keep track
            # of all previous calculations by adding them
            # into a dictionary, when a duplicate entry is found, return False
            #
            # this dictionary lookup will throw KeyError if the entry does NOT exist
            # for this exception, add the entry n onto the dictionary
            #
            try:
                if ( prev_dict[n] ):
                    return False
                
            except KeyError:
                prev_dict[n] = True
    
            #
            # get the next n
            #
            n = self.nextN(n)
            
    
    def nextN(self, n):
        """
        :type n: int
        :rtype: int
        """
    
        #
        # calculate the next value of n by squaring and adding up
        # the sum of each decimal position value
        #
        sum_of_each_dec_pos_val_squared = 0
        dec_pos_val = 0
        while ( n > 0 ):
            
            #
            # right-most decimal position value
            #
            dec_pos_val = n % 10
            
            #
            # sum the square of this decimal position
            #
            sum_of_each_dec_pos_val_squared += ( dec_pos_val * dec_pos_val )
            
            #
            # remove right-most decimal position
            #
            n = int ( n / 10 )
            
        return sum_of_each_dec_pos_val_squared
    
    
def main():
    solution = Solution()
    
    import pdb
    pdb.set_trace()
    
    print ( "False == " + str ( solution.isHappy(2)))


if __name__ == "__main__":
    main()
    
    
    
