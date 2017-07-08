"""

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.


"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


MAX = pow(2,31)-1

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if ( root is None ):
            return 0

        return self.minDepthHelper(root, 1)
        
        
    def minDepthHelper(self, root, depth):
        
        #
        # return an arbitarily large value for nodes
        # which are NOT leaf nodes
        #
        if ( root is None ):
            return MAX
        
        #
        # return a valid value for depth for leaf nodes
        #
        if ( root.left is None and root.right is None ):
            return depth
            
        #
        # return the minimum of the the subtrees
        #
        return min ( self.minDepthHelper(root.left, depth+1), self.minDepthHelper(root.right, depth+1) )
    
    