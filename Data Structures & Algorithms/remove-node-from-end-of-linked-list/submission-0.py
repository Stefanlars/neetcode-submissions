# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # initial thought: iterate a fast pointer to the end and get the length.
        # Once we have the length a slow pointer will iterate to that specific position

        length = 0

        fast = head

        while fast:
            length += 1

            fast = fast.next

        prev = None
        slow = head

        for i in range(length - n):
            if slow:
                prev = slow
                slow = slow.next

        if prev:
            prev.next = slow.next
            return head
        else:
            return slow.next

        