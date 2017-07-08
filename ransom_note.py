"""

383. Ransom Note

Given an arbitrary ransom note string and another string containing letters from all the magazines,
write a function that will return true if the ransom note can be constructed from the magazines ;
otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

"""



class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        len_rn = len ( ransomNote )
        len_mag = len ( magazine )
        
        #
        # the length of the magazine must be larger than the length of the note
        #
        if len_rn > len_mag:
            return False
        
        #
        # go through each char in the ransom note, and ensure that the count of each char
        # in the ransom note is less than the count of each char in the magazine
        #
        for ch in ransomNote:
            if ransomNote.count(ch) > magazine.count(ch):
                return False
                    
        return True
    
def main():
    
    solution = Solution()
    
    print ( "False == " + str ( solution.canConstruct("aabb", "aab") ) )
    
    print ( "True == " + str ( solution.canConstruct("aa", "aab") ) )
    
    
    
    
if __name__ == "__main__":
    main()
    
    
    