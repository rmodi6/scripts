# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3331/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        p = head
        q = head.next
        while q is not None and q.next is not None:
            temp = p.next
            p.next = q.next
            q.next = q.next.next
            p.next.next = temp
            p = p.next
            q = q.next
        return head
