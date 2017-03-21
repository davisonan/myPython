#' % Miscellaneous
#' % Xu Tian
#' % 2017/03/14

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
    if len(x) in [0, 1]:
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


