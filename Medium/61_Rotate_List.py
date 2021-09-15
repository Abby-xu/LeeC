# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
      
      #check the length
        lastNode, length = head, 1
        while lastNode.next:
            lastNode = lastNode.next
            length += 1

        # check the number of rotation
        k = k % length

      # setlast node point to the first node
        lastNode.next = head

      #traverse until (length - k) node
        temp = head
        for i in range(length - k - 1): temp = temp.next

      #disconnect the first and last node
        out = temp.next
        temp.next = None

        return out
