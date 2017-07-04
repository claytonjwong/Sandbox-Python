"""
 
36. Valid Sudoku
 
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules (http://sudoku.com.au/TheRules.aspx)
 
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
 
"""
 
class Solution(object):
        
    def isValidSudoku(self, board):
        seen = sum(([(c, i), (j, c), (i/3, j/3, c)]
                    for i, row in enumerate(board)
                    for j, c in enumerate(row)
                    if c != '.'), [])
        return len(seen) == len(set(seen))
    
    
    
#     def isValidSudoku(self, board):
#         """
#         :type board: List[List[str]]
#         :rtype: bool
#         """
#          
#         col = []
#          
#         #
#         # ensure each row contains unique numbers
#         #
#         for i, row in enumerate(board):
#              
#             #
#             # size is used to check for the row uniqueness
#             #
#             size = 0
# 
#             for k, ch in enumerate(row):
#                  
#                 #
#                 # create new lists for each column, and add non-empty spaces
#                 # 
#                 if k == len(col):
#                     col.append([])
#                   
#                 #
#                 # increment the size for non-empty spaces
#                 # and include them in the column list
#                 #
#                 if ch != '.':
#                     col[k].append(ch)
#                     size += 1
# 
#             #
#             # ensure the row is unique
#             #   
#             if '.' in row:
#                 row = row.replace('.', '')
#          
#             if size != len(set(row)):
#                 return False
#         
#         #
#         # ensure each column is unique
#         #
#         for c in col:
#             
#             if len(c) != len(set(c)):
#                 return False
# 
#         
#         return True

         
def main():
     
    solution = Solution() 
     
    board = [
        "012",
        "123",
        "234",
        ]
     
    import pdb
    pdb.set_trace()
    print("False == " + str ( solution.isValidSudoku(board) ))
     
     
     
if __name__ == '__main__':
    main()

