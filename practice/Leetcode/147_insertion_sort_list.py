# https://leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, i = head, head.next
        while i:
            j = dummy
            temp = i.next
            while j != prev and j.next.val <= i.val:
                j = j.next
            if j == prev:
                prev = i
                i = i.next
                continue
            i.next = j.next
            j.next = i
            prev.next = temp
            i = temp
        return dummy.next
