# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1=list1
        cur2=list2
        if cur1 is None and cur2 is None:
            return None
        if cur1 is None:
            return cur2
        if cur2 is None:
            return cur1
        startnode=ListNode(-1)
        tail=startnode
        while cur1 and cur2:
            if cur1.val<cur2.val:
                tail.next=cur1
                tail=tail.next
                cur1=cur1.next
            else:
                tail.next=cur2
                tail=tail.next
                cur2=cur2.next
        if cur1:
            tail.next=cur1
        else:
            tail.next=cur2
        return startnode.next
            
        