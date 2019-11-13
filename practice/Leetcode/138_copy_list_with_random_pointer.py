# https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        copy = Node(-1, None, None)
        temp1 = head
        prev = copy
        hmap = {}
        while temp1 is not None:
            node = Node(temp1.val, None, None)
            hmap[temp1] = node
            prev.next = node
            prev = node
            temp1 = temp1.next
        temp1 = head
        temp2 = copy.next
        while temp1 is not None:
            if temp1.random in hmap:
                temp2.random = hmap[temp1.random]
            else:
                temp2.random = None
            temp1 = temp1.next
            temp2 = temp2.next
        return copy.next
