"""

419. Battleships in a Board

Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:

You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
Example:
X..X
...X
...X
In the above board there are 2 battleships.
Invalid Example:
...X
XXXX
...X
This is an invalid board that you will not receive - as battleships will always have a cell separating between them.
Follow up:
Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?

"""


class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        
        #
        # ship count
        #
        ship_count = 0
        
        #
        # prev_row is used to see if there are any ship pieces above the current position
        # this is needed in order to check if the current piece is part of an already counted ship or
        # if the current piece is part of a new ship
        #
        prev_row = None
        
        #
        # go through each row and each character in the row
        # if there is no ship piece to the left or above
        # then this is a unique ship, increment count by 1
        #
        for row, row_val in enumerate ( board ):
            
            #
            # go through each char in the string
            #
            for col, chr in enumerate ( row_val ):
                
                #
                # check for a ship piece
                #
                if chr == "X":
                     
                    #
                    # check for ship piece to the left
                    #
                    same_ship = True if col>0 and row_val[col-1]=="X" else False
                     
                    #
                    # check for ship piece above and OR result with the above check for ship to the left
                    #
                    same_ship |= True if prev_row is not None and prev_row[col]=="X" else False
                     
                    #
                    # increment ship count if there is no ship piece to the left or above
                    # since this is a unique ship ( not part of the same ship which was already counted )
                    #
                    if not same_ship:
                         
                        ship_count += 1
    
            #
            # store the previous row in order to check for the same ship above the current row
            #
            prev_row = row_val
            
    
        return ship_count
    
def main():
    
    import pdb
    
    solution = Solution()
    
    # X..X
    # ...X
    # ...X
    
    board = ["X..X","...X","...X"]
    
#     pdb.set_trace()
    print ("2 == " + str ( solution.countBattleships(board) ))


if __name__ == '__main__':
    main()






