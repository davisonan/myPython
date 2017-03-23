#' % Sorting algorithms
#' % Xu Tian
#' % 2017/03/17

#' # Background of sorting algorithms
#' This write-up covers the following algorithms: bubble sort, insertion 
#' sort, selection sort, merge sort and quick sort. THroughout this article, 
#' only an ascending order of an array is seeked.

#' ## Bubble sort
#' Bubble sort is constantly moving the largest value to the end by comparing 
#' elements pairwise from the beginning to the end iteratively. The whole 
#' process is like emerging the largest value like a bubble to the surface and 
#' hence the name.

def bubbleSort(arr):
    n = len(arr)
    flag = False  # Sorting completion indicator
    while True:
        print(arr)
        flag = True
        for i in range(1, n):
            if arr[i] < arr[i-1]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                flag = False
        n -= 1
        if flag: break

arr = [2, 5, 4, 6, 4, 1, 3, 8, 7]
bubbleSort(arr)

#' We can clearly see that in every iteration, the largest value is moved to
#' the back of the array. Therefore, we can shrink the for loop by 1 in every
#' iteration. The flag is set to False whenever there's a swap. When there's 
#' no swap, the sorting is completed. The duplicated values are not an issue 
#' since the same values will not be swaped and other values can still be 
#' compared as in the regular case.

#' Here's the summary of key attributes of an algorithm:

#' - __Worst and average case time complexity__: $O(n^2)$. Worst case occurs when array is reversely sorted.
#' - __Best case time complexity__: $O(n)$. Best case occurs when array is already sorted.
#' - __Extra space__: $O(1)$
#' - __Boundary cases__: Bubble sort takes minimum time $O(n)$ when elements are already sorted.
#' - __Sorting in-place__: Yes
#' - __Stable__: Yes

#' ## Insertion sort
#' The idea of insertion sort is by maintaining the array at the beginning 
#' sorted and moving the first element in the remaining unsorted array to 
#' the right place in the beginning.

def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        print(arr)
        j = i
        while True and j > 0:
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1
            else:
                break

arr = [6, 5, 3, 1, 8, 7, 2, 4]
insertionSort(arr)
print(arr)

#' Here's the summary of key attributes of an algorithm:

#' - __Worst and average case time complexity__: $O(n^2)$. Worst case occurs when array is reversely sorted.
#' - __Best case time complexity__: $O(n)$. Best case occurs when array is already sorted.
#' - __Extra space__: $O(1)$
#' - __Boundary cases__: Insertion sort takes minimum time $O(n)$ when elements are already sorted.
#' - __Sorting in-place__: Yes
#' - __Stable__: Yes

#' The idea is to move the first element of the remaining unsorted array into 
#' the right place in the already sorted array. Since this is done in-place,
#' the new element is compared one by one starting from the end of the sorted 
#' array. Duplicates don't matter since there's a swap only when the new 
#' element is smaller than the previous one.


#' ## Selection sort
#' Selection sort is similar to the insertion sort except that every time we 
#' move the smallest element in the remaining array to the beginning of this 
#' remaining array such that the array in the front upto this element is 
#' sorted.

def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        print(arr)
        idx = arr.index(min(arr[i:]))
        arr[i], arr[idx] = arr[idx], arr[i]

arr = [6, 5, 3, 1, 8, 7, 2, 4]
selectionSort(arr)
print(arr)

#' The current element also needs to be compared with the smallest of the 
#' rest. Therefore, in the fourth row, it's min(arr[i:]) including the 
#' i-th element in the array. If the i-th element happens to be the smallest,
#' it doesn't hurt to swap the value with itself. And this redundancy is well
#' compensated by the clarity of the code.

#' Here's the summary of key attributes of an algorithm:

#' - __Worst and average case time complexity__: $O(n^2)$. Worst case occurs when array is reversely sorted.
#' - __Best case time complexity__: $O(n^2)$. Best case occurs when array is already sorted.
#' - __Extra space__: $O(1)$
#' - __Boundary cases__: Insertion sort takes minimum time $O(n)$ when elements are already sorted.
#' - __Sorting in-place__: Yes
#' - __Stable__: Yes

#' The best, average and worst cases all have $O(n^2)$ time complexity. This 
#' makes this algorithm not suitable for large $n$.

#' ## Heap sort
#' Heap sort is 


def heapSort(arr):
    



#' ## Merge sort
#' Merge sort is a divide and conque algorithm by dividing the array into 
#' multiple subarrays and merging them in a structured way such that the 
#' returned array is sorted. It's a faster algorithm than the previous methods.

def merge(l, r):
    output = []
    i, j = 0, 0
    nl, nr = len(l), len(r)
    while i < nl and j < nr:
        if l[i] < r[j]:
            output.append(l[i])
            i += 1
        else:
            output.append(r[j])
            j += 1
    if i < nl: output.extend(l[i:])
    if j < nr: output.extend(r[j:])
    return output

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        l = mergeSort(arr[:mid])
        r = mergeSort(arr[mid:])
        tmp = merge(l, r)
        print(tmp)
        return tmp

