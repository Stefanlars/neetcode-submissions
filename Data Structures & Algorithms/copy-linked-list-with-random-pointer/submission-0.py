"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Two passes. First build the intial linked list
        # Use a hm to store pointers to nodes based on their index
        if not head: 
            return None

        hm = {}


        prev = Node(-1)
        dummy = prev
        

        while head:
            if head.random and head.random not in hm:
                hm[head.random] = Node(head.random.val)
            

            if head not in hm:
                curr = Node(head.val)

                hm[head] = curr
                
            else:
                curr = hm[head]
            
            if head.random:
                curr.random = hm[head.random]

            prev.next = curr

            prev = prev.next
            head = head.next


        return dummy.next

