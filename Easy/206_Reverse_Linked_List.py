# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None or head.next == None): return head
        
        list_to_re = head.next
        
        re_list = head
        re_list.next = None
        
        while list_to_re != None:
            temp = list_to_re
            list_to_re = list_to_re.next
            
            temp.next = re_list
            re_list = temp
        
        return re_list
