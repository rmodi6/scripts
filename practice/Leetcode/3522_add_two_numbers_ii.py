# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3522/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        def add(t1, t2, len1, len2):
            if not t1.next and not t2.next:
                return ListNode((t1.val + t2.val) % 10), (t1.val + t2.val) // 10
            if len1 == len2:
                ans, carry = add(t1.next, t2.next, len1-1, len2-1)
                return ListNode((t1.val + t2.val + carry) % 10, ans), (t1.val + t2.val + carry) // 10
            if len1 > len2:
                ans, carry = add(t1.next, t2, len1-1, len2)
                return ListNode((t1.val + carry) % 10, ans), (t1.val + carry) // 10
            if len2 > len1:
                ans, carry = add(t1, t2.next, len1, len2-1)
                return ListNode((t2.val + carry) % 10, ans), (t2.val + carry) // 10
                
        
        len1, len2 = 0, 0
        t1, t2 = l1, l2
        while t1:
            t1 = t1.next
            len1 += 1
        while t2:
            t2 = t2.next
            len2 += 1
        ans, carry = add(l1, l2, len1, len2)
        if carry:
            ans = ListNode(1, ans)
        return ans
