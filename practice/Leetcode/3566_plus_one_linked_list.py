# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3566/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def addOne(node):
            if node.next:
                carry = addOne(node.next)
            else:
                carry = 1
            ret = (node.val + carry) // 10
            node.val = (node.val + carry) % 10
            return ret
        
        carry = addOne(head)
        if carry:
            temp = ListNode(1)
            temp.next = head
            return temp
        return head
