#' % Searching algorithms
#' % Xu Tian
#' % 2017/03/20

#' # Background of sorting algorithms
#' This write-up covers the following searching algorithms: binary search,
#' linear search, etc.

#' ## Binary search
#' Suppose the underlying array has already been sorted. And the binary search 
#' seeks to divide the searching space by one half at every iteration. The 
#' time complexity is $O(log(n))$.

def binarySearch(arr, x):
    n = len(arr)
    start = 0
    end = n-1
    mid = n//2
    