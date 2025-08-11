import numpy as np
x=[1,2,3,4,5]
"""
# array() is used to create an array from a list or tuple
arr=np.array(x)
arr1=np.array(x,dtype='float64') # dtype can modify the data type of the array you can take int ,float, str,complex,bool.
print(arr)
print(arr.ndim)  # ndim gives the number of dimensions of the array
print(arr.dtype) # dtype gives the data type of the array
print(arr.size) # size gives the total number of elements in the array
print(arr.shape) # shape gives the dimensions of the array in tuple form
print(arr.itemsize) # itemsize gives the size of each element in bytes
print(arr.nbytes) # nbytes gives the total size of the array in bytes
print(arr.shape) # shape gives the dimensions of the array in tuple form
#for complex numbers you can use complex64 or complex128
print(arr1)
print(arr.ndim)
print(arr.dtype)
x=[[1,2,3,4,5],[6,7,8,9,10]]
arr2=np.array(x)
print(arr2)
print('Dim:',arr2.ndim)
print(arr2.dtype)

#ARRAYS by ones()
arr3=np.ones([2,3,2],dtype='int32')  # creates an array of ones with the given shape and data type
arr4=np.ones([2,3,2])
arr5=np.zeros([2,3,2])  # creates an array of zeros with the given shape and data type
print(arr3)
print(arr4)
arr6=np.empty([3,2,2]) # creates an empty array with the given shape and data type
print(arr6)
arr7=np.full([3,2,2],4)  # creates an array filled with the given value
print(arr7)

arr8=np.eye(3)  # creates a 2D array with ones on the diagonal and zeros elsewhere
#print(arr8)
arr9=np.eye(5,5,1)
#print(arr9)

arr10=np.eye(5,5,-1)
print(arr10) # creates a 2D array with ones on the diagonal and zeros elsewhere, with an shift of main diagonal by 1
arr11 = np.identity(4)  # creates a 2D array with ones on the diagonal and zeros elsewhere
print(arr11)

#ARRAYS by diagonal()
arr12 = np.diag([1, 2, 3, 4])
print(arr12)
x1=[[1,2,3,4],[2,3,4,5]]# creates a 2D array with the given values on the diagonal
arr13 = np.diag(x1)
print(arr13)
#array by arange()
arr14 = np.arange(10)  # creates a 1D array with values from 0 to 9
print(arr14)
arr15 = np.arange(10, 20)  # creates a 1D array with values from 10 to 19
print(arr15)
arr16 = np.arange(10, 20, 2)  # creates a 1D array with values from 10 to 19 with a step of 2
print(arr16)
#arr16[1:3]=13
print(arr16)  # modifies the values at index 1 and 2 to 13
#slicing the array
#x1[0:3,1:3]=123
#print(x1)  # modifies the values at index 0 to 2 and 1 to 2 to 123"""
#create an array matrix of 6x6 all thee elements are 0 but borders are 1
arr17=np.zeros(6*6).reshape(6,6)  # creates a 2D array with zeros
arr17[0:1,:] =1 # sets the first row  to 1 {row,colum}
arr17[5:,:] =1
arr17[:,0:1] =1 # sets the first row  to 1 {row,colum}
arr17[:,5:]=1
print(arr17)
