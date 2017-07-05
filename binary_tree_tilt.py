"""

563. Binary Tree Tilt

https://leetcode.com/problems/binary-tree-tilt/#/description


Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.

Example:
Input: 
         1
       /   \
      2     3
Output: 1
Explanation: 
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.tilt = 0
        
        def _sum(node):
            if not node:
                return 0
            
            left, right = _sum(node.left), _sum(node.right) 
            
            self.tilt += abs ( left - right )
            
            return node.val + left + right

        if not root:
            return 0
        
        _sum(root)
        return self.tilt
        
    
    
def main():
    
    solution = Solution()
    
    root = None
    
    
    print ( "0 == " + str ( solution.findTilt(root) ))

    root = TreeNode(0)
    
    print ( "0 == " + str ( solution.findTilt(root) ))
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print ( "1 == " + str ( solution.findTilt(root) ))
    
    root.left.left = TreeNode(4)
    
    root.right.left = TreeNode(5)

    import pdb
    
    pdb.set_trace()

    print ( "11 == " + str ( solution.findTilt(root) ))

if __name__ == '__main__':
    main()







