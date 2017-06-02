"""

205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.

"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        len_str = len ( s )
        mapping_s_to_t = {}
        mapping_t_to_s = {}
        
        if ( len_str != len ( t ) ):
            return False
        
        i=0
        while ( i < len_str ):
            
            #
            # lookup the mapping between the character from s and t
            #
            # if the mapping does NOT exist, then KerError is throw, so add the mapping
            #
            # if the mapping exists, then ensure the key-value pair match for the current chars,
            # if they do NOT match, then return False
            #
            try:
                if ( mapping_s_to_t[ s[i] ] != t[i] ):
                    return False
            except KeyError:
                mapping_s_to_t[ s[i] ] = t[i]

            try:
                if ( mapping_t_to_s[ t[i] ] != s[i] ):
                    return False
            except KeyError:
                mapping_t_to_s[ t[i] ] = s[i]
                
            i += 1
    
        return True
    
def main():
    
    solution = Solution()
    print ( "True == " + str ( solution.isIsomorphic("paper", "title")))
    print ( "False == " + str ( solution.isIsomorphic("ab", "aa")))

if __name__ == "__main__":
    main()
    
    