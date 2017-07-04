"""

606. Construct String from Binary Tree

https://leetcode.com/problems/construct-string-from-binary-tree/

You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())", 
but you need to omit all the unnecessary empty parenthesis pairs. 
And it will be "1(2(4))(3)".
Example 2:
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example, 
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.



"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        result = self.tree2strHelper(t)
        
        #
        # leaf node, remove empty brackets for left and right nodes
        #
        result = result.replace("[]()","")
        
        #
        # remove empty right nodes
        #
        result = result.replace("()", "")
        
        #
        # change empty left nodes from [] to (),
        # this is needed as a place holder when
        # the left node is empty, but the right node exists
        #
        result = result.replace("[", "(")
        result = result.replace("]", ")")
        
        
        return result
    
    def tree2strHelper(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
            return ""
        
        #
        # use "[]" as an empty place holder for the left node 
        #
        return str(t.val) + "[" + self.tree2strHelper(t.left) + "](" + self.tree2strHelper(t.right) + ")"

                 
    
def main():
    
    solution = Solution()
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    

    
    print ( "1(2()(4))(3) == " + solution.tree2str(root) )
    
if __name__ == '__main__':
    main()












