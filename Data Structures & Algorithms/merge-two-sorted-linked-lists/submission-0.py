# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummyCurr = dummy
        curr1, curr2 = list1, list2
        while curr1 or curr2:
            print("BEFORE:")
            print("curr1:", curr1.val if curr1 else None)
            print("curr2:", curr2.val if curr2 else None)
            print("dummyCurr:", dummyCurr.val)
            # if both lists are not done yet:
            if curr1 and curr2:
                if curr1.val < curr2.val:
                    dummyCurr.next = curr1
                    dummyCurr = dummyCurr.next
                    curr1 = curr1.next
                else:
                    dummyCurr.next = curr2
                    dummyCurr = dummyCurr.next
                    curr2 = curr2.next                       
            # if list1 is not done yet:
            elif curr1:
                dummyCurr.next = curr1
                dummyCurr = dummyCurr.next
                curr1 = curr1.next
            # if list 2 is not done yet:
            elif curr2:
                dummyCurr.next = curr2
                dummyCurr = dummyCurr.next
                curr2 = curr2.next
            print("AFTER:")
            print("dummyCurr.next:", dummyCurr.next.val if dummyCurr.next else None)
            print("curr1:", curr1.val if curr1 else None)
            print("curr2:", curr2.val if curr2 else None)
            print("--------------------")
        return dummy.next