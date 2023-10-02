"""
Name: Christopher Bucsa
"""
import numpy as np 
np.set_printoptions(precision=3)
np.random.seed(123)

"""
Problem 1
"""
print("\n",40*"-","\n","Problem 1:\n",40*"-")
# Create/Print a null vector of size 11
vectorNull = np.zeros(11, int)
print("Null vector with 11 elements: ", vectorNull)


"""
Problem 2
"""
print("\n",40*"-","\n","Problem 2:\n",40*"-")
# Create and print a 3x5 matrix of ones.
threeFive = np.ones((3, 5))
print("3 x 5 matrix of ones: ", threeFive)

"""
Problem 3
"""
print("\n",40*"-","\n","Problem 3:\n",40*"-")
# Create and print a vector with 10 linearly spaced elements having
# values ranging from 0.0 to 10.0
linSpaceVector = np.linspace(0.0, 10.0, 10)
print("Vector with 10 linearly spaced elements: ", linSpaceVector)


"""
Problem 4
"""
print("\n",40*"-","\n","Problem 4:\n",40*"-")
# Create and print a 4x3 matrix with values from 1 to 12.
fourThree = np.arange(1, 13)
matrix = fourThree.reshape(4,3)
print("4 x 3 matrix: ", matrix)


"""
Problem 5
"""
print("\n",40*"-","\n","Problem 5:\n",40*"-")
# Create vector and reverse it
reverse = np.arange(20,31)
print("Vector reversed: ", reverse[::-1])

"""
Problem 6
"""
print("\n",40*"-","\n","Problem 6:\n",40*"-")
# Create linearly spaced 1D array with values between -5 and 15
intVector = np.linspace(-5,15,21)
print(intVector)

"""
Problem 7
"""
print("\n",40*"-","\n","Problem 7:\n",40*"-")
# Create 1D array/vector with real numbers from -10.0 to 10.0 in intervals of 0.1
realArray = np.arange(-10.0, 10.1,0.1)
print("Size of array = ", realArray.size)

"""
Problem 8
"""
print("\n",40*"-","\n","Problem 8:\n",40*"-")
# Create a 1D array of size 100 whose elements are all ones. Then, set the values with odd
# indices to -1.
onesVector = np.ones(100)
onesVector[1::2] = -1
print(onesVector[0:10])

"""
Problem 9
"""
print("\n",40*"-","\n","Problem 9:\n",40*"-")
# Create/print numpy arrays of various dimensions
B = np.array([[1, 2, -3], [3, 4, -1]])
print(B, "\n")

A = np.array([[2, 5, -1], [1, 4, 5], [2, 1, -6]])
print(A, "\n")

y = np.array([-1, 3, 7])
print(y, "\n") 

z = np.array([13, 0, 2])
zCol = z.reshape(3,1)
print(zCol)

"""
Problem 10
"""
print("\n",40*"-","\n","Problem 10:\n",40*"-")
# Convert temeratures from celcius to fahrenheit using arrays
temperatures = np.arange(-40, 101, 1) # Create an array with values ranging from -40 to 100, in steps of 1
temperatures[0::1] = (9/5) * temperatures + 32 # Use slicing to go over each index of array
print("-40 degrees Celcius = ", temperatures[0], " degrees Fahrenheit") 
print("100 degress Celcius = ", temperatures[-1], " degrees Fahrenheit")

"""
Problem 11
"""
print("\n",40*"-","\n","Problem 11:\n",40*"-")
# Create 4x6 matrix of random integers between -10 to 10
# and retrieve certain values
randArray = np.random.randint(-10, 10, size = (4, 6))
print("Value at (1,1) of matrix = ", randArray[1,1])
print("Value at (2,3) of matrix = ", randArray[2,3])
print("Value at (3,0) of matrix = ", randArray[3,0])
print("Value at (0,5) of matrix = ", randArray[0,5])

"""
Problem 12
"""
print("\n",40*"-","\n","Problem 12:\n",40*"-")
# part 1: Create 1D array containing 10^6 elements using .normal function
my_vec = np.random.normal(0, 1, 10**6)

# part 2: Compute average of arary using loop
mySum = 0
for e in my_vec:
    mySum = mySum + e 
average = mySum / len(my_vec) 
print("Average using loop: ", average)

# part 3: Compute average of array using built-in function
print("Average using numpy function: ", np.mean(my_vec))

# part 4: Interpretation
print("The average makes logical sense. Since the size is 10^6, the denominator will be"
      "significantly smaller than the numerator(sum) when calculating the average.  This "
      "leads to a very small value for the average.")

"""
Problem 13
"""
print("\n",40*"-","\n","Problem 13:\n",40*"-")
# Creating, adding, multiplying vectors
a = np.random.randint(1, 11, size = 10)
b = np.random.randint(1, 11, size = 10) 
c = np.random.randint(1, 11, size = 10)
d = (a * b) + c
print(d)

"""
Problem 14
"""
print("\n",40*"-","\n","Problem 14:\n",40*"-")
# Create function to perform computations on arrays
def position(t):
    """
    Given an array of time, this function calculates the distance using d = 0.5 * g * t^2
    Parameters: 
    t(array):  Measurments of time, in seconds.
    Returns:
    distance array: Array containg distances for each time measurement 
    """
    g = -9.81
    d = 0.5 * g * (t**2)
    return d

t = np.arange(0, 10.1, 0.1)
distance = position(t)  
expected_result = 0.5 * -9.81 * 1**2
print("Expected Result: ", expected_result)
print("When time is 1, distance = ", distance[10])
print("Is result as expected?", expected_result == distance[10] )

