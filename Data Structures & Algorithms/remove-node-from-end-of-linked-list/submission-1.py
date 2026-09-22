# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # initial thought: iterate a fast pointer to the end and get the length.
        # Once we have the length a slow pointer will iterate to that specific position

        length = n

        dummy = ListNode(-1)
        dummy.next = head
        fast = head
        slow = dummy

        while length > 0:
            fast = fast.next
            length -= 1

        while fast:
            slow = slow.next
            fast = fast.next
            

            
        slow.next = slow.next.next


        return dummy.next

        