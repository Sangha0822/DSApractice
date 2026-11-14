# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Plan is first reverse the lineked list. After we are giong to move up to 'n'th place.
        # after we are going to reconnect the linked list and revesrse it back with the new
        # linked list
        
        if not head.next:
            return None

        curr = head.next
        prev = head
        head.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        

        head = prev
        prev = None
        curr = head
        for i in range(n-1):
            prev = curr
            curr = curr.next

        if n == 1:
            head = head.next
        else:
            prev.next = curr.next

        curr = head.next
        prev = head
        head.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
