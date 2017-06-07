"""

290. Word Pattern

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.


"""


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if len(pattern) == 0 or len(str) == 0:
            return False
        
        #
        # insert mappings from pattern to str in a dic
        # to ensure uniaueness
        #
        dic_pw = {}
        dic_wp = {}
        list = str.split()
        
        #
        # go through each character in the pattern
        #
        for c in pattern:
            
            #
            # pop the first word from the list,
            #
            # if it exists in the dic, ensure it matches the corresponding pattern-key
            # otherwise, add it to the dic
            #
            if len ( list ) == 0:
                return False
            
            word = list.pop(0)
            
            #
            # pattern to word
            #
            if c in dic_pw:
                if dic_pw[c] != word:
                    return False
            else:
                dic_pw[c] = word
            
            #
            # word to pattern
            #
            if word in dic_wp:
                if dic_wp[word] != c:
                    return False
            else:
                dic_wp[word] = c
            
        #
        # if the pattern matches, then the list should be exhausted and len is 0
        # otherwise if there are more words remaining in list, then there is no match
        #
        return len ( list ) == 0 
    
    
    
def main():
    
    solution = Solution()
    
    print ( "True == " + str ( solution.wordPattern("abba", "dog cat cat dog") ) )

if __name__ == "__main__":
    main()
    
    
    





