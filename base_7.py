"""

504. Base 7

Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].


"""



class Solution(object):
    
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        #
        # mapping between int index and char value
        #
        # ex: strmap[0] = "0"
        #
        strmap = "0123456"
        
        base = 7

        #
        # base case, simply return the number as a string
        #
        if abs(num) < base:
            return "-" + strmap[abs(num)] if num < 0 else strmap[num]
        
        #
        # recursive case
        #
        # num//base is used to right-shift num by one base position such
        # that the right-most digit "falls off", the part which "falls off" is the remainder
        # ( ex: base 10, if num is 1234, then 1234/10 = 123 with remainder 4
        # 
        # the remainder is the value to be placed in the right-most position
        # of the string to be returned, look it up in the int to str mapping
        #
        rshifted_num = -1 * (abs(num)//base) if num < 0 else (num//base)
        remainder = abs(num) % base
        
        return self.convertToBase7( rshifted_num ) + strmap[ remainder ]
        
    
    
def main():
    
    solution = Solution()
    
#     import pdb
#     pdb.set_trace()
    
    print ( "-11 == " + str ( solution.convertToBase7(-8) ))
            
if __name__ == '__main__':
    main()





