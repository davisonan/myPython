#' % Problems related to linked lists
#' % Xu Tian
#' % 2017/03/20

#' # Background
#' This document contains the major issues about a linked list including
#' designing a well behaved linked list class with many more member methods than
#' an ordinary linked list class would have. These member methods are ususally
#' coming from problems on leetcode about linked lists.

#' # List Node class
#' The linked list is a list of linked nodes where each node is an instance of
#' the following Node class.

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

#' The getters in the following class definition is really unnecessary since
#' in Python, the value attributes are not private and can be accessed outside
#' of the class directly, although the string representation is needed to have
#' a better visual of the node.
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

#' This is the LinkedList class. The initiater is standard, however, the member
#' methods are somehow always customized depending upon the needs. Usually
#' interview problems will split functionalities of this class into
#' subproblems, but once they are better orgnized, you'll see these problems
#' are really just fundamental in data structurs.

#' The following code is the correct version because if cur is None,
#' then the previous node could refer to this newNode since the previous
#' node's next pointer is still pointing to None.

#' The following code is the definition of a LinkedList class with the following
#' member methods:

#' - __init__:
#' - __len__:
#' - append:
#' - getAt:
#' - insert:
#' - delete:
#' - deleteAll:
#' - reverse:
#' - printForward:
#' - printBackward:
#' - isPalindrome:
#' - sort:
#' - hasCycle:
#' - getRandomNode:

import random
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, newNode):
        """Append a new node at the end of the list."""
        self.length += 1
        cur = self.head
        if cur:
            while cur.next: cur = cur.next
            cur.next = newNode
        else:
            self.head = newNode

    def getAt(self, pos):
        """Get an element from a particular position.
        Assume the first position is 0.
        Return "None" if position is not in the list."""
        if pos < 0: return None
        curPos, cur = 0, self.head
        while cur and curPos != pos:
            curPos, cur = curPos + 1, cur.next
        if cur and curPos == pos: return cur
        if cur is None: raise IndexError("No value at Position {}.".format(pos))

    def insert(self, newNode, pos):
        """Insert a new node at the given position.
        Inserting at position 2 means between
        the 2nd and 3rd elements."""
        self.length += 1
        if pos == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            curPos, cur = 0, self.head
            while cur and curPos+1 != pos:
                cur, curPos = cur.next, curPos + 1
            if cur and curPos+1 == pos:
                newNode.next = cur.next
                cur.next = newNode

    def delete(self, val):
        """Delete the first node with a given value."""
        cur = self.head
        self.length -= 1
        if cur and cur.val == val: self.head = cur.next
        while cur and cur.next and cur.next.val != val:
            cur = cur.next
        if cur and cur.next and cur.next.val == val:
            cur.next = cur.next.next

    def deleteAll(self, val):
        """Delete all the nodes with a given value."""
        dummy = Node(-1)
        dummy.next = self.head
        cur = dummy
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
                self.length -= 1
            else:
                cur = cur.next
        self.head = dummy.next

    def reverse(self):
        """Reverse the linked list."""
        prev = None
        while self.head:
            curr = self.head
            self.head = self.head.next
            curr.next = prev
            prev = curr
        self.head = prev

    def reverseBetween(self, m, n):
        """Reverse the linked list between m and n"""
        


    def printForward(self):
        """Print the nodes' values forwards recursively.
            f() is a wrapper function for recursive calls.
        """
        def f(list):
            if list:
                print(list.val, end=' ')
                f(list.next)
        curr = self.head
        f(curr)
        print()

    def printBackward(self):
        """Print the nodes' values backwards recursively.
            g() is a wrapper function for recursive calls.
        """
        def g(list):
            if list:
                g(list.next)
                print(list.val, end= ' ')
        curr = self.head
        g(curr)
        print()

    def isPalindrome(self):
        """Return True if the linked list forms a palindrome."""
        return True

    def sort(self):
        """Sort the linked list"""
        pass

    def hasCycle(self):
        """Return True if there's a cycle in the LinkedList."""
        if not (self.head or self.head.next): return False
        slow = fast = self.head
        # only need to monitor fast pointer for the following two nodes.
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast: return True
        else:
            return False

    def getCycleBeginAt(self):
        """Get the start position of a cyle if there's any.
        Return None if there's no cycle.
        """
        if not (self.head and self.head.next): return None
        slow = fast = self.head
        # only need to monitor fast pointer for the following two nodes.
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                slow = self.head
                while slow is not fast:  # Monitor if slow is fast.
                    slow = slow.next
                    fast = fast.next
                else:
                    return slow
        else:
            return None

    def getRandomNode(self):
        """Return the value of a random node chosen with equal probabilities."""
        count, rslt = 1, None
        cur = self.head
        while cur:
            if random.randint(1, count) == 1:  # Important: inclusive.
                rslt = cur
            count, cur = count + 1, cur.next
        return rslt.val

    def oddEvenReorder(self):
        """Reorder the linkedlist with nodes at odd positions first and followed
        by nodes at even positions. The relative order of odd nodes and even nodes
        should be maintained."""
        if self.head and self.head.next:
            curOdd = self.head
            headEven, curEven = self.head.next, self.head.next
            while curOdd and curEven and curOdd.next and curEven.next:
                curOdd.next = curEven.next
                curOdd = curOdd.next
                curEven.next = curOdd.next
                curEven = curEven.next
            curOdd.next = headEven
        return self.head

