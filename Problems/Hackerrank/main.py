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

