# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3396/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            head = head.next
        if not head:
            return head
        p = head
        q = p.next
        while q:
            if q.val == val:
                p.next = q.next
                q = q.next
                continue
            p = q
            q = q.next
        return head
