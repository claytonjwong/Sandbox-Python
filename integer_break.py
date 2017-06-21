"""

343. Integer Break


Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.



"""



class Solution(object):
    
    def integerBreak(self, num):
        """
        :type n: int
        :rtype: int
        """
        if num <= 2: # 1+1=2 and 1*1=1
            return 1
        
        elif num == 3: # 2+1=3 and 2*1=2
            return 2 
        
        elif num == 4: # 2+2=4 and 2*2=4
            return 4
        
        #
        # 5 is the first instance where the product of the sum of the halves is > num itself
        #
        else: # n >= 5
            
            #
            # subtract and multiply by 3 as many times as possible
            #
            product = 1
            
            while num >= 5:
                product *= 3
                num -= 3
        
        #
        # multiply product by the "leftovers" of num after removing as many 3s as possible
        #
        return num * product
    
    
def main():
    
    solution = Solution()
    
    print ("36 == " + str ( solution.integerBreak(10) ))
    
    print ("1 == " + str ( solution.integerBreak(2) ))
    
    print ("2 == " + str ( solution.integerBreak(3) ))
    
    print ("4 == " + str ( solution.integerBreak(4) ))
    
    print ("6 == " + str ( solution.integerBreak(5) ))
    
    print ("18 == " + str ( solution.integerBreak(8) ))
    

    
    print ("54 == " + str ( solution.integerBreak(11) ))

    
    print ("162 == " + str ( solution.integerBreak(14) ))
    

if __name__ == '__main__':
    main()







