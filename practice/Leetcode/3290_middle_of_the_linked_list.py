# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3290/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        p, q = head, head
        i = 0
        while p.next:
            p = p.next
            if i % 2 == 0:
                q = q.next
            i += 1
        return q
