# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3635/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        copy = Node('-1')
        prev = copy
        hmap = {}
        while head:
            if head in hmap:
                node = hmap[head]
            else:
                node = Node(head.val)
                hmap[head] = node
            if head.random is None:
                rand = None
            elif head.random not in hmap:
                rand = Node(head.random.val)
                hmap[head.random] = rand
            else:
                rand = hmap[head.random]
            node.random = rand
            prev.next = node
            prev = node
            head = head.next
        return copy.next
