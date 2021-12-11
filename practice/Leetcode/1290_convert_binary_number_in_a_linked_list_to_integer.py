# https://leetcode.com/contest/weekly-contest-167/problems/convert-binary-number-in-a-linked-list-to-integer/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        n = ''
        while head is not None:
            n += str(head.val)
            head = head.next
        return int(n, 2)

# Alternate solution

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        return self.getDecimalValueUtil(head)[0]
    
    def getDecimalValueUtil(self, node):
        if node is None:
            return 0, -1
        val, index = self.getDecimalValueUtil(node.next)
        return node.val * (2**(index+1)) + val, index+1
