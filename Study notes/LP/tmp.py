# tmp.py

import pandas_datareader.data as web
import pandas as pd
import matplotlib.pyplot as plt
import datetime

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime.today()
f = web.DataReader("F", 'yahoo', start, end)

t = f.index
y = f['Adj Close']
plt.figure()
plt.plot(t, y, '.')
plt.xlabel('Date')
plt.ylabel('Price')

r = log(y).diff()
plt.plot(r)

r.plot.hist(alpha=0.5, bins=100)

RPP1=sum(rev)/sum(pv)
RPP2=average(RPP1_User)

# sampling distribution

#####
def convertFun(time):
    if time[-2:]=='AM':
        if time == '12:00:00AM':
            print('00:00:00')
        else:
            print(time[:-2])
    else:
        print(str(int(time[:2])+12)+time[2:-2])

time1 = '07:05:45PM'
time2 = '00:00:00AM'
time3 = '12:00:00PM'
convertFun(time1)
convertFun(time2)
convertFun(time3)

#####
n,k,q = 3,2,3
a = [1, 2, 3]
k = k % n
b = a * 2
for m in [0,1,2]:
    print(b[n-k+m])

#####
l = [1,2,3,4,5]
from itertools import combinations
for i in combinations(l, 4):
    print(i)


#####
def red(s):
    n = len(s)
    if n == 0:
        return "Empty String"
    else:
        flag = False
        for i in range(n-1):
            if s[i] == s[i+1]:
                s = s[:i] + (s[i+2:] if i+2 <= n-1 else '')
                flag = True
                break
        if flag:
            return red(s)
        else:
            return s

s = 'aaabccddd'
red(s)
s = 'baab'
red(s)
s = 'aa'
red(s)

#####

S = 'SOSSPSSQSSOR'
n = 0
for i in range(len(S)):
    if (i % 3 == 0 or i % 3 == 2) and S[i] != 'S':
        n += 1
    elif i % 3 == 1 and S[i] != 'O':
        n += 1
print(n)


n=int(input().strip())
def f(S):
    l = list(map(ord, S))
    for i in range(1, len(l)):
        print(l[i], l[i-1], l[n-i-1], l[n-i])
        if abs(l[i] - l[i-1]) != abs(l[n-i-1] - l[n-i]):
            return False
    return True

S = 'acxz'
f(S)
S = 'bcxz'
f(S)


##### Caesar Cipher
# Method 1: Use string
# Method 2: Use index only


#####
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)

#####
import os
_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')

a, b, *rest = range(5)
a, b, *rest = range(4)
a, b, *rest = range(3)
a, *body, c, d = range(5)
*head, b, c, d = range(5)

l = list(range(10))
l[2:5] = [10, 20]
l
l[4:9] = 10

#####
l = [1, 2, 3]
id(l)
l *= 2
id(l)
t = (1, 2, 3)
id(t)
t *= 2
id(t)

t = (1, 2, [30, 40])
t[2] += [50, 60]
t

fruits = ['grape', 'apple', 'banana', 'raspberry']
sorted(fruits, key=len)  # 'apple' and 'grape' are kept the original order


#####
import bisect, sys
HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}   {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))


demo(bisect.bisect)

#####
import bisect
import random

SIZE = 7

random.seed(1234)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE * 2)
    bisect.insort(my_list, new_item)
    print('%2d ->' %new_item, my_list)


#####
import array
numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
len(memv)
memv[0]
memv_oct = memv.cast('B')
memv_oct
memv_oct.tolist()
memv_oct[5] = 4
numbers

#####
import numpy
a = numpy.arange(12)
a
type(a)
a.shape
a.shape = 3, 4
a
a[2]
a[2, 1]
a[:, 1]
a.transpose()


#####
from fractions import Fraction
from functools import reduce
n1 = Fraction(1, 2)
n2 = Fraction(3, 4)
n3 = Fraction(10, 6)
fracs = [n1, n2, n3]

def product(fracs):
    nums = [i.numerator for i in fracs]
    dens = [i.denominator for i in fracs]
    num = reduce(lambda x, y: x * y, nums)
    den = reduce(lambda x, y: x * y, dens)
    t = Fraction(num, den)
    return t.numerator, t.denominator

