"""

Given a binary tree and a sum, determine if the tree
has a root-to-leaf path such that adding up all the values
along the path equals the given sum.

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.hasPathSumHelper(root, 0, sum)
            
    def hasPathSumHelper(self, node, curr_sum, target):
        
        #
        # if node is None, return False,
        # otherwise, add the node value
        # onto the current sum
        #
        if ( node is None ):
            return False
        else:
            curr_sum += node.val

        #
        # check if this is a leave node,
        # if so, then return True if the current sum
        # is equal to the target value
        #
        if ( node.left is None and node.right is None ):
            return curr_sum == target
        
        #
        # if this is NOT a leave node, then check children
        #
        else:
        
            return self.hasPathSumHelper( \
                        node.left, curr_sum, target ) \
            or \
                    self.hasPathSumHelper( \
                        node.right, curr_sum, target )
    
    
def main():
    
    solution = Solution()
    
    
    root = TreeNode(1)
    sum = 1
    
    print ( "True == " + str ( solution.hasPathSum(root, sum) ) )


    root.left = TreeNode(2)
    sum = 3
    
    
    print ( "True == " + str ( solution.hasPathSum(root, sum) ) )

if __name__ == "__main__":
    main()