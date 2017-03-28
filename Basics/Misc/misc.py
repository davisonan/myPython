#' % Miscellaneous
#' % Xu Tian
#' % 2017/03/14

#' # Landau notation
#' $O$, $\Omega$, $\Theta$ represents the worst, best and average speed of 
#' growth of computations with respect to the sample size $n$. Read this [post](http://cs.stackexchange.com/questions/57/how-does-one-know-which-notation-of-time-complexity-analysis-to-use)
#' for a clear explantion.

#' # Big O notation
#' Big O specifically describes the worst-case scenario, and can be used to 
#' describe the execution time required or the space used (e.g. in memory or on 
#' disk) by an algorithm. This is why it's also said "big-O uppper bound runtime
#' for a function".

#' The worst case here means the algorithm runs in the worst possible scenario,
#' i.e., for a sorting algorithm, the worst case is the array is sorted in the 
#' reversed order, for a binary searching algorithm, the worst case is the 
#' target number is located at the last step of the binary search instead of 
#' right in the middle or at the index of exactly divisible by the power of 2.
#' This is the actual meaning of worst case.

#' The worst cases, the average cases and the best cases can differ 
#' dramatically because of the constant multiplier.

#' # List and linked List
#' List is implemented as an array. The proof is indexing takes constant time
#' regardless of the length of the list, however, a linked list would take 
#' the time proportional to the length of the linked list. However though, 
#' a list does have the characteristics of a list, taking different types of 
#' objects, etc. The pointers are allocated with the same amount of memory, 
#' but the objects the pointers point to can be different, in CPython.


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    def append(self, newNode):
        cur = self.head
        if self.head:
            while cur.next:
                cur = cur.next
            cur.next = newNode
        else:
            self.head = newNode

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    
    def append(self, new_element):
        cur = self.head
        if self.head:
            while cur.next:
                cur = cur.next
            cur.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        if position < 1:
            return None
        else:
            curPos = 1
            cur = self.head
            while cur and curPos != position:
                curPos += 1
                cur = cur.next
            if cur and curPos == position:
                return cur
            if cur is None:
                return None
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        if position == 1:
            new_element.next = self.head
            self.head = new_element
        if position > 1:
            curPos = 1
            cur = self.head
            while cur and curPos + 1 != position:
                curPos += 1
                cur = cur.next
            if cur and curPos + 1 == position:
                new_element.next = cur.next
                cur.next = new_element
    
    def delete(self, value):
        """Delete the first node with a given value."""
        if self.head.value == value:
            self.head = self.head.next
        cur = self.head
        while cur and cur.next and cur.next.value != value:
            cur = cur.next
        if cur and cur.next and cur.next.value == value:
            cur.next = cur.next.next
        
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

# Test insert
ll.insert(e4,3)
# Should print 4 now
print ll.get_position(3).value

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value


#' # Resorvior sampling
#' Resorvior sampling is a sampling method for streaming of data. For a 
#' sample of $n$ data points in the stream, the probability that each point
#' is sampled is equivalent.

import random
from collections import Counter

def rsampling(arr):
    n = len(arr)
    x = arr[0]
    for i in range(1, n):
        p = random.random()
        x = arr[i] if p < 1/(i+1) else x
    return x

arr = [5, 2, 4, 6, 1, 3]
rsampling(arr)

rslt = [rsampling(arr) for _ in range(10000)]
print(Counter(rslt))

def rksampling(arr, k):
    rslt = arr[:k]  # The first k elements in list rslt
    for i in range(k, len(arr)):  # Iterate from k to n
        j = random.randint(0, i)  # sample integer from 0 to i, inclusive
        if j < k:  # if the integer is in the first k values
            rslt[j] = arr[i]  # update
    return rslt

arr = [5, 2, 4, 6, 1, 3]
rksampling(arr, 2)
rslt = [rksampling(arr, 2) for _ in range(100000)]
rslt = [i[0] for i in rslt] + [i[1] for i in rslt]
print(Counter(rslt))


#' # Palindrome
#' Palindrome is an interesting phenomena that a string or an interger
#' is the same with its reversed version. The following chunks of code 
#' give three versions of string palindrome algorithms and one integer
#' algorithm.

# String efficient recursive
def isPalindrome1(x):
    if len(x) <= 1:
        return True
    return x[0] == x[-1] and isPalindrome1(x[1:-1])

# String efficient recursive
def isPalindrome2(x, start, end):
    if start > end:
        return True
    return x[start] == x[end] and isPalindrome2(x, start+1, end-1)

# String loop
def isPalindrome3(x):
    i, j = 0, len(x)-1
    while i < j:
        if x[i] != x[j]:
            return False
        i += 1
        j -= 1
    return True

s0 = "HelloworlddlrowolleH"
print(isPalindrome1(s0))
print(isPalindrome2(s0, 0, len(s0)-1))
print(isPalindrome3(s0))

#' The palindrome can also happen on integers, however, the exact 
#' algorithm is slightly different. 
# Palindrome integer 
def isPalindrome(x):
    div = 1
    while x // div >= 10:
        div *= 10
    while x > 0:
        l = x // div
        r = x % 10
        if l != r: return False
        x = (x % div) // 10
        div //= 100
    return True

isPalindrome(101010101010101010101)
%timeit isPalindrome(101010101010101010101)


#' # Shuffling
#' This chunk of code is from leetcode.

for i in range(len(ans)-1, 0, -1):     # start from end
    j = random.randrange(0, i+1)    # generate random index 
    ans[i], ans[j] = ans[j], ans[i]    # swap

#' Another exercise was from a video on Udacity.



#' # Combinations
#' This chunk of code is for algorithms generating all combinations of an 
#' array.


#' # Class inheritance
class parent(object):
    def __init__(self, param):
        self.v1 = param
class child(parent):
    def __init__(self, param):
        self.v2 = param

obj = child(5)
# __init__ is overwritten, therefore, self.v1 never exists.
print(obj.v1, obj.v2)


