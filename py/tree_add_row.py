"""

623. Add One Row to Tree

Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d. The root node is at depth 1.

The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1, create two tree nodes with value v as N's left subtree root and right subtree root. And N's original left subtree should be the left subtree of the new left subtree root, its original right subtree should be the right subtree of the new right subtree root. If depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as the new root of the whole original tree, and the original tree is the new root's left subtree.

Example 1:
Input: 
A binary tree as following:
       4
     /   \
    2     6
   / \   / 
  3   1 5   

v = 1

d = 2

Output: 
       4
      / \
     1   1
    /     \
   2       6
  / \     / 
 3   1   5   

Example 2:
Input: 
A binary tree as following:
      4
     /   
    2    
   / \   
  3   1    

v = 1

d = 3

Output: 
      4
     /   
    2
   / \    
  1   1
 /     \  
3       1
Note:
The given d is in range [1, maximum depth of the given tree + 1].
The given binary tree has at least one tree node.


"""



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def __init__(self):
        
        self.insert_here = []
    
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        #
        #  If depth d is 1 that means there is no depth d-1 at all,
        # then create a tree node with value v as the new root of the whole original tree,
        # and the original tree is the new root's left subtree.
        #
        if d == 1:
            new_tree = TreeNode(v)
            new_tree.left = root
            return new_tree
        
        #
        # recursively traverse the tree,
        # and include nodes to be updted
        # in the insert_here list
        #
        self.addOneRowHelper(root, v, d, curr_depth=1)
        
        #
        # go through the insert_here list and
        # add the value to insert
        #
        for node in self.insert_here:
            
            #
            # left
            #
            temp = node.left
            node.left = TreeNode(v)
            node.left.left = temp
            
            #
            # right
            #
            temp = node.right
            node.right = TreeNode(v)
            node.right.right = temp
        
        #
        # return the modified tree
        #
        return root
    
    
    def addOneRowHelper(self, node, v, d, curr_depth):
        """
        :type node: TreeNode
        :type v: int
        :type d: int
        :type curr_depth: int
        :rtype: None
        """
        
        #
        # end recursion when there are no more nodes to traverse till depth d-1
        #
        if node is None:
            return
    
        #
        # end recursion at depth d-1
        #
        if curr_depth == d - 1:
                
            self.insert_here.append(node)
        
        #
        # recursively check left and right nodes in the next depth down
        #
        elif curr_depth < d:
            
            self.addOneRowHelper(node.left, v, d, curr_depth+1) 
            self.addOneRowHelper(node.right, v, d, curr_depth+1)
    
def main():
    
    solution = Solution()
    
# Input: 
# A binary tree as following:
#        4
#      /   \
#     2     6
#    / \   / 
#   3   1 5   
# 
# v = 1
# 
# d = 2
# 
# Output: 
#        4
#       / \
#      1   1
#     /     \
#    2       6
#   / \     / 
#  3   1   5  
 
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(5)
    

    solution.addOneRow(root, v=1, d=2)
    
    
if __name__ == '__main__':
    main()    
    
    