def main():
    import random
    ll = LinkedList()
    nNodes = 100
    for i in range(nNodes):
        ll.append(Node(random.randint(0, 10)))
    ll.reverse()
    for i in range(5):
        print(ll.getAt(i).val, ll.getAt(nNodes-i-1).val)
    ll.append(Node(1))
    ll.append(Node(2))
    ll.append(Node(3))
    len(ll)
    ll.getAt(1).val
    ll.insert(Node(2.3), 1)
    ll.getAt(1).val
    len(ll)
    ll.append(Node(3))
    ll.append(Node(3))
    ll.append(Node(3))
    ll.append(Node(3))
    ll.reverse()
    ll.deleteAll(2)
    len(ll)
    ll.deleteAll(3)
    len(ll)
    [ll.getAt(i).val for i in range(len(ll))]

if __name__ == '__main__':
    main()

#' # Misunderstandings and mistakes
#' Many concepts if not understood well can lead to mistakes. This section
#' emphasizes the concepts or points that I made mistakes about or had
#' misunderstandings. In linked list, it seems a well-known trick to use a
#' dummy variable to point to the beginning of the linked list.


# if cur:
#     while cur:
#         cur = cur.next
#     cur = newNode
# else:
#     self.head = newNode

#' # List and linked List
#' List is implemented as an array. The proof is indexing takes constant time
#' regardless of the length of the list, however, a linked list would take
#' the time proportional to the length of the linked list. However though,
#' a list does have the characteristics of a list, taking different types of
#' objects, etc. The pointers are allocated with the same amount of memory,
#' but the objects the pointers point to can be different, in CPython.

#' These are the three ways of simulating for random nodes I've tried. The first
#' one didn't pass all the test cases on leetcode. The second one is not correct
#' either, the third one is the correct solution. The difference between the 2nd
#' and 3rd is random.randint(a, b) returns an integer including a and b, however
#' there's another function randint(a, b) by default in Python returning an
#' an integer not including b. The first one should work and does work, however,
#' it could pass the tests. I still wonder why.

import random
def runSim():
    rslt = None
    for i in range(1, 100):
        if random.random() < 1/i:
            rslt = i
    return rslt

rslts = Counter([runSim() for _ in range(100000)])

import random
for i in range(1, 1000):
    if random.randint(0, i) == 0:
        print(i)

import random
for i in range(1, 1000):
    if random.randint(1, i) == 1:
        print(i)

#' I always have a little trouble in deciding the monitoring rules in while
#' loops etc. The condition in while loops. There must be a set of rules to tell
#' how we can come up with the while conditions.

#' # How do we decide on conditions in a while loop?
#' If I don't know what to put in the condition first, put True and keep writing
#' until a point you'll have to write conditions to break out of the while loop.
#' That very condition is what you'll need to put as the condition in the while
#' loop.
