# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.sum=0
        def mid(root):
            if root.left:
                mid(root.left)
            if root.val>=L and root.val<=R:
                self.sum+=root.val
            if root.right:
                mid(root.right)
        if root:
            mid(root)
        return self.sum 