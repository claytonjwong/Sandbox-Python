"""

371. Sum of Two Integers


Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.


"""



class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
        if b == 0:
            return a
        
        return self.getSum( a ^ b , ( a & b ) << 1 )

#
# below code was my first iteration at this problem, from below info I found that
# there are two bitwise calculations performed, XOR and AND, carryover is performed only with AND,
# when both bits are set    
#
#         sum = 0
#         
#         #
#         # see if both a and b are negative
#         # if so, sum the positives, and then negate that sum
#         #
#         is_negative = False
#         
#         if ( a < 0 and b < 0 ):
#             a *= -1
#             b *= -1
#             is_negative = True
#         
#         #
#         # iterate through each bit position from 0 to 31 inclusive
#         # and perform bitwise operations to add a and b
#         #
#         for i in range(0, 32):
#             
#             bit = 1<<i
#             a_bit = a & bit
#             b_bit = b & bit
#             
#             #
#             # either a's bit is set XOR b's bit is set
#             #
#             if a_bit ^ b_bit:
#             
#                 #
#                 # carryover to next binary position,
#                 # since sum for this bit position is already set
#                 # from a previous carry over
#                 #
#                 if sum & bit:
#                     
#                     #
#                     # carry over by shifting left by 1
#                     #
#                     sum |= bit << 1
#                     
#                     #
#                     # unset the current bit
#                     #
#                     sum &= ( 0xFFFF ^ bit )
#                 
#                 #
#                 # no carry over, simply include this bit in the sum
#                 #
#                 else:
#                     sum |= bit
#             
#             #
#             # both a's bit AND b's bit are set
#             #
#             elif a_bit & b_bit:
#                 
#                 #
#                 # add by carryover to next binary position
#                 #
#                 # example: 2+2
#                 # 2 = 0010
#                 # 2 = 0010
#                 # 4 = 0100
#                 #
#                 sum |= bit << 1    
#         
#         
#         if ( is_negative ):
#             sum *= -1
#         
#         return sum       
            
    
def main():
    
    import pdb
    
    pdb.set_trace()
    
    solution = Solution()
    
    print ( "3 == " + str ( solution.getSum(1, 2) ))

    print ( "4 == " + str ( solution.getSum(2, 2) ))
    
    print ( "12 == " + str ( solution.getSum(6, 6) ))
    
    print ( "18 == " + str ( solution.getSum(6, 12) ))
    
    print ( "-4 == " + str ( solution.getSum(-2, -2) ))


if __name__ == "__main__":
    main()








