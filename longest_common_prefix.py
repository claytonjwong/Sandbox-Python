"""
Write a function to find the longest common prefix string amongst an array of strings.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        common_prefix = ""

        #
        # return None if strs is None
        #
        if ( strs == None ):
            return None


        
        #
        # find the smallest string in the array of strings
        #
        smallest = None
        
        for string in strs:
            if ( smallest == None ):
                smallest = string
            elif ( str == None ):
                return None
            elif ( len ( smallest ) > len ( string ) ):
                smallest = string

        #
        # iterate through the array of strings,
        # and add to the count if the characters
        # are equal to the smallest length string
        #
        i = 0
        
        while ( smallest and i < len ( smallest ) ):

            same = True
        
            #
            # ensure all strings in the array have the same character
            # as the smallest string
            #
            for string in strs:
            
                if ( string[i] != smallest[i] ):
                    same = False
                    break
            
            #
            # if all strings in this position are the same, 
            # then add this character onto the common prefix
            #
            # otherwise bail out
            #
            if ( same ):
                common_prefix = common_prefix + smallest[i]
            else:
                break
            
            #
            # move onto the next character position
            #
            i += 1
                    

        return common_prefix
        

    
        
        
    
def main():
    
    solution = Solution()
    
    str_arrays1 = [
        "howdy",
        "how",
        "hi", 
    ]

    
    print ( "h: " + solution.longestCommonPrefix(str_arrays1))
    
    str_arrays2 = [
        "howdy",
        "how",
        "how is that done", 
    ]
    
    print ( "how: " + solution.longestCommonPrefix(str_arrays2))


    str_arrays3 = [
        "",
        "how",
        "how is that done", 
    ]
    
    print ( "\"\": " + solution.longestCommonPrefix(str_arrays3))    
    
    
    
if __name__ == "__main__":
    main()
        
    