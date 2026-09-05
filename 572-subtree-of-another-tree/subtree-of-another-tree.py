# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(p, q) -> bool:
            
            def dfs(root1, root2):
                if root1 == None and root2 == None:
                    return True
                elif (root1 == None and root2 != None) or (root1 != None and root2 == None):
                    return False
                
                if root1.val != root2.val:
                    return False
                
                leftDepth = dfs(root1.left, root2.left)
                rightDepth = dfs(root1.right, root2.right)

                return leftDepth and rightDepth
            
            return dfs(p, q)
        
        def dfs(k):
            if k == None:
                return False
            
            leftDepth = dfs(k.left)
            rightDepth = dfs(k.right)

            return isSameTree(k, subRoot) or leftDepth or rightDepth
        
        return dfs(root)