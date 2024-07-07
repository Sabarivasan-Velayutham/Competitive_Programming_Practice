

# QUESTION : https://leetcode.com/problems/maximum-width-of-binary-tree/
# 662. Maximum Width of Binary Tree

# Reference : https://www.youtube.com/watch?v=ZbybYvcVLks

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def widthOfBinaryTree(self, root) -> int:
        if not root:
            return 0
        ans = 1
        queue = deque()  #create queue
        queue.append([root, 0])

        while queue:
            start = queue[0][1] #first node in that level 
            end = queue[-1][1]  #last node in that level 
            ans = max(ans, end-start+1)  #maximum width at that level 

            for i in range(len(queue)):
                temp = queue.popleft()  # remove first node 
                #append its left or right node to that queue 
                if temp[0].left:
                    queue.append([temp[0].left, temp[1]*2])
                if temp[0].right:
                    queue.append([temp[0].right, temp[1]*2+1])
        return ans
