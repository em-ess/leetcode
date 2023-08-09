# PROBLEM 1 FOR THE DAY MON JUL 31

# 2236. Root Equals Sum of Children
# You are given the root of a binary tree that consists of exactly 3 nodes: the root, its left child, and its right child.
#
# Return true if the value of the root is equal to the sum of the values of its two children, or false otherwise.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def checkTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
       return root.val == (root.left.val + root.right.val)
#Success Runtime: 
  
