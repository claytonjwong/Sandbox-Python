"""

"""

class Solution(object):
    def reverseVowels(self, str):
        """
        :type s: str
        :rtype: str
        """
        
        #
        # in python, strings are immutable, so ns is the new string
        # which will be contructed and returned
        #
        ns = ""
        
        queue = []
        
        vset = set("aeiouAEIOU")
        
        #
        # iterate through str and add vowels onto queue
        #
        for ch in str:
            
            if ch in vset:
                
                queue.append(ch)
                
        #
        # iterate through s and construct ns
        # pop off the q whenever there is vowel found
        # in order to reverse the order of vowels
        # non-vowels are simply appended to this string
        #
        for ch in str:
            
            #
            # vowel
            #
            if ch in vset:
                
                ns += queue.pop()
            
            #
            # non-vowel
            #
            else:
                
                ns += ch
        
        
        return ns
    

def main():
    
    
    solution = Solution()
    print ( "holle == " + str ( solution.reverseVowels("hello") ))


if __name__ == "__main__":
    main()


    
    
