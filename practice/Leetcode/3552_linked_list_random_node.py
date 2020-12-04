# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3552/

import random

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        self.n = 0
        temp = head
        while temp:
            temp = temp.next
            self.n += 1

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        r = random.randint(0, self.n-1)
        i = 0
        temp = self.head
        while i < r:
            temp = temp.next
            i += 1
        return temp.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
