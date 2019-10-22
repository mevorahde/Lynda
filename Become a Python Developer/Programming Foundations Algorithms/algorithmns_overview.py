'''
Algorithm complexity:
	- space complexity: How much memory does it require?
	- time complexity: how much time does it take to complete?
Inputs and Outputs:
	- what does the algorithm accept, and what are the results?
Classification:
	- Can be serial/parallel, exact/approximate, deterministic/non-deterministic (produce a solution over successive
	guesses and gets more accurate over time.)
	
Common Algorithms:
	- Search algorithms:
		+ Find specific data in a structure
	- Sorting algorithms:
		+ Take a dataset and apply a sort order to it
	- Computational algorithms:
		+ Conversion like, given one set of data, calculate in another
	- Collection algorithms:
		+ Work with collection of data
'''


# Euclid's Algorithm
# Definition: find the greatest common denominator (GCD) of two integers.


def gcd(a: int, b: int) -> int:
	while b != 0:
		t = a
		a = b
		b = t % b
	
	return a


print(gcd(60, 96))  # answer should be 12
print(gcd(20, 8))   # answer should be 4

'''
Big-O Notation:
- O(1) : Constant time - Looking up a single element in an array
- O(log n) : Logarithmic - Finding an item in a sorted array with a binary search
- O(n) : Linear time - Searching an unsorted array for a specific value
- O(n log n) : Log-linear - Complex sorting algorithms like heap sort and merge sort
- O(n**2) : Quadratic - Simple sorting algorithms, such as bubble sort, selection sort, and insertion sort
'''
