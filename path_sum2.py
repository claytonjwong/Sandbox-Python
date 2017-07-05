"""

113. Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]

"""

# Definition for a binary tree node.
class TreeNode(object):
    

    
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

class Solution(object):
    
    def __init__(self):
        self.pathSumList = []
        
    
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        if root is None:
            return []
        
        self.pathSumHelper(root, [], 0, sum)
        
        return self.pathSumList
    
    
    def pathSumHelper(self, node, path_so_far, sum_so_far, sum_target):
        """
        :type node: TreeNode
        :type path_so_far: List[int]
        :type sum_so_far: int
        :type sum_target: int
        """
        
        #
        # include current node in the path so far list and sum so far
        #
        path_so_far.append(node.val)
        sum_so_far += node.val
        
        #
        # leaf node, no more recursion
        #
        if node.left is None and node.right is None:
            
            #
            # target sum match
            #
            if sum_so_far == sum_target:
                
                #
                # create a new list from path_so_far, 
                # and append it onto the path sum list of lists
                #
                # [ note: path_so_far[:] is the same as list(path_so_far) ]
                #
                self.pathSumList.append(path_so_far[:])
                
        #
        # recursively go through the tree, we need to pop from path_so_far,
        # since it is a list which is passed by reference.  We do NOT need to
        # "reset" the sum_so_far, in this same manner, because it is an int
        # which is passed by value
        #
        if node.left is not None:
            self.pathSumHelper(node.left, path_so_far, sum_so_far, sum_target)
            path_so_far.pop()
            
        if node.right is not None:
            self.pathSumHelper(node.right, path_so_far, sum_so_far, sum_target)
            path_so_far.pop()
                
    
def main():
    
    import pdb
    
    solution = Solution()

    root = TreeNode(0)
    

    solution.pathSum(root, 0)
    
    print ( "[[0]] == " + str ( solution.pathSumList ) ) 
    
    
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
    
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
#     pdb.set_trace() 
    solution.pathSum(root, 22)
    
       
    print ( str ( solution.pathSumList ) )


if __name__ == "__main__":
    main()






