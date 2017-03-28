#' % Data Structures
#' % Xu Tian
#' % 2017/03/14

#' # Data Structures
#' This is based on the course Udacity 513.

#' # Stacks
#' This is an abstract data structure. It can be implemented using 
#' other data structures. FIFO.

"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        if self.head:
            new_element.next = self.head
            self.head = new_element
        else:
            self.head = new_element

        # No need to check if self.head is None or not, because
        # if it's None, new_element.next = self.head will still
        # do the same thing. Need to think this through.
        # new_element.next = self.head
        # self.head = new_element

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        if self.head:
            tmp = self.head
            self.head = self.head.next
            return tmp
        else:
            return None

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first()
    
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop())
stack.push(e4)
print(stack.pop().value)


#' # Linked list
#' - How do you delete a node in a linked list?
#' - How do you reverse a linked list?
#' - How do you determine if a given linked list has a cycle in it?
#' - Given a singly linked list, determine if it is a palindrome?
#' - Remove all elements from a linked list of integers that have value val.
#' - Write a program to find the node at which the intersection of two singly linked lists begins.


#' # Queues
#' FILO, enqueue, dequeue.
#' Deques, priority_queue
#' 


