#' % Problems related to linked lists
#' % Xu Tian
#' % 2017/03/20

#' # Background
#' This writeup consists of the tree-based problems in leetcode.

#' In linked list, it seems a stnadard approach to use a dummy variable to
#' point to the beginning of the linked list.

#' # List Node class
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def getVal(self):
        return self.val
    def getNext(self):
        return self.next
    def __str__(self):
        return "Node {}, next is {}".format(self.val, self.next)

ln0 = ListNode(1)
ln1 = ListNode(2)

# 203. Remove Linked List Elements
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val: head = head.next
        if head:
            start = head
            while head.next:
                if head.next.val == val:
                    head.next = head.next.next if head.next.next else None
                else:
                    head = head.next
            return start
        else:
            return None

sol = Solution()
sol.removeElements(ln0, 1)


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next

# 160. Intersection of Two Linked Lists
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not (headA and headB): return None
        pa, pb = headA, headB
        while pa != pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next
        return pa
