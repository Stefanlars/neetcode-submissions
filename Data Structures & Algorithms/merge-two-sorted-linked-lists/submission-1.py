# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(-1)

        prev = dummy


        while list1 and list2:
            
            temp1 = list1
            list1 = list1.next
            temp1.next = None

            temp2 = list2
            list2 = list2.next
            temp2.next = None

            if temp1.val < temp2.val:
                prev.next = temp1
                prev = prev.next
                
                temp2.next = list2
                list2 = temp2
            else:
                prev.next = temp2
                prev = prev.next
                
                temp1.next = list1
                list1 = temp1
            

        if list1 and not list2:
            prev.next = list1
        else:
            prev.next = list2
        
        return dummy.next

        