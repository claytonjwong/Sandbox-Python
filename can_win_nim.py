"""

292. Nim Game

You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.


"""

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #
        # 4 stones left is the first instance where
        # you will never win regardless how many stones are picked up
        # as long as your opponent plays optimally
        #
        # with 8 stones left, you can choose 1, 2, or 3 stones, regardless,
        # again, your optimal opponent can force you to have 4 stones left
        #
        # etc, etc...
        #
        return n % 4 != 0

    
    
def main():
    pass


if __name__ == "__main__":
    main()





