"""
Write a function to find the longest common prefix string amongst an array of strings.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
 
        # find the longest common prefix of these concantentated strings
        tuple_of_strings = zip(*strs)
        for i,tuple_column in enumerate(tuple_of_strings):
            if len( set(tuple_column) ) != 1:
                return strs[0][0:i]
        
        # if we get here, then all strings so far are equal
        # return the smallest length string, since we ran out of string
        return min(strs) if strs else ''
    
        
        
    
def main():
    
    solution = Solution()
    

    
    str_arrays1 = [
        "howdy",
        "how",
        "h", 
    ]

    
    print ( "h: " + str(solution.longestCommonPrefix(str_arrays1)) + "\n\n");
    
    str_arrays2 = [
        "howdy",
        "how",
        "how is that done", 
    ]
    
    print ( "how: " + str(solution.longestCommonPrefix(str_arrays2)) + "\n\n");


    str_arrays3 = [
        "",
        "how",
        "how is that done", 
    ]
    
#     import pdb
#     pdb.set_trace()
    
    print ( "'': '" + str(solution.longestCommonPrefix(str_arrays3)) + "'\n\n");
    
    
    
if __name__ == "__main__":
    main()
        
    