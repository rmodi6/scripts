# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3468/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        node = Node(insertVal)
        if not head:
            node.next = node
            return node
        if head.next == head:
            node.next = head
            head.next = node
            return head
        pointer = head
        if insertVal >= pointer.val and insertVal <= pointer.next.val:
            node.next = pointer.next
            pointer.next = node
            return head
        if pointer.next.val < pointer.val and (insertVal <= pointer.next.val or insertVal >= pointer.val):
            node.next = pointer.next
            pointer.next = node
            return head
        pointer = pointer.next
        while pointer != head:
            if insertVal >= pointer.val and insertVal <= pointer.next.val:
                node.next = pointer.next
                pointer.next = node
                break
            if pointer.next.val < pointer.val and (insertVal <= pointer.next.val or insertVal >= pointer.val):
                node.next = pointer.next
                pointer.next = node
                break
            pointer = pointer.next
        if not node.next:
            node.next = head.next
            head.next = node
        return head
