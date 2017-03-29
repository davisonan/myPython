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

#' # Background of this writeup
#' The best way to learn something is to write about it as if you are going
#' to teach this subject. Now I'm going to give a lecture about sorting 
#' algorithms and I'm writing this course material for my students.

#' # Background of searching algorithms
#' It's useful and important. Dating back to a long time ago. Many sorting
#' algorithms were invented. They differ in memory requirement and time
#' complexity. The reason of ordering these algorithms is 
#' The algorithms include insertion sort, selection sort, merge sort, quick
#' sort, bubble sort. THroughout this article, only an ascending order is 
#' seeked. We'll start the cases with no duplicates and consider the case 
#' with duplicates later on.

#' ## Bubble sort
#' Bubble sort is constantly moving the largest value to the end by comparing 
#' elements pairwise from the beginning to the end iteratively. The whole 
#' process is like merging the largest value like a bubble to the surface and 
#' hence the name.
