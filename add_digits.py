"""

258. Add Digits

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.


"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        sum = 0
        
        while True:
            
            #
            # add up each decimal position from right-to-left
            #
            sum += num % 10
            num //= 10
            
            #
            # when there are no decimal positions left,
            # see if the sum is greater than a single decimal digit
            # if so, then reset num to sum and reset sum to 0
            #
            # return sum when there are no decimal positions left
            # and sum is a single decimal digit
            #
            if num == 0 and sum >= 10:
                num = sum
                sum = 0
            elif num == 0 and sum < 10:
                break
            
        return sum
    
def main():
    
    solution = Solution()

#     import pdb
#     pdb.set_trace()
    
    print ( str ( " 2 == " + str ( solution.addDigits(38) )) )


if __name__ == "__main__":
    main()







