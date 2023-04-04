"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    # Function for preorder traversing
    def pr(self,root,output):
        # If root is None than return because it has reached the end
        if root== None:
            return 
        # Else append the root value to output list
        # So that we can record the preorder traversing
        output.append(root.val)
        # Recursivly traverse through all the children
        for i in root.children:
            self.pr(i,output)

    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # Intializing empty list
        output=[]
        # Function call to preorder traversal
        self.pr(root,output)
        # Returning the output list
        return output