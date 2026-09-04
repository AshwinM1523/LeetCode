# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []

        if root == None:
            return ans
        
        # all the way left
        leftOutput = self.inorderTraversal(root.left)
        # add number
        ans += leftOutput
        ans.append(root.val)
        # all the way right
        rightOutput = self.inorderTraversal(root.right)

        return ans + rightOutput
