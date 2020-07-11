# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/545/week-2-july-8th-july-14th/3386/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        p = head
        while p:
            if p.child:
                q = self.flatten(p.child)
                p.child = None
                temp = p.next
                p.next = q
                q.prev = p
                if temp:
                    while q.next:
                        q = q.next
                    q.next = temp
                    temp.prev = q
                p = temp
            else:
                p = p.next
        return head
