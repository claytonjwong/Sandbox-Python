class Solution(object):
    def longestPrefix(self, s):
        """
        :type s: str
        :rtype: int
        """
            
        if s is None or len(s)==0:
            return 0
        
        curr=0
        for i,ch in enumerate(s):
            if ord(ch) < curr:
                return i
            
            curr=ord(ch)
    
        return len(s)
    
def main():
    
    solution = Solution()
    
    print ( "0 == " + str ( solution.longestPrefix(None) ))
    print ( "0 == " + str ( solution.longestPrefix("") ))
    
    print ( "6 == " + str ( solution.longestPrefix("knotty") ))
    print ( "3 == " + str ( solution.longestPrefix("apple") ))
    print ( "2 == " + str ( solution.longestPrefix("excel") ))
    
    
if __name__ == '__main__':
    main()