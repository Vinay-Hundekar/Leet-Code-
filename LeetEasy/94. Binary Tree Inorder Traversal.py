# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # Function for inorder traversal and append the root value in the output list
    def inorder(self,root,output):
        if root==None:
            return
        # recursion to traverse left node
        self.inorder(root.left,output)
        output.append(root.val)
        # recursion to traverse right node
        self.inorder(root.right,output)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Initializing empty list
        output=[]
        # Function call for inorder traversal
        self.inorder(root,output)
        # Returning the output list
        return output