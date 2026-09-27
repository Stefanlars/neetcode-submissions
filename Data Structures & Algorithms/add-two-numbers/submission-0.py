# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        def add(l1, l2, carry) -> Optional[ListNode]:

            if not l1 and not l2 and carry == 0:
                return None

            
            curr = ListNode()

            add_sum = carry

            if l1:
                add_sum += l1.val
            
            if l2:
                add_sum += l2.val

            curr_carry = 0

            if add_sum >= 10:
                curr_carry = add_sum // 10
                add_sum = add_sum % 10

            curr.val = add_sum

            curr.next = add(l1.next if l1 else None, l2.next if l2 else None, curr_carry)


            return curr

        return add(l1, l2, 0)