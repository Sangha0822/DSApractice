# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return None
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        l1 = head
        l2 = slow.next
        slow.next = None
        
        prev = l2
        l2 = l2.next
        prev.next = None
        while l2:
            temp = l2.next
            l2.next = prev
            prev = l2
            l2 = temp
        l2 = prev
        curr = head
        while l2:
        
            temp = l1.next
            curr.next = l2
            curr = curr.next
            l1 = temp

            temp = l2.next
            curr.next = l1
            curr = curr.next
            l2 = temp
        
