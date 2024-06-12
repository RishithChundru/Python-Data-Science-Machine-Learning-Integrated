# Data Manipulation and analysis with Numpy
# Creating a numpy array from a list
import numpy as np
# Creating a 1D array from a list
# array object in numpy is called ndarray
arr1=np.array([1,2,3,4,5])
print(arr1)

# Creating a 2D array from a list of lists
arr2=np.array([[1,2,3],[4,5,6]])
print(arr2)

# Creating Arrays with Functions

# Creating an array of zeros
# zeros(rows,cols)
zeros=np.zeros((3,4))
print(zeros)

# creating an array of Ones
# ones(rows,cols)
ones=np.ones((3,4))
print(ones)

# creating an array with a range of values
# arange(start number, stop number, step)
range_arr=np.arange(10,20,2)
print(range_arr)

# Creating an array with random values
random_arr=np.random.rand(3,3)
print(random_arr)


# Basic Array Operations- Element-wise Operations

arr=np.array([1,2,3,4,5])

# Element-wise addition
print(arr+2)

# Element-wise Multiplication
print(arr*2)

# Element-wise Subtraction
print(arr-1)

# Element-wise division
print(arr/2)

# Mathematical Functions

arr=np.array([1,2,3,4,5])

# square root
print(np.sqrt(arr))

# Exponential
print(np.exp(arr))

# Logarithm
print(np.log(arr))

# Sine
print(np.sin(arr))


# Indexing and Slicing- Indexing

arr=np.array([1,2,3,4,5])

# Accessing Elements
print(arr[0])
print(arr[1])

# Slicing array
print(arr[1:4]) # Elements from index 1 to 3
print(arr[:3])  # First three Elements
print(arr[2:])  # Elements from index 2 to the end

# Advanced Indexing

arr=np.array([1,2,3,4,5])

# Boolean Indexing
print(arr[arr>3])

# Fancy Indexing
indices=[0,2,4]
print(arr[indices])


# Reshaping and Transposing- Reshaping Arrays

arr=np.array([[1,2,3],[4,5,6]])

# Reshaping array
reshaped=arr.reshape((3,2))
print(reshaped)

# Transposing Arrays
transposed=arr.T
print(transposed)

# Aggregation Function- Sum and Mean
arr=np.array([[1,2,3],[4,5,6]])

# Sum of all elements
print(np.sum(arr))

# sum along columns
print(np.sum(arr,axis=0))

# sum along rows
print(np.sum(arr,axis=1))

# Mean of all elements
print(np.mean(arr))

# Minimum value
print(np.min(arr))

# Maximum Value
print(np.max(arr))

# index of minimum value
print(np.argmin(arr))

# Index of maximum value
print(np.argmax(arr))