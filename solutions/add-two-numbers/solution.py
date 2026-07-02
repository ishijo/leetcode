# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        sum_num = 0
        for curr in [l1,l2]:
            i = 1
            num = 0
            while curr:
                num += curr.val * i
                curr = curr.next
                i *= 10
            sum_num += num
        
        ll_vals = [int(str(sum_num)[i]) for i in range(len(str(sum_num))-1,-1,-1)]
        
        dummy = ListNode(0)
        tail = dummy

        for val in ll_vals:
            tail.next = ListNode(val)
            tail = tail.next

        return dummy.next


