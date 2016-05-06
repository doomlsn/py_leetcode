# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None: return l2
        if l2==None: return l1
        output = ListNode(0)
        temp   = output
        flag   = 0
        while l1 and l2:
            temp.next =ListNode((l1.val+l2.val+flag) % 10)
            flag = (l1.val+l2.val+flag) / 10
            l1   = l1.next
            l2   = l2.next
            temp =temp.next
        #if l1:
        while l1:
            temp.next = ListNode((l1.val+flag) % 10)
            flag      = (l1.val+flag) / 10
            l1 = l1.next
            temp = temp.next
        #if l2:
        while l2:
            temp.next = ListNode((l2.val+flag) % 10)
            flag      = (l2.val+flag) / 10
            l2 = l2.next
            temp = temp.next
        if flag==1:
            temp.next=ListNode(1)
        return output.next
