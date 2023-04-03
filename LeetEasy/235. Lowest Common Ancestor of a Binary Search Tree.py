# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # Function to return LCA node
    def LCA(self, root, mi, mx):
        # If minimum value is lesser or equal to root and
        # root value is lesser or equal to maximum value 
        # Than root is LCA
        if mi <= root.val and root.val <=mx:
            return root
        # Else if minimum amd maximum is lesser than root than check in left sub tree
        if mi < root.val and mx < root.val:
            return self.LCA(root.left, mi, mx)
        # Else check in right sub tree
        return self.LCA(root.right,mi, mx)

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Condition to make sure that p is always lesser than q
        if p.val>q.val:
            p,q=q,p
        # Function call to LCA which returns the LCA node(treenode)
        return self.LCA(root, p.val, q.val)