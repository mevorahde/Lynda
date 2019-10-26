# Use a hashtable (dictionary) to filer out duplicate items

# define a set of items that we want to reduce duplicates
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

# create a hashtable to perform a filter
duplicate_filter = dict()

# loop over each item and add to the hashtable
for item in items:
    duplicate_filter[item] = 0
# create a set from the resulting keys in the hashtable
result = set(duplicate_filter.keys())
print("Duplicate items removed....")
print("Here is your list: ", result)