arr = [6, 5, 3, 4, 1, 8, 7, 2, 4]
arrSorted = mergeSort(arr)

#' Here's the summary of key attributes of an algorithm:

#' - __Worst and average case time complexity__: $O(nlog(n))$. Worst case occurs when array is reversely sorted.
#' - __Best case time complexity__: $O(nlog(n))$. Best case occurs when array is already sorted.
#' - __Extra space__: $O(1)$
#' - __Boundary cases__: Insertion sort takes minimum time $O(nlog(n))$ when elements are already sorted.
#' - __Sorting in-place__: Yes
#' - __Stable__: Yes

#' ## Quick sort
#' Quick sort is a divide and conquer algorithm. It has two steps: one is to 
#' partition the array by a pivot point usually at the end of the array being
#' sorted; the other is to move the values that are smaller than the pivot 
#' point to the left and those larger than the pivot point to the right in the
#' array being sorted.

def quickSort(arr, lo, hi):
    if lo < hi:
        p = partition(arr, lo, hi)
        print(arr)
        quickSort(arr, lo, p-1)
        quickSort(arr, p+1, hi)

def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[hi] = arr[hi], arr[i+1]
    return i + 1

arr = [6, 5, 3, 4, 1, 8, 7, 2, 4]
quickSort(arr, 0, len(arr)-1)
print(arr)

#' Here's the summary of key attributes of an algorithm:

#' - __Worst case time complexity__: $O(n^2)$. Worst case occurs when array is reversely sorted.
#' - __Average case time complexity__: $O(nlog(n))$.
#' - __Best case time complexity__: $O(nlog(n))$. Best case occurs when array is already sorted.
#' - __Extra space__: $O(1)$
#' - __Boundary cases__: Insertion sort takes minimum time $O(nlog(n))$ when elements are already sorted.
#' - __Sorting in-place__: Yes
#' - __Stable__: No


#' ## Topological sort




#' # Use searching algorithms to find the k-th largest element
#' This is actually based on the problem 215. Kth Largest Element in an Array
#' on Leetcode. One [solution](https://discuss.leetcode.com/topic/22159/python-different-solutions-with-comments-bubble-sort-selection-sort-heap-sort-and-quick-sort)
#' gives a comprehensive list of solutions based on the common searching ideas
#' this tutorial covered before. And I think this sets up a good example of 
#' organizing knoweldge and applying knowledge on new problems. This is a 
#' good inspiration and I'll keep doing that starting from here.

# O(nlog(n)) solution-1
# A little more typing
def findKthLargest1(nums, k):
    return sorted(nums, reverse=True)[k-1]

arr = [6, 5, 3, 4, 1, 8, 7, 2, 4]
findKthLargest1(arr, 3)

# O(nlog(n)) solution-2
# In-place; no additional memory.
def findKthLargest2(nums, k):
    nums.sort(reverse=True)
    return nums[k-1]

arr = [6, 5, 3, 4, 1, 8, 7, 2, 4]
findKthLargest2(arr, 3)

# O(nlog(n)) solution-3
# A clean and concise solution
def findKthLargest3(nums, k):
    return sorted(nums)[-k]

arr = [6, 5, 3, 4, 1, 8, 7, 2, 4]
findKthLargest3(arr, 3)

# O(nk) solution
# Based on bubble sort
def findKthLargest4(nums, k):
    n = len(nums)
    for i in range(k):
        for j in range(1, n):
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
        n -= 1
    return nums[-k]

arr = [6, 5, 3, 4, 1, 8, 7, 2, 4]
findKthLargest4(arr, 3)

# O(nk) solution-2
# Based on selection sort
# Faster than bubble sort, maybe due to the maximum routine
def findKthLargest5(nums, k):
    for i in range(k):
        idx = nums.index(max(nums[i:]))
        nums[i], nums[idx] = nums[idx], nums[i]
    return nums[k-1]

arr = [6, 5, 3, 4, 1, 8, 7, 2, 4]
findKthLargest5(arr, 4)

# The insertion sort is not an idea to build the algorithm upon. Because
# all the numbers would need to be inserted into the proper place to complete
# the insertion sort. Therefore, it's still a O(n^2) algorithm.

# 
# Faster than bubble sort, maybe due to the maximum routine
def findKthLargest6(nums, k):
    for i in range(k):
        idx = nums.index(max(nums[i:]))
        nums[i], nums[idx] = nums[idx], nums[i]
    return nums[k-1]

arr = [6, 5, 3, 4, 1, 8, 7, 2, 4]
findKthLargest5(arr, 4)




# To time the functions, use the following chunk of code to
# do that.
# import timeit
# timeit.timeit('findKthLargest(arr, 3)', 
#     setup="from __main__ import findKthLargest, arr", 
#     number=1000)


