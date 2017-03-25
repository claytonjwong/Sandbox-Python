"""

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "" and ()" and "()[]{}" and "[({})]" are all valid but "(]" and "([)]" are not.

"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        #
        # iterate through each character in the string
        #
        for c in s:
            
            #
            # see if this character is in the open bracket group
            #
            if ( c in [
                "(",
                "{",
                "[",
                ]
            ):
                #
                # push the expected corresponding close bracket
                # later this will be popped and expected to match
                #
                if ( c == "(" ):
                    stack.append(")")
                    
                elif ( c == "{" ):
                    stack.append("}")
                    
                elif ( c == "[" ):
                    stack.append("]")
            
            #
            # see if this character is in the close bracket group
            #
            elif ( c in [
                ")",
                "}",
                "]",
                ]
            ):
                #
                # if the stack is empty, then there is no matching bracket, return False
                #
                if ( len ( stack ) == 0 ):
                    return False
                #
                # if the close bracket does NOT match with the open bracket, return False
                #
                elif ( c != stack.pop() ):
                    return False
            #
            # if the character is NOT an open or close bracket, then return False
            #
            else:
                return False
        
        #
        # if all items which were pushed onto the stack were popped off the stack, then
        # the stack should be empty, return True, otherwise, return False
        #
        if ( len ( stack ) == 0 ):
            return True
        else:
            return False

def main():
    solution = Solution()
    
    print ( "True: " + str ( solution.isValid("()") ) )
    print ( "False: " + str ( solution.isValid("(") ) )
    print ( "False: " + str ( solution.isValid(")") ) )
    print ( "False: " + str ( solution.isValid(")") ) )
    print ( "True: " + str ( solution.isValid("") ) )
    print ( "False: " + str ( solution.isValid("(()") ) )
    print ( "False: " + str ( solution.isValid("())") ) )
    print ( "True: " + str ( solution.isValid("{({[(({}))]})}") ) )
        
if __name__ == "__main__":
    main()