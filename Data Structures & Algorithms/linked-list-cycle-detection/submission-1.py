# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        turtle = head
        rabbit = head

        while turtle.next and rabbit.next and rabbit.next.next:
        
            turtle = turtle.next

            rabbit = rabbit.next.next

            if turtle is rabbit:
                return True


        return False
