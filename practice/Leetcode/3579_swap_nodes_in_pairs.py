# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/572/week-4-december-22nd-december-28th/3579/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        p = head
        while p and p.next:
            t = p.next
            p.next = t.next
            t.next = p
            if p == head:
                head = t
            else:
                q.next = t
            q = p
            p = p.next
        return head
