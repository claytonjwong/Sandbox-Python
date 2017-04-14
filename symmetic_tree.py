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
    
    #
    # traverse each half of the tree in opposite directions,
    # and push to a stack.  If the stacks are equal, then return True,
    # False otherwise
    #
    left_stack = []
    right_stack = []
    
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
        # the tree is symetmetic if it is just a node without children
        #
        if ( root.left == None and root.right == None ):
            return True
        
        #
        # ensure the values of the left and right children are the same
        #
        elif ( root.left and root.right ):
            
            if ( root.left.val != root.right.val ):
                return False
            
            else:
                self.traverse_left_first_and_push_to_stack(root.left)
                self.traverse_right_first_and_push_to_stack(root.right)
                
                #
                # check if the stacks are equal
                #
                return ( self.left_stack == self.right_stack )
                
        #
        # either root.left is None or root.right is None
        # regardless, the tree is NOT symmetric
        #
        else:
            return False


    def traverse_left_first_and_push_to_stack(self, node):
        
        if ( not node ):
            self.left_stack.append(None)
            return
        
        self.left_stack.append(node.val)
        self.traverse_left_first_and_push_to_stack(node.left)
        self.traverse_left_first_and_push_to_stack(node.right)
        
    
    def traverse_right_first_and_push_to_stack(self, node):
        
        if ( not node ):
            self.right_stack.append(None)
            return
        
        self.right_stack.append(node.val)
        self.traverse_right_first_and_push_to_stack(node.right)
        self.traverse_right_first_and_push_to_stack(node.left)
        

#     def push_and_traverse_left_first(self, node):
#         
#         #
#         # push, then traverse left first, followed by right
#         #
#         if ( node and node.val ):
#             self.equality_stack.append(node.val)
#             self.push_and_traverse_left_first(node.left)
#             self.push_and_traverse_left_first(node.right)
#         else:
#             self.equality_stack.append(None)
# 
# 
#     def traverse_right_first_and_pop(self, node):
#         
#         #
#         # traverse right first, then left, then start popping off
#         # in order to ensure that the popped values equal
#         # the previously pushed values
#         #
#         if ( node and node.val ):
#             
#             self.traverse_right_first_and_pop(node.right)
#             self.traverse_right_first_and_pop(node.left)
#             
#         current_value = self.equality_stack.pop()
#         
#         if ( current_value == node == None ) \
#         or ( current_value and node and current_value == node.val ): \
#             return True
            
    
    
def main():
    
    solution = Solution()
    
    single_node = TreeNode(0)
    
    print ( "single True == " + str ( solution.isSymmetric(single_node) ) )
    
    
    unsymmetric_tree = TreeNode(1)
    
    unsymmetric_tree.left = TreeNode(2)
    
    print ( "False == " + str ( solution.isSymmetric(unsymmetric_tree) ) )
    
    
    unsymmetric_tree.right = TreeNode(2)
    
    import pdb
    pdb.set_trace()
    
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