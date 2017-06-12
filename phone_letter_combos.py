"""

17. Letter Combinations of a Phone Number

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.

"""

 
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        
        combos = [""]
         
        dic = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz" }

          
        #
        # iterate through each digit
        #
        for digit in digits:
             
            #
            # keep track of new combinations based on previous combinations
            #
            new_combos = []
              
            #
            # iterate through each letter of the digit
            #
            for letter in dic[digit]:
                 
                #
                # append this letter onto each of the previous letter combinations
                #
                for prev_letters in combos:
                     
                    new_combos.append( prev_letters + letter )
                 
            #
            # save these letter combos so far, in prepraration
            # for appending the next letter onto these previous letters
            #
            combos = new_combos
             
        return combos
        
                
    
def main():
    
    import pdb
    
    pdb.set_trace()
    
    solution = Solution()
    solution.letterCombinations("23")


if __name__ == "__main__":
    main()









