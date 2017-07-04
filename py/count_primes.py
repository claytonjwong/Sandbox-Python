"""

204. Count Primes

Description:

Count the number of prime numbers less than a non-negative number, n.

"""
 
import math
 
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        #
        # 2 is prime, however, this function is NOT include n, this function
        # returns the amount of primes from (0 to n-1) inclusive
        #
        if ( n <= 2 ):
            return 0
         
        #
        # assume n > 2, 
        #
        # using the sieve of eratosthenes:
        #
        # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
        #
        # pp is a bool list whose index represents each integer, which will be used to track
        # "potential primes".  Each time an integer is found to NOT be prime,
        # set it to false, per the sieve of eratostshenes
        #
        # track from ( 2 to sqrt(n) inclusive ),
        # set 0,1 to False initially, since these are NOT prime
        #
        pp = [True] * n
        pp[0] = pp[1] = False
         
        sqrt_n = int(math.sqrt(n))
         
        #
        # iterate from ( 2 to sqrt(n) inclusive )
        #
        for i in range ( 2, sqrt_n+1 ):
             
            #
            # if this number is NOT prime, then move onto the next number
            #
            if ( pp[i] == False ):
                continue
             
            #
            # this number is prime, so use the sieve of eratosthenes
            # to set all derviates of this prime number as False ( NOT prime )
            #
            i_squared = i * i
            j = 0
            non_prime_index = i_squared # + (j*i) -- since j is 0, we can skip this calculation
            while non_prime_index < n:
                 
                #
                # this is a key part of the sieve of eratostshenes, take for example 2 with list 2..10
                # 2 is prime and is set to True, so all derivates of 2 ( 4, 6, 8, 10 ) are set to non-prime
                # by calculating the index as i^2 + j*i
                #
                # for example the first iteration is performed with value i=2:
                #
                # 2, 3, 4, 5, 6, 7, 8, 9, 10
                #
                #
                # i^2 + 0*2 = 4 ... so 4 is NOT prime
                #
                # i^2 + 1*2 = 6 ... so 6 is NOT prime
                #
                # i^2 + 2*2 = 8 ... so 8 is NOT prime
                #
                # i^2 + 3*2 = 10 ... so 10 is NOT prime
                #
                 
                #
                # set this index as NOT prime
                #
                pp[non_prime_index] = False
                 
                #
                # iterate by adding the value of i
                #
                j += 1
                non_prime_index = i_squared + (j * i)
                 
                 
        count = 0
         
        for prime in pp:
            if prime:
                count += 1    

        return count


def main():
    solution = Solution()
    
    import pdb
    pdb.set_trace()
    
    primes = solution.countPrimes(5)


if __name__ == "__main__":
    main()




