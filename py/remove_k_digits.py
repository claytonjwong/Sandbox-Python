"""

402. Remove K Digits

https://leetcode.com/problems/remove-k-digits/


Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

"""



class Solution(object):
    
    def removeKdigits(self, num, k):
        
        result = self.removeKdigitsHelper(num, k)
        
        if result is None:
            return "0"
        else:
            result = result.lstrip("0")
        
        return "0" if result=="" else result
    
    
    def removeKdigitsHelper(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
                
        #
        # do NOT remove anything, recursive base case
        #
        if k == 0:
            return num
        
        #
        # remove all digits, and up with with "0"
        #
        elif k >= len(num):
            return ""
        
        #
        # iterate through num and remove k digits
        #
        while k > 0:
    
            found_largest = False
    
            #
            # find and remove the largest left-most digit
            #
            i = 0
            while i < len(num) - 1:
                
                #
                # if the digit to the left is larger than
                # the digit to the right,
                #
                # then remove the larger digit to the left here
                #
                if num[i] > num[i+1]:
                    
                    #
                    # remove digit at index i
                    #
                    if i == 0:
                        num = num[1:]
                    else:
                        num = num[0:i] + num[i+1:]
                    
                    #
                    # since we have removed the largest digit, we can exit the inner loop here
                    #
                    found_largest = True
                    break
                
                #
                # check next i for the largerst left-most digit
                #
                i += 1
                
            #
            # we did NOT find a largest left-most digit to remove,
            # so remove the right-most digit here, since it is the largest
            #
            # [note: this occurs for nums in incremental order (ex: 1234), so remove 4 to make 123]
            #
            if not found_largest:
                
                num = num[:-1]
            
            #
            # decrement k by 1 and iterate
            #    
            k -= 1
            
        #
        # return num with k digits removed
        #
        return num

    
def main():
    
    solution = Solution()
    
    

    
    print ( "1219 == " + str ( solution.removeKdigits("1432219", 3) ))
    

    
    print ( "11 == " + str ( solution.removeKdigits("112", 1) ))

#     import pdb
#     pdb.set_trace()
    
    print ( "31 == " + str ( solution.removeKdigits("331", 1) ))
    

    
    print ( "0 == " + str ( solution.removeKdigits("1001", 2) ))
    
    print ( "0 == " + str ( solution.removeKdigits("1001", 4) ))
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    














