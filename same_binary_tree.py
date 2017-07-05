"""

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        #
        # base case, empty trees are equal
        #
        if ( p == None and q == None ):
            return True
        
        #
        # if the values of the current nodes are the same,
        # check the left and right children recursively
        # return False if the node values are NOT equal 
        #
        elif ( p and q ):
            
            if ( p.val == q.val ):
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False
        
        #
        # ( p exists and q does NOT  ) or  ( q exists and p does NOT )
        # either way, the trees are not equal
        #    
        else:
            return False
            
    
    
def main():
    
    tree_A = None
    tree_B = None
    
    solution = Solution()
    
    print ( "True == " + str ( solution.isSameTree(tree_A, tree_B) ) )
    
    
    tree_A = TreeNode(1)
    tree_B = TreeNode(1)
    
    print ( "True == " + str ( solution.isSameTree(tree_A, tree_B) ) )
    

    tree_A = TreeNode(0)
    tree_B = TreeNode(1)
    
    print ( "False == " + str ( solution.isSameTree(tree_A, tree_B) ) )


    tree_A = TreeNode(1)
    tree_A.left = TreeNode(2)
    tree_A.right = TreeNode(3)

    tree_B = TreeNode(1)
    tree_B.left = TreeNode(2)
    tree_B.right = TreeNode(3)
    
    print ( "True == " + str ( solution.isSameTree(tree_A, tree_B) ) )

if __name__ == "__main__":
    main()