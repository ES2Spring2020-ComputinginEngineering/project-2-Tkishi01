#Please place your FUNCTION code for step 4 here.
import KMeansClustering_functions as kmc #Use kmc to call your functions
import numpy as np
x = np.array([4,5,6])
y = np.array([1,2,3])
bob = np.array(list(map(lambda i: [y[i],x[i]], range(len(x)))))
z = np.array([7,8,9])
chad = np.array(list(map(lambda i: [bob[i],z[i]], range(len(z)))))
print(bob)

jon = np.column_stack((y,x))
sam = np.column_stack((jon,z))
print(sam[0])