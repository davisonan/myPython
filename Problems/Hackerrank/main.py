###############################################################################
##### Useful functions
print(locals())
print(globals())

# input() can read in the end-of-line character, which when compared with a string, 
# may not be equal.

###############################################################################
##### Useful functions
for i in zip([1,2,3,4,5,6], 'Hacker'):
    print(i)

for i in zip([1,2,3,4,5,6], [0,9,8,7,6,5,4,3,2,1]):
    print(i)

A = [1,2,3]
B = [6,5,4]
C = [7,8,9]
X = [A] + [B] + [C]

for i in zip(*X):
    print(i)


eval('9 + 5')

N, M = map(int, input().split())
rows = [input() for _ in range(N)]
K = int(input())

for row in sorted(rows, key=lambda row: int(row.split()[K])):
    print(row)

print(*[1, 3, 4], sep='')

Sorting1234

print(*sorted(input(), key=lambda c: (-ord(c) >> 5, c in '02468', c)), sep='')

print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')

order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
print(*sorted(input(), key=order.index), sep='')

import string
print(*sorted(input(), key=(string.ascii_letters + '1357902468').index), sep='')


# The map() function applies a function to every member of an iterable and returns the result.
# Lambda functions cannot use the return statement and can only have a single expression. 
# Unlike def, which creates a function and assigns it a name, lambda creates a function 
# and returns the function itself. Lambda can be used inside lists and dictionaries.
n=5
a,b=0,1
c=[]

for i in range(n):
    c.append(a)
    a,b=b,a+b


l = list(range(10))
l = list(map(lambda x:x*x, l))
l = list(filter(lambda x: x > 10 and x < 80, l))




from itertools import product
print(list(product([1,2,3],repeat = 2)))
print(list(product([1,2,3],[3,4])))
print(list(product(*A)))
B = [[1,2,3],[3,4,5],[7,8]]
print(list(product(*B)))


class Complex(object):
    def __init__(self, a, b):
        self.re = float(a)
        self.img = float(b)
    def __add__(self, other):
        return Complex(self.re+other.re, self.img+other.img)
    def __sub__(self, other):
        return Complex(self.re-other.re, self.img-other.img)
    def __mul__(self, other):
        return Complex(self.re*other.re-self.img*other.img, self.re*other.img+self.img*other.re)
    def __truediv__(self, other):
        try:
            real = self.re*other.re+self.img*other.img
            img = self.img*other.re-self.re*other.img
            divisor = other.re**2 + other.img**2
            return Complex(real/divisor, img/divisor)
        except ZeroDivisionError:
            raise Exception("Divided by a zero complex number.")
    def mod(self):
        return Complex(sqrt(self.re**2+self.img**2), 0)
    def __str__(self):
        sign = '+' if self.img >=0 else '-'
        return '{:.2f}'.format(self.re) + sign + '{:.2f}'.format(abs(self.img)) + 'i'

c1 = Complex(-1, -2)
c2 = Complex(0, 1)

print(c1)
print(c2)
print(c1/c2)
print(c1.mod())


###############################################################################
##### Class 2 - Find the Torsional Angle
from math import sqrt
from math import acos
from math import pi
class Vector(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y, self.z+other.z)
    def __sub__(self, other):
        return Vector(self.x-other.x, self.y-other.y, self.z-other.z)
    def dotProd(self, other):
        return self.x*other.x+self.y*other.y+self.z*other.z
    def norm(self):
        return sqrt(self.x**2+self.y**2+self.z**2)
    def crossProd(self, other):
        first = self.y*other.z - self.z*other.y
        second = self.z*other.x - self.x*other.z
        third = self.x*other.y - self.y*other.x        
        return Vector(first, second, third)
    def __str__(self):
        return "Point: {}, {}, {}".format(self.x, self.y, self.z)
la = list(map(float, input().split()))
A = Vector(la[0], la[1], la[2])
lb = list(map(float, input().split()))
B = Vector(lb[0], lb[1], lb[2])
lc = list(map(float, input().split()))
C = Vector(lc[0], lc[1], lc[2])
ld = list(map(float, input().split()))
D = Vector(ld[0], ld[1], ld[2])
AB = B-A
BC = C-B
CD = D-C
X = AB.crossProd(BC)
Y = BC.crossProd(CD)
num = X.dotProd(Y)
den = X.norm()*Y.norm()
ang = acos(num/den)/pi*180
print('{:.2f}'.format(ang))

###############################################################################
##### Time Delta
from datetime import datetime as dt

fmt = '%a %d %b %Y %H:%M:%S %z'
for i in range(int(input())):
    print(int(abs((dt.strptime(input(), fmt) - 
                   dt.strptime(input(), fmt)).total_seconds())))

###############################################################################
##### Closures
def outer():
    x = 1
    def inner():
        print(x)
    return inner
foo = outer()
dir(foo)  # list all attributes
foo.__closure__

##### Decorators
def outer(some_func):
    def inner():
        print("before some_func")
        ret = some_func() # 1
        return ret + 1
    return inner
def foo():
    return 1
decorated = outer(foo) # 2
decorated()


###############################################################################
##### Collections->Collections.namedtuple()
from collections import namedtuple
N, Grade = int(input()), namedtuple('Grade', input().strip())
Avg = sum([float(Grade(*input().split()).MARKS) for _ in range(N)])/N
print('{:.2f}'.format(Avg))

###############################################################################
##### Collections->Most Common
import operator
s, d = input().strip(), {}
for c in s:
    d[c] = d.get(c, 0) - 1
sorted_d = sorted(d.items(), key=operator.itemgetter(1, 0))
for i in range(3):
    print(sorted_d[i][0], -sorted_d[i][1])

from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
[print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]

###############################################################################
##### Collections->Piling Up!
for t in range(input()):
    input()
    lst = map(int, raw_input().split())
    l = len(lst)
    i = 0
    while i < l - 1 and lst[i] >= lst[i+1]:
        i += 1
    while i < l - 1 and lst[i] <= lst[i+1]:
        i += 1
    print("Yes" if i == l - 1 else "No")

###############################################################################
##### Regex and Parsing->

###############################################################################
##### args
def one(*args):
    print(args)

def add(x, y):
    return x + y
lat=[1,2]
add(*lat)

def foo(**kwargs):
    print(kwargs)
foo()
foo(x=1, y=2)

def Func(*args, **kwargs):
    for arg in args:
        print(arg)
    for item in kwargs.items():
        print(item)
Func(12, 13, x=1, y=2)   # positional argument follows keyword argument

###############################################################################
##### Closures and Decorators->Standardize Mobile Number Using Decorators
l = [input() for _ in range(int(input()))]

def wrapper(f):
    def phone(l):
        f(["+91 "+c[-10:-5]+" "+c[-5:] for c in l])
    return phone

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

sort_phone(l)

###############################################################################
##### Closures and Decorators->Standardize Mobile Number Using Decorators

def addOne(myFun):
    def g():
        return myFun() + 1
    return g

@addOne
def foo():
    return 3

foo()



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
