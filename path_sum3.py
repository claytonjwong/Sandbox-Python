"""

437. Path Sum III


You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11


"""



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0

        #
        # First invoke:
        #
        #    + self.pathSumHelper(root.left, sum - root.val) \
        #    + self.pathSumHelper(root.right, sum - root.val) \
        #
        # in order to count all path sums equal to sum beginning
        # with this root node INCLUDED in the sum count
        #
        #
        # Second invoke:
        #
        #    + self.pathSum(root.left, sum ) \
        #    + self.pathSum(root.right, sum ) \
        #
        # in order to "start over" with a new sub-tree
        # NOT including root node in the sum count
        #
        return ( 1 if root.val == sum else 0 ) \
            + self.pathSumHelper(root.left, sum - root.val) \
            + self.pathSumHelper(root.right, sum - root.val) \
            + self.pathSum(root.left, sum ) \
            + self.pathSum(root.right, sum ) \

    
    
    def pathSumHelper(self, node, sum):
        """
        :type node: TreeNode
        :type curr_sum: int
        :type target_sum: int
        :rtype: int
        """
        if node is None:
            return 0
        
        #
        # go through each node of this sub-tree, and see if there
        # are any paths which add up to sum
        #
        return ( 1 if node.val == sum else 0 ) \
            + self.pathSumHelper(node.left, sum - node.val) \
            + self.pathSumHelper(node.right, sum - node.val)
        
    
    
def main():
    
    import pdb


    solution = Solution()
    
    root = TreeNode(8)
    
    print ( "1 == " + str ( solution.pathSum(root, 8) ))


    root.left = TreeNode(8)
    
    print ( "2 == " + str( solution.pathSum(root, 8)))

#
# [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
    
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(-3)
    
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    
    root.right.right = TreeNode(11)
    
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-2)
    
    root.left.right.right = TreeNode(1)
    
    print ( "3 == " + str( solution.pathSum(root, 8)))
    

# [1,null,2,null,3,null,4,null,5]
# 3

    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    root.right.right.right.right = TreeNode(5)
    
    print ( "2 == " + str( solution.pathSum(root, 3)))


if __name__ == "__main__":
    main()
    
    
    
    