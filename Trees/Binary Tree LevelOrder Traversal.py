

# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []
        queue = deque()
        queue.append(root)
        output = []

        while queue:
            nodes_in_curr_level = []
            length = len(queue)

            for _ in range(length):
                curr_node = queue.popleft()
                nodes_in_curr_level.append(curr_node.val)

                if curr_node.left:
                    queue.append(curr_node.left)

                if curr_node.right:
                    queue.append(curr_node.right)

            output.append(nodes_in_curr_level)

        return reversed(output)
