"""

652. Find Duplicate Subtrees

https://leetcode.com/contest/leetcode-weekly-contest-43/problems/find-duplicate-subtrees/

Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1: 
        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:
      2
     /
    4
and
    4
Therefore, you need to return above trees' root in the form of a list.


"""

import collections

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def findDuplicateSubtrees(self, root):
        
        # flatten each tree as a string representation of each subtree
        # use the string value as a key in the hash of trees
        # use list of TreeNode as the value for each hash entry
        # then see where hash collisions occur, these are dup subtrees
        def to_string(root):
            if root is None:
                return "None"
            key = \
                "(left=" + to_string(root.left) + \
                ",right=" + to_string(root.right) + \
                ",root=" + str(root.val) + ")"
            trees[key].append(root)
            return key
        
        trees = collections.defaultdict(list) # default list is []
        to_string(root)
        
        return [roots[0] for roots in trees.values() if len(roots)>1]
        
        
    # n + n/2 + n/4 + ... + 2 + 1   storage is 2n
 
        
if __name__ == '__main__':
    
    """
        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
    """
    
#     root = TreeNode(1)
#     root.left = TreeNode(2)
#     root.right = TreeNode(3)
#     root.left.left = TreeNode(4)
#     root.right.left = TreeNode(2)
#     root.right.left.left = TreeNode(4)
#     root.right.right = TreeNode(4)


#     root = TreeNode(6)
#     root.right = TreeNode(0)
#     root.left = TreeNode(5)
#     root.left.left = TreeNode(-2)
#     root.left.right = TreeNode(6)
#     root.left.left.left = TreeNode(5)
#     root.left.right.right = TreeNode(-3)
#     root.left.left.left.left = TreeNode(6)
#     root.left.left.left.right = TreeNode(-5)
#     root.left.left.left.left.right = TreeNode(0)
    
    root = TreeNode(0)
    root.left = TreeNode(0)
    root.right = TreeNode(0)
    root.left.left = TreeNode(0)
    root.right.right = TreeNode(0)
    root.right.right.right = TreeNode(0)
        
    solution = Solution()
    
    import pdb
    pdb.set_trace()
    result = solution.findDuplicateSubtrees(root)
    
    i=0
    for tree in result:
        
        print("\n\n\n\nprinting tree: " + str(i) + "...") 
        queue = []
        queue.append(tree)
        
        while len(queue) > 0:
            
            curr = queue.pop(0)
            
            if curr:
                print ("Value: " + str(curr.val))
            
            if curr.left:
                queue.append(curr.left)
                
            if curr.right:
                queue.append(curr.right)
        
        i+=1
        
    print ("\n\n\n That's all!")
    
        
#     result = solution.doTreesMatch(root.right.left.left, root.right.right)
      
    
    
    
    
    
    
    