"""

415. Add Strings


Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.


"""

import math

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        sum = ""
        
        #
        # left fill each string with 0's so that each string is the same length
        #
        max_len = max ( len(num1), len(num2) )
        
        num1 = num1.rjust(max_len, '0')
        num2 = num2.rjust(max_len, '0')
        
        #
        # iterate from right to left and add each digit together
        #
        carryover = False
        i = max_len - 1
        while i >= 0:
            
            #
            # add current digits together and include carryover if it exists
            #
            int1 = self.str_to_int( num1[i] )
            int2 = self.str_to_int( num2[i] )
            
            digit_sum = int1 + int2
            
            if carryover:
                digit_sum += 1
            
            #
            # check for carryover
            #
            carryover = False
            if digit_sum >= 10:
                carryover = True
                digit_sum %= 10
            
            #
            # multiply by the dec_pos and
            # include this digit sum in the total sum
            #
            sum = str ( digit_sum ) + sum
            
            #
            # prepare for next iteration
            #
            digit_sum = 0
            i -= 1
            
        if carryover:
            sum = "1" + sum
        
        return sum
    
    
    def str_to_int(self, s):
        if s == '0':
            return 0
        elif s == '1':
            return 1
        elif s == '2':
            return 2
        elif s == '3':
            return 3
        elif s == '4':
            return 4
        elif s == '5':
            return 5
        elif s == '6':
            return 6
        elif s == '7':
            return 7
        elif s == '8':
            return 8
        elif s == '9':
            return 9
    
def main():
    
    import pdb
    
    solution = Solution()
    
    
    print ( "0 == " + str ( solution.addStrings("0","0")))
    
    
    print ( "10 == " + str ( solution.addStrings("1", "9")))
    
    print ( "1000 == " + str ( solution.addStrings("1", "999")))
    
    pdb.set_trace()
    print ( "198 == " + str ( solution.addStrings("99", "99")))
    
    print ( "101 == " + str ( solution.addStrings("100", "1")))


if __name__ == "__main__":
    main()







