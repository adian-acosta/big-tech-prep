# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        # recursive solution

        if not list1 or not list2:
            return list1 or list2
        
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

        # iterative solution:

        #dummy = ListNode()
        #temp = dummy

        #while list1 and list2:
        #    if list1.val < list2.val:
        #        temp.next = list1
        #        list1 = list1.next
        #    else:
        #        temp.next = list2
        #        list2 = list2.next
            
        #    temp = temp.next
        
        #temp.next = list1 or list2
        #return dummy.next

# https://leetcode.com/problems/merge-two-sorted-lists/submissions/1624680983