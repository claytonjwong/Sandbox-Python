

import math
from collections import Counter

class Solution(object):
    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        if a < 10:
            return a
        
        smallest = math.pow(2,31)
        
        #
        # find all factors and insert into a list,
        # where the index is n and the value is m
        # and n * m = a,
        #
        # use 0 for invalid values
        #
        fact = []
        fact.append(0)
        
        for i in range(1,int(a//4)+2):
            
            if a % i == 0 and int(a//i) != a:
                fact.append(int(a//i))
            else:
                fact.append(0)
        

        
        for i,v in enumerate(fact):
            
            #
            # invalid value
            #
            if i * v == 0:
                continue
            
            #
            # add i onto the front of fact[i], and set to smallest if applicable
            #
            dec_pos = int( math.pow(10,len(str(v))) )
            
            smallest = min ( smallest, i * dec_pos + v )
        
        
        #
        # coalesce 1111 into 1
        #
        if smallest == math.pow(2,31):
            return 0
        
        return smallest % 10 if len( Counter(str(smallest)) )==1 else smallest
        
def main():
    
    solution = Solution()
    
    
    print ( "68 == " + str  (solution.smallestFactorization(48) ))
    
    print ( "35 == " + str  (solution.smallestFactorization(15) ))
    
    
    print ( "1 == " + str  (solution.smallestFactorization(1) ))
    
    print ( "2 == " + str  (solution.smallestFactorization(2) ))
    
    print ( "3 == " + str  (solution.smallestFactorization(3) ))
    
    print ( "0 == " + str  (solution.smallestFactorization(11) ))
    
    
if __name__ == '__main__':
    main()    
    