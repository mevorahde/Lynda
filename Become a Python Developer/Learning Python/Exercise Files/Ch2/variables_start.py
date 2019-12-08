# 
# Example file for variables
#

# Declare a variable and initialize it
#f = 0
#print(f)


# # re-declaring the variable works
#f = "abc"
#print(f)


# # ERROR: variables of different types cannot be combined
# print("the is a string" + 123)
# Above would work in JavaScript
# doesn't work in Python, variables need to be the same type
#print("the is a string " + str(123))

# Global vs. local variables in functions


def some_function():
    # make f global
    global f
    f = "def"
    print(f)


some_function()
print(f)

# can delete a global variable with the 'del' function
#del f
#print(f)
