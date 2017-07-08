"""

405. Convert a Number to Hexadecimal

Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.
Example 1:

Input:
26

Output:
"1a"
Example 2:

Input:
-1

Output:
"ffffffff"


"""



class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ""
        
        #
        # perform 8 iterations, one itr per nibble of the 32-bit int
        #
        i = 8
        while i > 0:
            
            nibble = num & 0xF
            
            if nibble < 0xA:
                
                #
                # nibble is 0-9, simple pre-pend it here
                #
                result = str( nibble ) + result
                
            else:
                
                #
                # nibble is 10-15, map to corresponding char and convert based on int value
                #
                # 87 + 10 = 'a'
                # 87 + 11 = 'b'
                # 87 + 12 = 'c'
                # 87 + 13 = 'd'
                # 87 + 14 = 'e'
                # 87 + 15 = 'f'
                #
                result = chr( 87 + nibble ) + result
                
            #
            # right-shift to drop the right-most nibble
            #
            num >>= 4
            i -= 1
            
        result = result.lstrip("0")
        
        return result if len(result) > 0 else "0"
    
def main():
    
    solution = Solution()
    
#     import pdb
#     pdb.set_trace()
    
    print ( "ffffffff == " + str ( solution.toHex(-1) ))
    
    print ( "400 == " + str ( solution.toHex(1024) ))
    
if __name__ == '__main__':
    main()