result = product(fracs)
print(*result)

reduce(lambda x, y: x.numerator * y.numerator, fracs)
reduce(lambda x, y: x.denominator * y.denominator, fracs)

s='hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwflvsgygh'
i, j = 0, len(s)-1
idx = -1
while i < j:
    if s[i] != s[j]:
        if s[i+1] == s[j]:
            idx = i
            break
        elif s[i] == s[j-1]:
            idx = j
            break
    i += 1
    j -= 1
print(idx)

#####



a to the four where supers i be the other four

wordDict = {}
charDict = {l:0 for l in 'abcdefghijklmnopqrstuvwxyz'}
line = input().strip()
while line:
    words = [word.strip().lower() for word in line.split()]
    for word in words:
        wordDict[word] = wordDict.get(word, 0) + 1
        for char in word:
            if char.isalpha():
                charDict[char] += 1
    
    line = input().strip()

print(sum([val for val in wordDict.values()]))
print("words")
for word in sorted(wordDict.keys()):
    print('%s %s' %(word, wordDict[word]))
print("letters")
for char in sorted(charDict.keys()):
    print('%s %s' %(char, charDict[char]))

import re
DATA = "Hey, you - what are you doing here!?"
l = re.findall(r"[\w']+", DATA)

line = 'a to the four where supers i be the other four'
for word in re.findall(r"[\w']+", line):
    print(word)

##### sorted can sort a dictionary by key by default
##### But this is losing some readability than sorted(d.keys())
d = {'a':1, 'b':3, 'c':2, 'd':5}
for i in sorted(d):
    print(i, '=>', d[i])

#####
0o1, 0o20, 0o377  # oct
0x01, 0x10, 0xFF  # hex
0b1, 0b10000, 0b11111111  # bin

64, 0o100, 0x40, 0b1000000
int('64'), int('100', 8), int('40', 16), int('1000000', 2)
int('0x40', 16), int('0b1000000', 2)


x = 0xFF
x ^ 0b10101010  # bitwise XOR, either but not both
x=99
bin(x), x.bit_length(), len(bin(x))-2

from decimal import Decimal
Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3)

from fractions import Fraction
x=Fraction(1, 3)
y=Fraction(4, 6)
x
y
print(y)

x+y
x-y
x*y
x/y

Fraction('.25')
Fraction('1.25')
Fraction('.25') + Fraction('1.25')

(2.5).as_integer_ratio()
f = 2.5
z = Fraction(*f.as_integer_ratio())
{1, 2, 3}.issubset(range(-5, 5))


isinstance(True, int)

True == 1
True == 1.0
True == 2
True is 1
True + 4

######
# dynamic typing
a = 3
b = a
sys.getrefcount(0)  # count the references to object 0.

######
s = '0123456789'
s[5:1:-1]

'spam'[1:3]
'spam'[slice(1, 3)]
'spam'[::-1]
'spam'[slice(None, None, -1)]

######
x = 1234
res = 'integers: ...%d...%-6d...%06d' %(x, x, x)
res

x = 1.234567890
'%e | %E | %f | %g' %(x, x, x, x)
'%-6.2f | %05.2f | %+06.1f' %(x, x, x)

'%f, %.2f, %.*f' %(1/3.0, 1/3.0, 5, 1/3.0)

'%(qty)d more %(food)s' % {'qty': 1, 'food': 'spam'}

food = 'spam'
qty = 10
vars()
'%(qty)d more %(food)s' % vars()

import sys
'My {1[kind]} runs {0.platform}'.format(sys, {'kind': 'laptop'})
'My {map[kind]} runs {sys.platform}'.format(sys=sys, map={'kind': 'laptop'})
'{:>10} = {:<10}'.format('spam', 123.4567)

'{.platform:>10} = {[kind]:<10}'.format(sys, dict(kind='laptop'))
'{0.platform:>10} = {1[kind]:<10}'.format(sys, dict(kind='laptop'))

'{0:d}'.format(9999999999999)
'{0:,d}'.format(9999999999999)
'{:,.2f}'.format(2340.340392843)

from formats import commas, money
'%s' % commas(000000000)

