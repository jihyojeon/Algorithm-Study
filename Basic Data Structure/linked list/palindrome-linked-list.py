# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import collections

class Solution:
    def LIST_isPalindrome(self, head: ListNode) -> bool:
        list_head = []
        node = head
        while True:
            if node is None:
                break
            list_head.append(node.val)
            node = node.next

        while True:
            if len(list_head) <= 1:
                return True
            if list_head.pop() == list_head.pop(0):
                continue
            else:
                return False

    def deque_isPalindrome(self, head: ListNode) -> bool:
        deque_head = collections.deque()
        node = head
        while True:
            if node is None:
                break
            deque_head.append(node.val)
            node = node.next

        while True:
            if len(deque_head) <= 1:
                return True
            if deque_head.pop() == deque_head.popleft():
                continue
            else:
                return False