import numpy as np

# Define the curve function (x^2 is preset but it can be changed into any simple function)
def f(x):
    return x**2

# Define the limits of the curve  (0 and 1 are preset but they can be changed to any value)
a = 0
b = 1

# Choose the number of rectangles (1000 are preset but it can be changed to any value)
n = 1000

# Calculate the width of each rectangle
dx = (b - a) / n

# Calculate the area under the curve
area = 0
for i in range(n):
    xi = a + i * dx
    area += f(xi) * dx

# Calculate the length of the curve
length = 0
for i in range(n):
    xi = a + i * dx
    length += np.sqrt(1 + (2 * xi)**2) * dx

# Calculate the volume of the solid of revolution
volume = 0
for i in range(n):
    xi = a + i * dx
    volume += np.pi * (f(xi)**2) * dx

# Print the results
print("Area:", area)
print("Length:", length)
print("Volume:", volume)
