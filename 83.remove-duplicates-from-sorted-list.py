#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # pointer to the head node
        current = head;
        # while we have a node and the next of it
        while current and current.next:
            # if they have equal values
            if current.val == current.next.val:
                # set the next for the current to the next of next
                current.next = current.next.next
                # continue in case of repeated numbers
                continue
            # if no equal values, just move to next and keep comparing 
            current = current.next
        # finally, return the head
        return head
  
# @lc code=end

