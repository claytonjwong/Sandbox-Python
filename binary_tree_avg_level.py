

"""

637. Average of Levels in Binary Tree

https://leetcode.com/contest/leetcode-weekly-contest-40/problems/average-of-levels-in-binary-tree/


Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5,
and on level 2 is 11. Hence return [3, 14.5, 11].

"""




# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

class Solution(object):
    def __init__(self):
        self.depth_node_list = {}
    
    def averageOfLevelsHelper(self, node, depth):
        
        if node is None:
            return None
        
        if depth in self.depth_node_list:
            self.depth_node_list[depth].append(node.val)
        else:
            self.depth_node_list[depth] = [node.val]
            
        self.averageOfLevelsHelper(node.left, depth+1)
        self.averageOfLevelsHelper(node.right, depth+1)
        
        
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        result = []
        
        if root == None:
            return []
        
        self.averageOfLevelsHelper(root, 0)
        
        for key, node_list in self.depth_node_list.items():
            
            sum = 0.0
            cnt = 0.0
            for val in node_list:
                
                sum += val
                cnt += 1.0
                
            result.append(sum/cnt)
            
        
        return result
            
        
    
def main():
    
    solution = Solution()
    
    print (str(solution.averageOfLevels(None)))
    
    tree = TreeNode(3)
    
    print (str(solution.averageOfLevels(tree)))
    
    tree.left = TreeNode(9)
    tree.right = TreeNode(20)
    
    print (str(solution.averageOfLevels(tree)))
    
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)
    
    print (str(solution.averageOfLevels(tree)))
    
if __name__ == '__main__':
    main()
        
        
        
        
        
        
        