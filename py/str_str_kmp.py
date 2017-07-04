"""

28. Implement strStr()

Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


"""

#
# 
#

class Solution(object):
    
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        #
        # we will never find the needle in the haystack
        # is the needle or haystack do NOT exist
        #
        if haystack == None or needle == None:
            return -1
        
        #
        # KMP algo
        #
        # ( https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm )
        #
        # generate next (nx) array, need O(n) time
        #
        i, k, len_haystack, len_needle = -1, 0, len(haystack), len(needle)
        nx = [-1] * len_needle
        while k < len_needle - 1:  
            #
            # needle[i] stands for prefix, neelde[k] stands for postfix
            #
            if i == -1 or needle[i] == needle[k]:   
                i, k = i + 1, k + 1
                
                #
                # ???
                #
                # the letters are the same, or we have started back at -1
                # if the letters are the same, then i is incremented by 1 for each same letter
                # this allows us to "skip" forward this many positions in the next future search
                # in case the current search fails at some point
                #
                # we start back at -1 when the letters are different, when the letters are different,
                # then there is no "skipping" forward
                #
                nx[k] = i
                
            else:
                
                #
                #
                #
                i = nx[i]
                
                if i != -1:
                    import pdb
                    pdb.set_trace()
                
            print (i,k,nx[i],nx[k])
            
            
        import pdb
        pdb.set_trace()
        #
        # check through the haystack using next, need O(m) time
        #
        i = k = 0
        while i < len_haystack and k < len_needle:
            
            if k == -1 or haystack[i] == needle[k]:
                i, k = i + 1, k + 1
                
            else:
                k = nx[k]
                
        if k == len_needle:
            return i - k
        
        return -1
    
def main():
    
    solution = Solution()

    """
    
    haystack
    
    0123456789
    ABCABCABCD
    
    ik 
    0123
    ABCD
    
    needle
    
    """
    
    print ("8 == " + str ( solution.strStr("AAACAAABAAAD", "AAAD") ))
    
if __name__ == "__main__":
    main()
    
    
    
    
    
    