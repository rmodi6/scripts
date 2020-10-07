# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3486/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1
        k = k % n
        if k == 0:
            return head
        i = 0
        temp = head
        while i < n - k - 1:
            i += 1
            temp = temp.next
        tail.next = head
        head = temp.next
        temp.next = None
        return head
