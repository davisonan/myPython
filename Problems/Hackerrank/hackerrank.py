#!/bin/python3

import sys

n = 262141

count = 0
maxCount = 0
while n > 0:
    digit = n % 2
    print(digit, end='')
    if digit == 1:
        count += 1
        # print(maxCount)
    else:
        if count > maxCount:
            maxCount = count
        count = 0
    n = n // 2
if count > maxCount:
    maxCount = count
print(maxCount)

###############################################################################
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class Solution(object):
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next
    def insert(self, head, data):
        current = head
        if current == None:
            current = Node(data)
            return current
        else:
            while current.next:
                current = current.next
            current.next = Node(data)
            return head

mylist = Solution()
list0 = [2, 3, 4, 1]
T = 4
head = None
for i in range(T):
    data = list0[i]
    head = mylist.insert(head, data)
mylist.display(head)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3

###############################################################################
class Calculator(object):
    def power(self, n, p):
        if n > 0 and p > 0:
            return n ** p
        else:
            print("n and p should be non-negative")

myCalculator=Calculator()
myCalculator.power(33, 5)

###############################################################################
def levelOrder(self,root):
    queue = [root] if root else []
    
    while queue :
        node = queue.pop()
        print(node.data, end=" ")
        
        if node.left  : queue.insert(0,node.left)
        if node.right : queue.insert(0,node.right)


###############################################################################
import math

def isPrime(n):
    if n == 2:
        return True
    elif n == 1 or (n & 1 == 0):
        return False
    else:
        for i in range(2, math.ceil(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

n = int(input())
list0 = [int(input().strip()) for i in range(n)]
for i in list0:
    if isPrime(i):
        print('Prime')
    else:
        print('Not prime')

isPrime(2)

###############################################################################
t = int(input().strip())
for _ in range(t):
    n , k = input().strip().split(' ')
    n , k = int(n) , int(k)
    print(k-1 if ((k-1) | k) <= n else k-2)

Instead of having to test various combinations of A & B, once can simply determine 
the result with knowledge of the value of the last digit of k.
Thought Process: Always strive to see if k-1 can be achieved, if not then try k-2 
and so on. This is because the maximum value less than k is k-1, but (k-1) will only be 
valid if it can be formed via A&B

(I) If k ends with 1, then the result is (k-1) In this case k-1 can always be formed by 
switching off the last digit of k, where k is .......1
(II) If k ends with 0, and is of form 2^m i.e. a power of 2 then result is (k-1) or (k-2). 
Let k=2^m If (2^m)-1 is in the range, then result is (k-1). In this case B=(2^m)-1 and 
A=k-1
else, result is (k-2). (k-2) is always guaranteed as it is the precursor of a binary number 
that ends with a 1, see (I)
(III) The last possible case is where k ends with 0, and is not a power of 2. Again the 
result is either (k-1) or (k-2)
If the number obtained by switching on the rightmost 1 of (k-1) is the range, then 
that number can be bitwise multiplied by k-1 to give (k-1). Otherwise result is (k-2). 
(k-2) is always guaranteed as it is the precursor of a binary number that ends with a 
1, see (I) & (II)

###############################################################################
5
5 3
-2 -1 0 1 2
6 4
-3 -1 0 3 1 0
4 4
-3 -1 0 -2
3 2
-2 -1 0
7 5
-2 -1 0 1 2 -3 -4

print('5')
print('5 3')
print('-2 -1 0 1 2')
print('6 4')
print('-3 -1 0 3 1 0')
print('4 4')
print('-3 -1 0 -2')
print('3 2')
print('-2 -1 0')
print('7 5')
print('-2 -1 0 1 2 -3 -4')

###############################################################################
a = [1, 2, 3, 4]
b = a[:]
a.pop(-1)
b.pop(0)

###############################################################################
def merge(left, right):
    rslt = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            rslt.append(left[i])
            i += 1
        else:
            rslt.append(right[j])
            j += 1

    if i < len(left):
        rslt.extend(left[i:])
    if j < len(right):
        rslt.extend(right[j:])

    return rslt

left = [1, 2, 5, 7]
right = [2, 3, 4, 8]
merge(left, right)
s0 = left + right

def mergeSort(s):
    if len(s) <= 1:
        return s
    else:
        n = len(s)
        mid = n//2
        left = mergeSort(s[:mid])
        right = mergeSort(s[mid:])
        return merge(left, right)

mergeSort(s0)
###############################################################################
def f():
    global var
    print(var)

def f2():
    global var
    var = 1
    f()

f2()

###############################################################################
arr = [0] * 36
def f(n):
    if n <= 2:
        arr[n] = n
        return arr[n]
    elif n == 3:
        arr[n] = 4
        return arr[n]
    else:
        if arr[n] != 0:
            return arr[n]
        else:
            arr[n] = f(n-1) + f(n-2) + f(n-3)
            return arr[n]

f(36)
