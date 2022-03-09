# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        dummy.next = head
        node = dummy
        while node.next and node.next.next:
            if node.next.val == node.next.next.val:
                v = node.next.val
                node.next = node.next.next.next
                while node.next and node.next.val == v:
                    node.next = node.next.next
            else:
                node = node.next
        return dummy.next