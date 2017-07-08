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
        
        #
        # if input is invalid, then return an empty list
        #
        if str_to_check is None or chars_to_mix_up is None:
            return []
        
        len_str_to_check = len ( str_to_check )
        len_chars_to_mix_up = len ( chars_to_mix_up )
        
        #
        # no anagram is possible if the amount of potential characters
        # used in the string to check is less than the anagram itself
        #
        if len_str_to_check < len_chars_to_mix_up:
            return []
        
        #
        # hash to store count of chars up to ord('z') = 122
        #
        hash_str_to_check = [0] * 123
        hash_chars_to_mix_up = [0] * 123
        
        #
        # fill up hash which a potential anagram would need to match
        #
        for ch in chars_to_mix_up:
            hash_chars_to_mix_up[ord(ch)] += 1
            
        #
        # fill up hash for the string to check from 0 to len ( chars to mix up - 2 ) inclusive
        #
        for ch in str_to_check[:len_chars_to_mix_up - 1 ]:
            hash_str_to_check[ord(ch)] += 1
        
        #
        # iterate through the string to check for anagarams, start at len ( chars to mix up - 1 )
        #
        for i in range ( len_chars_to_mix_up - 1, len_str_to_check ):

            #
            # add curr
            #
            curr = str_to_check[i]

            hash_str_to_check [ ord(curr) ] += 1
            
            #
            # remove prev
            #
            if i - len_chars_to_mix_up >= 0:
                
                prev = str_to_check [ i - len_chars_to_mix_up ]
                
                hash_str_to_check [ ord(prev) ] -= 1

            #
            # append the beginning anagram index if found
            #            
            if hash_str_to_check == hash_chars_to_mix_up:
                anagram_index_list.append( i - len_chars_to_mix_up + 1 )
   
        #
        # return list of start indices for the anagram(s) found 
        #
        return anagram_index_list

                
    
def main():
    
     
    solution = Solution()
    
    print ("[0, 6] == " + str ( solution.findAnagrams("cbaebabacd", "abc") ))


if __name__ == "__main__":
    main()
