##### Chp 8

#####
d=[(1, 'a'), (2, 'a'), (3, 'b'), (4, 'b')]
for key, items in groupby(d, itemgetter(1)):
    print(key)
    for subitem in items:
        print(subitem[0])
    print('_' * 20)

with open('word.txt', 'r') as f:
    wordSet = {line.strip() for line in f}
wordDict = defaultdict(set)
for word in wordSet:
    wordDict[len(word)].add(word)

##### Chp 8
L = [1, 2, 3]
L[1:2] = [4, 5]  # replace
L
L[1:1] = [6, 7]  # insertion
L
L[1:2] = []  # deletion
L


L = [1]
L[:0] = [2, 3, 4]
L[len(L):] = [5, 6, 7]
L
L.extend([8, 9, 10])
L


L + [1]
L.append(1)


[1, 2, 'spam'].sort()

d ={'a': 1, 'b': 2}
for k in d:  # It's equivalent with d.keys()
    print(k)
for k in d.keys():
    print(k)

l = (1, [2, 3], 4)
l[1] = 'spam'  # Only top-level immutability
l[1][0] = 'spam'  # This does work. 


None == False  # False
None is False  # False
if not None: print("True")  # not None is evaluated to be True
dir(None)
sys.getrefcount(None)
None.__bool__()  # This is False

dir(1)
(1).__bool__()
dir(2)
(2).__bool__()
dir(0)
(0).__bool__()
dir(-1)
(-1).__bool__()
dir(1.24)
(1.24).__bool__()


S = 'spam'
S[:0]

S = "SPAM"
S[0][0][0][0][0][0][0]

S = ['S', 'P', 'A', 'M']
S[0][0][0][0][0][0][0]

L = [0, 1, 2, 3]
L[4]  # IndexError
L[-1000:100]  # Not an error!
L[3:1] = ['?']  # 

[0, 1, 2, 3, 4, 5][3]
[0, 1, 2, 3, 4, 5][3:4]


L = []
L += 'SPAM'
L

L = []
L = L + 'SPAM'
L


L = [1, 2]
M = L
L = L + [3, 4]  # + creats a new object
(L, M)

L = [1, 2]
M = L
L += [3, 4]  # += calls .extend, make in-place change
(L, M)


x = 'spam'
y = 99
z = ['eggs']
print(x, y, z, sep='...', end='!\n')
print(x, y, z, sep='...', file=open('data.txt', 'w'))


import sys
sys.stdout.write("Hello world\n")


2 or 3, 3 or 2
[] or 3
[] or {}

2 and 3, 3 and 2
[] and 3
[] and {}


i = 5
while i < 10:
    print(i)
    i += 1
else:
    print("haha", i)


def f(): pass
def f(): ...

X = ...


### 
M = map(lambda x: 2 ** x, range(3))
for i in M: print(i)
for i in M: print(i)  # One pass only, the second iteration wouldn't work.

D = {'a': 1, 'b': 2, 'c': 3}
for k in sorted(D): print(k, D[k], end=' ')  # "Best practice" key sorting

###
y, z = 1, 2
def f():
    global x
    x = y + z
f()  # This would create x in the global scope
print(x)

###

def kwonly(a, *, b, c):
    print(a, b, c)
kwonly(1, c=3, b=2)
kwonly(c=3, b=2, a=1)
kwonly(1, 2, 3)
kwonly(1)

def kwonly(a, **, b, c): print(a, b, c)
def kwonly(a, **pargs, b, c): print(a, b, c)

def func(a, b=4, c=5):
    print(a, b, c)
func(1, 2)

def func(a, *pargs):
    print(a, pargs)
func(1, 2, 3)

def func(a, **kargs):
    print(a, kargs)
func(a=1, b=2, c=3)

def func(a, b, c=3, d=4): print(a, b, c, d)
func(1, *(5, 6))

def mysum(L):
    return 0 if not L else L[0] + mysum(L[1:])

mysum([1,2,3,4,5])

## Sum of items in nested lists
def sumtree(L):
    tot = 0  # tot of each branch starts at 0
    for x in L:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot

L = [1, [2, [3, 4], 5], 6, [7, [[[8]]]]]
sumtree(L)

