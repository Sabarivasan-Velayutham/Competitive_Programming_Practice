
# https://leetcode.com/problems/reverse-linked-list/description/

# https://leetcode.com/problems/reverse-linked-list/solutions/3081886/100-best-and-easy-solution-explained-visualization/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        temp = head
        while temp:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        return prev
