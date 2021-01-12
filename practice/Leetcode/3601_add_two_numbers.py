# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3601/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = head = ListNode(-1)
        carry = 0
        while l1 and l2:
            s = l1.val + l2.val + carry
            carry = s // 10
            head.next = ListNode(s % 10)
            head = head.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            s = l1.val + carry
            carry = s // 10
            head.next = ListNode(s % 10)
            head = head.next
            l1 = l1.next
        while l2:
            s = l2.val + carry
            carry = s // 10
            head.next = ListNode(s % 10)
            head = head.next
            l2 = l2.next
        if carry:
            head.next = ListNode(carry)
        return ans.next
