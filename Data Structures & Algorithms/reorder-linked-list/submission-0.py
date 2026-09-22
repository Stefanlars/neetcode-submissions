# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not head:
            return
        

        slow = fast = head

        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # with prev we can reverse the second half of the list and then glue it all together

        prev = None
        curr = slow

        while curr:
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp

        # while prev:
        #     print(prev.val)
        #     prev = prev.next
        
        # while head:
        #     print(head.val)
        #     head = head.next

        firstHalf = head
        secondHalf = prev

        while firstHalf and secondHalf:
            temp1 = firstHalf.next
            temp2 = secondHalf.next

            secondHalf.next = None

            firstHalf.next = secondHalf
            secondHalf.next = temp1

            firstHalf = secondHalf.next
            secondHalf = temp2

        







        
        