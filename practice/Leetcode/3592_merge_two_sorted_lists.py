# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3592/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ans = None
        while l1 and l2:
            if l1.val < l2.val:
                temp = ListNode(l1.val)
                l1 = l1.next
            else:
                temp = ListNode(l2.val)
                l2 = l2.next
            if not head:
                head = ans = temp
            else:
                ans.next = temp
                ans = ans.next
        if l1:
            if not head:
                head = ans = l1
            else:
                ans.next = l1
        if l2:
            if not head:
                head = ans = l2
            else:
                ans.next = l2
        return head
