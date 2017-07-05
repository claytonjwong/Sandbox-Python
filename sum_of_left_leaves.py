"""


"""



# Definition for a binary root root.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0
        
        #
        # add onto the sum of "left-leaves"
        # if this node contains a child
        # who is a left leaf
        #
        sum_ll = 0
        
        if self.hasLeftLeaf(root):
            sum_ll = root.left.val
            
        return sum_ll + self.sumOfLeftLeaves( root.left ) \
                   + self.sumOfLeftLeaves( root.right )
             

    def hasLeftLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        try:
            
            if root.left is not None and root.left.left is None and root.left.right is None:
                return True
            
        except AttributeError:
            pass
        
        return False
    
def main():
    
    import pdb
#     pdb.set_trace()
    
    solution = Solution()
    
    print ( "0 == " + str ( solution.sumOfLeftLeaves(None)))
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    
    print ( "2 == " + str ( solution.sumOfLeftLeaves(root)))
    
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    
    
#     pdb.set_trace()
    print ( "6 == " + str ( solution.sumOfLeftLeaves(root)))
    
    


if __name__ == "__main__":
    main()
















