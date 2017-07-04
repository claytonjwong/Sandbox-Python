"""

345. Reverse Vowels of a String

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".


"""

import re

class Solution(object):
        
    def __init__(self):
        #
        # this list is used to keep track of all vowels in a string to be reversed
        #
        self.vowels = []
    
    def reverseVowels(self, str):
        """
        :type s: str
        :rtype: str
        """
        
        #
        # all vowels, only lowercase is needed, since our regex will use the flag to IGNORECASE
        #
        vset = "[aeiou]"
        
        #
        # find all vowels in the string
        #
        self.vowels = re.findall(vset, str, flags=re.IGNORECASE)
        
        #
        # replace vowels in reverse order, the re.sub function will invoke self.replaceVowel()
        # whenever a vowel is found, and self.replaceVowel() pops off the vowels previously found
        # in reverse order
        #
        return re.sub(vset, self.replaceVowel, str, flags=re.IGNORECASE)
        

    def replaceVowel(self, matchobj):
        """
        :type matchobj: re matchobj
        """

        return self.vowels.pop()


def main():

    
    solution = Solution()
    print ( "holle == " + str ( solution.reverseVowels("hello") ))


if __name__ == "__main__":
    main()


    
    
