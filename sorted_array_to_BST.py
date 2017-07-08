"""

108. Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        if ( nums is None or nums == [] ):
            return None
        
        #
        # find the middle of the sorted array
        # and use that as the parent node
        #
        len_nums = len ( nums )
        middle_index = int ( len_nums / 2 )
        
        #
        # parent node
        #
        newNode = TreeNode( nums[middle_index] )
        
        #
        # left child node is created from the left-half of the array
        #
        newNode.left = self.sortedArrayToBST( nums[0:middle_index] )
        
        #
        # right child node is created from the right-half of the array
        #
        newNode.right = self.sortedArrayToBST( nums[middle_index+1:len_nums] )
        
        
        return newNode
    
    
def main():
    
    solution = Solution()    
    tree = solution.sortedArrayToBST([0,1,2,3,4,4,5])
    


if __name__ == "__main__":
    main()
    
    
    