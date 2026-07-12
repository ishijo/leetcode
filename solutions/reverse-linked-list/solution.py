# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        prev = None ## 3
        while curr: ## 4
            org_next = curr.next ## org_next is 5
            curr.next = prev ## curr's next is None
            #org_next.next = curr ##
            prev = curr
            curr = org_next ##

        return prev

        