"""

434. Number of Segments in a String

Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5


"""


class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None:
            return 0
            
        return len ( s.split() )
    
    
def main():
    solution = Solution()
    print ( "5 == " + str ( solution.countSegments("Hello, my name is John")))
    
if __name__ == "__main__":
    main()
    
    
    
    