import sys
sys.getrecursionlimit()

# Generators are single-iteration objects
# Built-in data types support multiple iterators and passes
L = [1, 2, 3, 4]
I1, I2 = iter(L), iter(L)


def both(N):
    for i in range(N): yield i
    for i in (x ** 2 for x in range(N)) : yield i

list(both(10))

[x ** 2 for x in range(10)]
(x ** 2 for x in range(10))
{x ** 2 for x in range(10)}
{x:x ** 2 for x in range(10)}

(x for x in range(5))  # x is local

x = 99
[x for x in range(5)]  # again, x is local
x

y = 99
for y in range(5): pass  # loop statements don't localize names
y



# timer
import time, sys
try:
    timer = time.perf_counter
except:
    timer = time.clock if sys.platform[:3] == 'win' else time.time

def myTimer(reps, func, *pargs, **kargs):
    repslist = list(range(reps))
    times = []
    for i in repslist:
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        times.append(elapsed)
    times.sort()
    return (times[0], times[reps//2], times[-1])

myTimer(1000, pow, 2, 1000)
myTimer(1000, str.upper, 'spam')
myTimer(1000, operator.mul, 'spam', 5)

import time
time.perf_counter()
time.process_time()


# test list builders
reps = 100000
repslist = list(range(reps))

def forloop():
    res = []
    for x in repslist:
        # res.append(abs(x))
        res.append(x + 10)
    return res

def listComp():
    # return [abs(x) for x in repslist]
    return [x + 10 for x in repslist]

def mapCall():
    # return list(map(abs, repslist))
    return list(map(lambda x: x + 10, repslist))

def genExpr():
    # return list(abs(x) for x in repslist)
    return list(x + 10 for x in repslist)

def genFunc():
    def gen():
        for x in repslist:
            # yield abs(x)
            yield x + 10
    return list(gen())

for test in (forloop, listComp, mapCall, genExpr, genFunc):
    theMin, theMed, theMax = myTimer(1000, test)
    print('%-9s: min %.5f, med %.5f and max %.5f' %(test.__name__, theMin, theMed, theMax))

# When abs(x), a built-in function is used:
# forloop  : min 0.01350, med 0.01493 and max 0.03956
# listComp : min 0.00810, med 0.00930 and max 0.01564
# mapCall  : min 0.00598, med 0.00682 and max 0.01059
# genExpr  : min 0.01116, med 0.01208 and max 0.02150
# genFunc  : min 0.01096, med 0.01257 and max 0.01693

# When x + 10, a user-defined function is used:
# forloop  : min 0.01192, med 0.01282 and max 0.02471
# listComp : min 0.00650, med 0.00767 and max 0.01263
# mapCall  : min 0.01477, med 0.01575 and max 0.03093
# genExpr  : min 0.00939, med 0.01033 and max 0.01542
# genFunc  : min 0.00959, med 0.00998 and max 0.01686

x = 99
def selector():
    import __main__  # Interactive namespace is a module
    print(__main__.x)  # It reaches the global version of x
    x = 88
    print(x)
selector()

def saver(x=[]):
    x.append(1)
    print(x)

saver([2])  # [2, 1]
saver()  # [1]
saver()  # [1, 1]
saver()  # [1, 1, 1]
# The mutable defaults are evaluated at def time, not call time.
# The list keeps growing even though interrupted by other calls.

a = []
b = []
c = a or b
c is a
c is b

## state retention
def saver():
    saver.x.append(1)
    print(saver.x)

saver()  # need to initialize saver.x
saver.x = []
saver()  # achieve state retention

## closures
def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x: i ** x)
    return acts
acts = makeActions()
acts[0](2)  # 16
acts[1](2)  # 16
acts[2](2)  # 16
acts[3](2)  # 16
acts[4](2)  # 16
## Comment: The enclosing scope variable is looked up when the 
## functions are called, they all effectively remember the same
## value, the value the loop variable had on the last loop.


list = [1, 2]  # list can be overwritten
list(map(abs, range(5)))  # list will not work
del list  # del list
list(map(abs, range(5)))  # list resumes being effective


###### Part IV Exercises #####
# 1. The basics



## Chapter 26
