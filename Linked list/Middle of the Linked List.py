

# https://leetcode.com/problems/middle-of-the-linked-list/description/?envType=study-plan&id=level-1

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tcount = 0 
        tmp = head  
        while tmp :
            tcount += 1
            tmp = tmp.next

        ind = tcount//2+1
        print(tcount,ind)

        tcount = 1
        tmp = head 
        while tcount!=ind:
            tcount += 1 
            tmp = tmp.next
        return tmp


# c++ code 
'''
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode *slow = head;
        ListNode *fast = head;
        while(fast != NULL && fast->next != NULL){
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }
};
'''