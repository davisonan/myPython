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
# %timeit isPalindrome(101010101010101010101)


#' # Shuffling
#' This chunk of code is from leetcode.

# for i in range(len(ans)-1, 0, -1):     # start from end
#     j = random.randrange(0, i+1)    # generate random index 
#     ans[i], ans[j] = ans[j], ans[i]    # swap

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
try:
    print(obj.v1, obj.v2)
except:
    print("The object has no attribute 'v1'.")

#' # The essence of object reference and variable name
#' A variable name is essentially a reference to an object, even in the 
#' simplest form of assignment. This is a big distinction with C++ where
#' an assignment is a binding to a piece of memory where the value of 
#' the variable name resides, whereas in Python the name is essentially
#' a reference to an object.


#' # Visualizing the time complexity of a searching algorithm in Python
#' This is a small study to show that the time complexity of the function 
#' ```sorted``` in Python is indeed a $O(nlog(n))$ algorithm. 

import timeit
import random
import matplotlib.pyplot as plt
import numpy as np

# def test(arr):
#     sorted(arr)

# times = []
arr0 = [10, 50, 100, 500, 1e3, 5e3, 1e4, 5e4, 1e5, 5e5, 1e6, 5e6, 1e7, 5e7]
# for idx, val in enumerate(arr0):
#     print(val)
#     arr = [random.random() for _ in range(int(val))]
#     times.append(timeit.timeit("test(arr)", setup="from __main__ import test, arr", number=int((20-log(val))**2)).real)


times = np.array([0.00027, 0.00133, 0.00275, 
    0.01583, 0.03339, 0.15277, 0.29951, 
    1.30919, 2.75746, 12.3195, 23.6044, 
    87.7369, 150.790, 362.974])

arr1 = np.array(times)/np.array(arr0)
c = arr1[-1]
plt.plot(arr0, c * np.array(arr0))
plt.plot(arr0, np.array(times))
plt.plot(arr0, c ** 1.2 * np.array(arr0) * np.log(np.array(arr0)))