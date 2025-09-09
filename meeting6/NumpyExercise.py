import numpy as np #Importing the Numpy library so that it can be used
# a = np.array([1,"b",3,"c",5]) # Create a 1D Numpy array
# b = np.array([6,7,8,9,10])# Create a 1D Numpy array
# print(a) # Displays the output of the Numpy array that has been created
# print(b) # Displays the output of the Numpy array that has been created

Array2D = np.array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]])

# print(Array2D)

array3D = np.array([[[1,2,3], [4,5,6]],
[[7,8,9], [10,11,12]],
[[13,14,15], [16,17,18]]])

# print(array3D)

data = np.array([[1,2,3,4], [5,6,7,8]])
print(data[:, 1:4])
