#
# My solution with some help from the internet
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # create a node called head
        head = ListNode()
        # pointer called current to point to current node
        current = head
        # if both lists are still there
        while list1 and list2:
            if list1.val < list2.val:
                # point at list 1
                current.next = list1
                # move list1 pointer
                list1 = list1.next
            else:
                # point at list 2
                current.next = list2
                # move list2 pointer
                list2 = list2.next
            # move current pointer regardless of which was true
            current = current.next
        
        # if lists are not same size we need to check
        if list1:
            current.next = list1
        else:
            current.next = list2

        # return the list next which points at the mergerd list
        return head.next



#
# LeetCode Answer
#

# The answer is the same in many places over the internet.