"""

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def isSymmetricTraverser(self, nodeA, nodeB):
        
        #
        # if either left or right is none, then return True
        # is both are None, otherwise return False
        #
        if ( nodeA is None or nodeB is None ):
            return nodeA == nodeB
        else:
            return nodeA.val == nodeB.val \
               and self.isSymmetricTraverser(nodeA.left, nodeB.right) \
               and self.isSymmetricTraverser(nodeA.right, nodeB.left)
               
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        #
        # empty tree is symmetric
        #
        if ( not root ):
            return True

        #
        # recusively traverse each tree
        #        
        return self.isSymmetricTraverser(root.left, root.right)

            
    
    
def main():
    
    solution = Solution()
    
    single_node = TreeNode(0)
    
    print ( "single True == " + str ( solution.isSymmetric(single_node) ) )
    
    
    unsymmetric_tree = TreeNode(1)
    
    unsymmetric_tree.left = TreeNode(2)
    
    print ( "False == " + str ( solution.isSymmetric(unsymmetric_tree) ) )
    
    
    unsymmetric_tree.right = TreeNode(2)
    
#     import pdb
#     pdb.set_trace()
    
    print ( "True == " + str ( solution.isSymmetric(unsymmetric_tree) ) )
    
    #
    #     1
    #    / \
    #   2   2
    #    \   \
    #    3    3
    #
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.left.left = None
    node.left.right = TreeNode(3)
    
    node.right = TreeNode(2)
    node.right.right = TreeNode(3)
    node.right.left = None
    
    
    
    
    print ( "False == " + str ( solution.isSymmetric(node) ) )

if __name__ == "__main__":
    main()