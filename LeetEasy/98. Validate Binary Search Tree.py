# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # Function for inorder traversing and append each element into items list
    def inorder(self, root,items):
        if root is None:
            return
        self.inorder(root.left,items)
        items.append(root.val)
        self.inorder(root.right,items)

    def isValidBST(self, root):
        # Creating empty list
        items =[]
        # Function call for list of elements, obtained by inorder traversaal
        self.inorder(root,items)
        
        # Checking wether list is sorted in assending order or not
        # If sorted than its binary search tree return True, because inorder traversal of
        # binary search tree gives sorted list of elements in assending order
        # If the list is not sorted in assending order than its not a BST 
        # Hence return False
        for i in range(len(items)-1):
			if items[i]>= items[i+1]:
				return False
        return True