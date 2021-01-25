# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3615/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap, head = [], ListNode(-1)
        tail = head
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i))
        while heap:
            value, i = heapq.heappop(heap)
            tail.next = ListNode(value)
            tail = tail.next
            if lists[i].next:
                lists[i] = lists[i].next
                heapq.heappush(heap, (lists[i].val, i))
        return head.next
