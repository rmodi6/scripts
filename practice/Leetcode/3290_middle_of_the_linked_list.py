# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3290/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        p, q = head, head
        while p and p.next:
            p = p.next.next
            q = q.next
        return q
