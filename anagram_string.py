"""

438. Find All Anagrams in a String


Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".


"""

class Solution(object):
    def findAnagrams(self, str_to_check, chars_to_mix_up):
        """
        :type str_to_check: str
        :type chars_to_mix_up: str
        :rtype: List[int]
        """
        anagram_index_list = []
        
        if str_to_check is None or chars_to_mix_up is None:
            return []
        
        len_str_to_check = len ( str_to_check )
        len_chars_to_mix_up = len ( chars_to_mix_up )
        
        if len_str_to_check < len_chars_to_mix_up:
            return []
        
        i = 0
        while i <= len_str_to_check - len_chars_to_mix_up:
            
            #
            # slide from right to left and check for anagrams
            #
            curr_substr = str_to_check[i:i+len_chars_to_mix_up]
            
            if self.isAnagram( curr_substr, chars_to_mix_up ):
                anagram_index_list.append(i)
            
            i += 1
            
        return anagram_index_list
    
        
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        #
        # invalid anagram if the length of the two strings are NOT equal
        #
        len_str = len ( s )
        
        if len_str != len (t):
            return False
        
        #
        # start with a hash from a-z
        # increment count for each instance of each letter found in s
        # decrement count for each instance of each letter found in t
        #
        q = {}
        for i in range ( ord('a'), ord('z') + 1 ):
            q [ i ] = 0
        
        for ch in s:
            q [ ord(ch) ] += 1
    
        for ch in t:
            try:
                q [ ord(ch) ] -= 1
            except KeyError:
                return False
    
        for i in range ( ord('a'), ord('z') + 1 ):
            if q [ i ] != 0:
                return False
    
        return True
                
    
def main():
    
    solution = Solution()
    
    print ("[0, 1, 2] == " + str ( solution.findAnagrams("abab", "ab") ))


if __name__ == "__main__":
    main()
















