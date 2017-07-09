"""

640. Solve the Equation

https://leetcode.com/contest/leetcode-weekly-contest-40/problems/solve-the-equation/

Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:
Input: "x+5-3+x=6+x-2"
Output: "x=2"
Example 2:
Input: "x=x"
Output: "Infinite solutions"
Example 3:
Input: "2x=x"
Output: "x=0"
Example 4:
Input: "2x+3x-6x=x+2"
Output: "x=-1"
Example 5:
Input: "x=x+2"
Output: "No solution"


"""


class Solution(object):
    
    def solveEquationHelper(self, equation):
        
        cw = ""
        
        x_cnt = 0
        n_cnt = 0

        neg_num = False
    
        for ch in equation:
            
            if ch == '-':
                
                if len(cw):
                    
                    if neg_num:
                        n_cnt -= int(cw)
                    else:
                        n_cnt += int(cw)
                        
                    cw = ""
                        
                neg_num = True
                
            if ord(ch) in range(ord('0'),ord('9')+1):
                cw += ch
                
            if ch == 'x':
                
                if len(cw) > 0:
                    
                    if neg_num:
                        x_cnt -= int(cw[0:len(cw)])
                    else:
                        x_cnt += int(cw[0:len(cw)])
                
                else:
                    
                    if neg_num:
                        x_cnt -= 1
                    else:
                        x_cnt += 1
                    
                cw = ""
                neg_num = False
            
            if ch == "+":
                
                if len(cw) > 0:
                    
                    if neg_num:
                        n_cnt -= int(cw)
                    else:
                        n_cnt += int(cw)
            
                cw = ""
                neg_num = False
                
        if len(cw) > 0:
            if neg_num:
                n_cnt -= int(cw)
            else:
                n_cnt += int(cw)
        
        return [x_cnt, n_cnt]
    
    
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        leq, req = equation.split("=")
        
#         import pdb
#         pdb.set_trace()
        
        left_x, left_n = self.solveEquationHelper(leq)
        right_x, right_n = self.solveEquationHelper(req)
        
        if left_x > right_x:
            
            x_cnt = left_x - right_x
            n_cnt = right_n - left_n
            
        else:
            
            x_cnt = right_x - left_x
            n_cnt = left_n - right_n
            




        
        if x_cnt == 0 and n_cnt == 0:
            return "Infinite solutions"
        
        # ax = 0, regardless of a, x=0 for this eq to be true always
        if n_cnt == 0:
            return "x=0"
        
        if x_cnt == 0 and n_cnt != 0:
            return "No solution"

        if n_cnt % x_cnt == 0:
            
            result = "x="
            
            if x_cnt < 0:
                result += "-"
            
            result += str(n_cnt//x_cnt) 
            
            return result
            
        return "No solution"
    
    
def main():
    
    solution = Solution()
    
    print ( str (solution.solveEquation("x+5-3+x=6+x-2") ))
    
if __name__ == '__main__':
    main()
        