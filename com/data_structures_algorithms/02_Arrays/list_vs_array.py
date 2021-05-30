"""
What's the Difference Between list and array?
Now that we know their definitions and features, we can talk about the differences between lists and arrays in Python:

Arrays need to be declared. Lists don't, since they are built into Python.
 In the examples above, you saw that lists are created by simply enclosing a sequence of elements into square brackets.
 Creating an array, on the other hand, requires a specific function from either the array module (i.e., array.array())
or NumPy package (i.e., numpy.array()). Because of this, lists are used more often than arrays.
Arrays can store data very compactly and are more efficient for storing large amounts of data.
Arrays are great for numerical operations; lists cannot directly handle math operations. For example,
you can divide each element of an array by the same number with just one line of code.
If you try the same with a list, you'll get an error.
"""
import array as arr
list1 = [3, 5, 7, 8, "Abir"]

print(type(list1))

# allows duplicates values
list1.append(8)
print(list1)

x = list1[1] = 12
print(x)

print(list1)
# In the code below, the "i" signifies that all elements in array_1 are integers:
array_1 = arr.array("i", [5, 7, 9, 10])
print(array_1)
print(type(array_1))