
# https://leetcode.com/problems/merge-two-sorted-lists/description/?envType=study-plan&id=level-1

# solution explanation ( recursive mode )
# https://leetcode.com/problems/merge-two-sorted-lists/solutions/759870/python3-solution-with-a-detailed-explanation-dummy-explained/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if not list1 or not list2 :
            return list1 or list2
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next,list2)
            return list1
        else :
            list2.next = self.mergeTwoLists(list1,list2.next)
            return list2
        