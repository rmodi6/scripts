# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3660/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def getLength(node):
            i = 0
            while node:
                node = node.next
                i += 1
            return i
        a = getLength(headA)
        b = getLength(headB)
        n = max(a, b)
        while headA and headB:
            if headA == headB:
                return headA
            if n <= a:
                headA = headA.next
            if n <= b:
                headB = headB.next
            n -= 1
        return None
