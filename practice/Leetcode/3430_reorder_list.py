# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3430/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        pointers = []
        while head:
            pointers.append(head)
            head = head.next
        for i in range(len(pointers) // 2):
            pointers[i].next = pointers[-i-1]
            pointers[-i-1].next = pointers[i+1]
        pointers[len(pointers) // 2].next = None
