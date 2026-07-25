# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next # storing the head of the second half
        slow.next = None # disconnecting the first and second halves

        #reversing

        # 0      1      2 - ..
        # sec   next  
        prev = None
        while second:
            next_node = second.next
            second.next = prev

            prev = second
            second = next_node
        
        # second becomes the head of the reversed list

        # 1   2 - 3
        #   5   4

        # 1 - 5 - 2
        second = prev
        first = head

        while first and second:
            next1 = first.next # saved
            first.next = second
            next2 = second.next
            second.next = next1

            first = next1
            #next1 = head.next
            second = next2
            #next2 = second.next
        

            

 
        



        