# algo.py

def max_subarray(A):
	max_ending_here = max_so_far = 0
	for x in A:
		max_ending_here = max(0, max_ending_here + x)
		max_so_far = max(max_so_far, max_ending_here)
		print x, max_ending_here, max_so_far
	return max_so_far

A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_subarray(A)

#!/usr/bin/env python
# coding=utf-8

"""
solving a quadratic equation
"""

from __future__ import division
import math

def quadratic_equation(a,b,c):
    delta = b*b - 4*a*c
    if delta<0:
        return False
    elif delta==0:
        return -(b/(2*a))
    else:
        sqrt_delta = math.sqrt(delta)
        x1 = (-b + sqrt_delta)/(2*a)
        x2 = (-b - sqrt_delta)/(2*a)
        return x1, x2

if __name__ == "__main__":
    print "a quadratic equation: 2x^2 - 3x + 1 = 0"
    coefficients = (2, -3, 1)
    roots = quadratic_equation(*coefficients)
    if roots:
        print "the result is:",roots
    else:
        print "this equation has no solution."


##### Microsoft #####
# Given an array of numbers, move all the 0s to the beginning
# of the array and leave the rest in the original oder.
l = [0, 1, 4, 0, 3, 5, 6, 0, 0, 2]
j = len(l) - 1  # index of last position for next positive integer
for i in range(len(l)-1, 0, -1):  # iterate through the numbers backwards
    if l[i] != 0:
        l[i], l[j] = l[j], l[i]
        j -= 1

##### Microsoft #####
# Find a pair in an array summing up to t
# 1. Use hashtable for searching and indexing.
# 2. Iterate through the array and check t-i.
# 3. When t-i = i, there's no such a pair.
from collections import Counter
l = [-1, 2, 3, 6, 2]
t = 2
def findPair(l, t):
    d = Counter(l)
    for i in l:
        x = t - i
        if x in d and (not (x == i and d[x] == 1)):
            return True
    return False

def test():
    assert(findPair(l, 2) == True)
    assert(findPair(l, 12) == False)
    assert(findPair(l, 4) == False)
    assert(findPair(l, 6) == False)
    print("All True")

test()


##### Microsoft #####
# Find the minimum of distance of two words in a article.
# Solution 1:
# Create two lists of positions of words and find
# all the distances of two lits and find the minimum.
# Note: This is a solution, but not an impressive one
# in an interview. You can pass, but you wouldn't shine.
def findMinDist1(s, w1, w2):
    l = s.split()
    l1, l2 = [], []
    for idx in range(len(l)):
        word = l[idx]
        word = word.strip('.,!~-| ').lower()
        if word == w1:
            l1.append(idx)
        if word == w2:
            l2.append(idx)

    minDist = min([abs(i-j) for i in l1 for j in l2])
    print(minDist, len(l1) * len(l2))

# Solution 2: The minimum finding part can be done better.
# Use two iterators for the two arrays. When one number in
# one array is already smaller than the current number in
# the other one, move to the next few until it's getting
# bigger. Because the minimum distance could only happen
# around the numbers that are close in two arrays.
def findMinDist2(s, w1, w2):
    l = s.split()
    l1, l2 = [], []
    for idx in range(len(l)):
        word = l[idx]
        word = word.strip('.,!~-| ').lower()
        if word == w1:
            l1.append(idx)
        if word == w2:
            l2.append(idx)

    i, j = 0, 0
    minVal = len(l)
    counter = 0
    while True:
        counter += 1
        if l1[i] > l2[j]:
            dis = l1[i] - l2[j]
            j += 1
        else:
            dis = l2[j] - l1[i]
            i += 1
        minVal = dis if dis < minVal else minVal
        if i == len(l1) or j == len(l2):
            break

    print(minVal, counter)

