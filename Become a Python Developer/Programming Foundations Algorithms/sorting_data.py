'''
Sorting Data

- Most modern languages have sorting built in
- These sorting tools include:
    + The Bubble Sort
        - Very simple to understand and implement
        - Performance: O(n**2)
            + For loops inside of for loops are usually n **2
        - Other sorting algorithms are generally much better
        - Not considered to be a practical solution unless the data set is very small
    + The Merge Sort
        - Divide and conquer algorithm
        - Breaks a dataset into individual pieces and merges them
        - Uses recursion to operate on datasets
        - Performs well on large sets of data
        - In general has a performance of O(n log n) time complexity
    + The Quicksort
        - Divide and conquer algorithm, like the merge sort
        - Also uses recursion to perform sorting
        - Generally performs better than merge sort, O(n log n)
        - Operates in place on the data
        - Worst case is O(n2) when data is mostly sorted already
    * Not the ONLY sorting tools
    * searching for an item in an unordered list, sometimes called a Linear search
'''