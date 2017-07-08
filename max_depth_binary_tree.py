"""

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        #
        # root does NOT exist, this is a empty tree with depth 0
        #
        if ( not root ):
            return 0
        
        #
        # root exists, this is a tree with at least depth 1
        #
        return self.maxDepthHelper(root, 1)
        
            
    def maxDepthHelper(self, node, depth):
        
        #
        # this node does NOT count since it does NOT exist,
        # return depth - 1
        #
        if ( not node ):
            return depth - 1 
        
        #
        # assume child nodes exist for recursive case and add 1 onto the depth
        #
        return max ( self.maxDepthHelper(node.left, depth+1), self.maxDepthHelper(node.right, depth+1) )
    
    
def main():
    
    solution = Solution()
    
    
    node0 = None
    print ( "0 == " + str ( solution.maxDepth(node0) ) )
    
    
    node1 = TreeNode(1)
    print ( "1 == " + str ( solution.maxDepth(node1) ) )
    
    
    node2 = TreeNode(2)
    node2.left = TreeNode(2)
    
    print ( "2 == " + str ( solution.maxDepth(node2)))
    
    
if __name__ == "__main__":
    main()
    
