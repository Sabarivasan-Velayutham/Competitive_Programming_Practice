
# https://leetcode.com/problems/linked-list-cycle-ii/description/?envType=study-plan&id=level-1

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# space : O(n)
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        arr = [head]
        node = None
        while head:
            if head.next not in arr:
                arr.append(head.next)
            else:
                return head.next
            head = head.next
        return node


# space : O(1)
# FLoyds Cycle detection Algorithm 

# https://www.youtube.com/watch?v=zbozWoMgKW0&t=0s
# https://www.youtube.com/watch?v=LUm2ABqAs1w

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow  = head 
        fast  = head
        cycle = False 
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                cycle = True
                break 
        if cycle == False :
            return None
        
        # there is cycle 
        while (head != slow) :
            head = head.next
            slow = slow.next
        return head 