s = '''When I teach computer science courses, I want to cover important concepts in addition to making the material interesting and engaging to students. Unfortunately, there is a tendency for introductory programming courses to focus far too much attention on mathematical abstraction and for students to become frustrated with annoying problems related to low-level details of syntax, compilation, and the enforcement of seemingly arcane rules. Although such abstraction and formalism is important to professional software engineers and students who plan to continue their study of computer science, taking such an approach in an introductory course mostly succeeds in making computer science boring. When I teach a course, I don't want to have a room of uninspired students. I would much rather see them trying to solve interesting problems by exploring different ideas, taking unconventional approaches, breaking the rules, and learning from their mistakes. In doing so, I don't want to waste half of the semester trying to sort out obscure syntax problems, unintelligible compiler error messages, or the several hundred ways that a program might generate a general protection fault.'''
w1 = 'a'
w2 = 'the'
findMinDist1(s, w1, w2)
findMinDist2(s, w1, w2)

##### Akuna Capital #####
# Find the median of a subarray
# Given the original array has been sorted in
# an ascending order.
def subarray_median(arr, k):
    idx0 = arr.index(k)
    while True:
        if idx0+1 < len(arr) and arr[idx0+1] == k:
            idx0 += 1
        else:
            break
    l = arr[:idx0+1]
    n = len(l)
    return (l[int(n/2)-1] + l[int(n/2)])/2.0 if n % 2 == 0 else l[n//2]

l = [1, 2, 3, 4, 5, 6, 8, 9, 12, 23, 141, 434]
k = 8
subarray_median(l, k)

##### Akuna Capital #####
# Rotate a matrix 90 degress in a clock-wise manner
m1 = []
for i in range(7):
    row = [i for i in range(i, i+5)]
    m1.append(row)

m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]
list(reversed(list(zip(*m1[::-1]))))  # Mirrored
# [(9, 6, 3),
#  (8, 5, 2),
#  (7, 4, 1)]
list(zip(*m1[::-1]))  # Clockwise
# [(7, 4, 1),
#  (8, 5, 2),
#  (9, 6, 3)]
list(reversed(list(zip(*m1))))  # Counte-clockwise
# [(3, 6, 9),
#  (2, 5, 8),
#  (1, 4, 7)]


# Binary Search
def bs(l, x, start, end):
    if start > end:
        return -1
    mid = (start + end)//2
    print(mid)
    if l[mid] > x:
        return bs(l, x, start, mid)
    elif l[mid] < x:
        return bs(l, x, mid, end)
    else:
        return l[mid]

l = [1, 2, 4, 6, 8, 13]
bs(l, 5, 0, len(l)-1)

def bs(l, x):
    start = 0
    end = len(l) - 1
    found = False
    while start <= end and not found:
        mid = (start + end)//2
        if l[mid] == x:
            found = True
        else:
            if l[mid] < x:
                start = mid + 1  # pos 1
            else:
                end = mid - 1  # pos 2
    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
bs(testlist, 13)
# Comment: The +1 and -1 at positions 1 and 2 are critical for the success of
# this algorithsm.
# This algorithm is quicker and more efficient than the recursive version.

l = [1, 2, 4, 6, 8, 13]
bs(l, 5, 0, len(l)-1)


# Reverse an integer
def reverseInt(x):
    assert x >= 0  # This function only for positive input
    n = 0
    while x > 0:
        n = 10 * n + x % 10
        x //= 10
        print(x, n)
    return n

reverseInt(10002)

# Find all prime factors
def find_prime(n):
    factors = []
    i, j, d = 0, 0, 2
    while n > 1:
        while n % d == 0:
            n //= d
            factors.append(d)
        j = (j+1) % 2
        if j == 0: i += 1
        if i == 0:
            d = 3
        else:
            d = 6 * i + [-1, 1][j]
        if d * d > n and n > 1:
            factors.append(n)
            break
    return factors
x = 600851475143
find_prime(x)

##### Fibonacci numbers #####
def fib1(n):
    a, b = 0, 1
    idx = 0
    while True:
        a, b = b, a+b
        yield b


##### Binary search #####
def binarySearch(arr, x):
	i, j = 0, len(arr)-1
	while i <= j: # 1
		mid = (i+j)//2 # 2
		print(i, mid, j)
		if arr[mid] == x:
			return True
		elif arr[mid] > x:
			j = mid - 1 # 3
		else:
			i = mid + 1 # 4
	return False

arr = [1, 2, 3, 4, 5, 7, 8, 9, 12, 14, 16, 18]
print(binarySearch(arr, 6))
# Comments: the four key points are labeled. Keep these four rules in mind if
# you don't get the full logic.
