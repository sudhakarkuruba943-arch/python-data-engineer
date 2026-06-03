import numpy as np
array1=np.array([1,"vinessh",6.8888])    #list as ndarray
array2=np.array((2,"sudhakar",3.333))   #tuple as ndarray
print(array1)
print(array2)
print(np.__version__)               # define the version of numpy
print(type(array1))

#ndarray with 0-D
arr0=np.array(1)
print(arr0.ndim)        #ndim is used to check the dimension of ndarray

#ndarray with 1-D
arr1=np.array([1,2,3,4])
print(arr1.ndim)

#ndarray with 2-D
arr2=np.array([[0,9,8],[7,6,5]])
print(arr2.ndim)

#ndarray with 3-D
arr3=np.array([[[1,2,3],[4,5,6]],[[0,9,8],[7,6,5]]])
print(arr3.ndim)

#ndarray eith highre dimension
#ndmin argument is used to define the dimensions of an array
arrn=np.array([1,2,3],ndmin=5)
print(arrn)
print(arrn.ndim)

#array access in numpy
# array can be accessed by using indexes and index starts from 0 that means first element index is 0 and second element index is 1 and soo on
arr_acc_0=np.array([9,0,8,5])
print(arr_acc_0[0])     #accessing first element
print(arr_acc_0[1])     #accessing second element
# access in 2D array
arr_acc_1=np.array([[1,2,3],[4,5,6]])
print(arr_acc_1[0,2])

#access in 3D array
arr_acc_2=np.array([[[1,2,3],[4,5,6]],[[0,9,8],[7,6,5]]])
print(arr_acc_2[1,0,0])

#Negative indexing 
#use negative indixing to access an array from the end
print(arr_acc_2[0,0,-1])

#slicing in numpy arrys
#slicing in python means taking elemnets from one given index to anoyher given index
#we pass slice  insted of index like this[start:end]

#[start:end:step]
arr_slice=np.array([1,2,4,5,6,9])
print(arr_slice[1:4])
print(arr_slice[1:])        #if we dont pass end it will take length of array based on dimension
print(arr_slice[:5])        #in we dont pass start it considerd as from 0
print(arr_slice[1:5:2])     #the step ins used to move slicing with stepd specified by default it take 1
#negative slicing also present in numpy arrays

#the Numpy array object has a property called dtype that returns the data type of the array
print(array1.dtype)        

#Creating Arrays with a defined data type
#We use the array() function to create arrays , this function can take an optional argument: dtype that allows  us to define the expected data type  of the array elements
arr_int=np.array([1,2,3,4,5])
print(arr_int.dtype)

arr_str=np.array(arr_int,dtype='S')
print(arr_str,arr_str.dtype)

arr_float=np.array(arr_int,dtype='f8')
print(arr_float,arr_float.dtype)
#for i,u,f,S and U we can define size also

#converting  data type of an existing array
# by using array.astype(data_type) you can change the data type of an existing array
new_arr=arr1.astype('S')
print(new_arr,new_arr.dtype)

#COPY  vs VIEW
#The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of original array
#The copy owns the data and any changes made  in copy will not affect the original array and vice verse
#The view not owns the data and any changes made to the view will affect the original array and vice verse

#COPY
array_main=np.array([1,"sudhakar",4,5,6,0.67])
print(array_main)
array_copy=array_main.copy()
array_main[0]="copy"
print(array_main)
print(array_copy)

#VIEW - changes made in original array
array_main1=np.array([0,8,"vinesh",4.567])
print(array_main1)
array_view=array_main1.view()
array_main1[0]="view"
print(array_main1)
print(array_view)

#VIEW - changes made in view
array_main2=np.array([99,88,77,"ajay"])
print(array_main2)
array_view1=array_main2.view()
array_view1[1]="view"
print(array_main2)
print(array_view1)

#Shape of an array
#The shape of an array is the number of elements in each dimension
#Numpy arrays have an attribute called"shape" that returns a tuple with each index having the number of corresponding elements
array_shape0=np.array([1,2,3,4])
print(array_shape0.shape)

array_shape1=np.array([[1,2,3],[5,6,7]])
print(array_shape1.shape)


#numpy array reshaping
#Reshaping means changing the shape of an array
#The shape of an array is the number of elements in each dimension
# by reshaping we can add or remove dimensions or change number of elements in each dimension
#we can convert array from one shape to another shape by using "reshape()" function with a numpy array object


#Reshpae from 1-D to 2-D
array_reshape1=np.array([6,7,4,8,2,4])
print(array_reshape1.ndim)
print(array_reshape1.shape)
array_re=array_reshape1.reshape(2,3)
print(array_re.ndim)
print(array_re.shape)
print(array_re)

#Reshape from 1-D to 3-D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr.shape)
print(newarr)


#Unknown Dimension
#You are allowed to have one "unknown" dimension.
#Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
#Pass -1 as the value, and NumPy will calculate this number for you.
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr1 = arr1.reshape(2, 2, -1)
print(newarr1)

#Flatting the arrays
#Flattening array means converting a multidimensional array into 1D array
#we can use "reshape(-1)" to do this
array_2D=np.array([[1,2,3],[5,6,7]])
print(array_2D,array_2D.shape)
array_1D=array_2D.reshape(-1)
print(array_1D,array_1D.shape)

#Note: There are a lot of functions for changing the shapes of arrays in numpy flatten, ravel and also for rearranging the elements rot90, flip, fliplr, flipud etc. These fall under Intermediate to Advanced section of numpy.

#Numpy array iterating
#Iterating means going through elements one by one 
#As we deal with multi dimensional arrays in numpy , we can do this by using basic "for" loop of python
#Iterating Arrays using "nditer()"
#the function "nditer" is a helping function that can be used from very basic to very advanced iterations. it solves some basic issues which we face in iterations,lets go through it with examples

#Iterating on each scalar element
#in basic "for" loops, Iterating througheach scalar of an array we need to use n for loops which can be difficult to write for arrays with higher dimensionality
array_iter=np.array([[[1,2,3],[4,5,6]],[[0,9,8],[7,6,5]]])
for x in np.nditer(array_iter):
    print(x)

#Numpy joining array
#Joining means putting contents of two or more arrays in a single array
#we join array based on axes
#we pass a sequence of arrays that we want to join to the concatenate() function , along with the axis . if axis is not explicitly passed it is taken as 0
#concatenate of with out axis 
array_concat1=np.array([11,22,33])
array_concat2=np.array([0,99,88])
print(array_concat1,array_concat2)
array_concat=np.concatenate((array_concat1,array_concat2),axis=0)
print(array_concat)

#conate array with axis
array_con1=np.array([[1,2],[3,4]])
array_con2=np.array([[0,9],[8,7]])
array_concatewith=np.concatenate((array_con1,array_con2),axis=1)
print(array_concatewith)

#Joining Arrays Using Stack Functions
#Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
#We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, ie. stacking.
#We pass a sequence of arrays that we want to join to the stack() method along with the axis. If axis is not explicitly passed it is taken as 0.
array_stack1=np.array([1,2,3,4])
array_stack2=np.array([6,7,8,9])
array_stack=np.stack((array_stack1,array_stack2),axis=1)    #joins a sequence of arrays along a new axis (increase dimensions)
print("array stack joing using stack() function")
print(array_stack)

array_stack_horizontal=np.hstack((array_stack1,array_stack2)) #Numpy provides a helper function : hstack() to stack along rows
print("array stack joining using hstack() function")
print(array_stack_horizontal)

array_stack_vertical=np.vstack((array_stack1,array_stack2))    #Numpy provides a helper function : vstack() to stack along columns
print("array stack joining using vstack() function")
print(array_stack_vertical)

array_stack_depth=np.dstack((array_stack1,array_stack2))     #dstack() to stack along height , which is the same as depth
print("array stack joining using dstack() function")
print(array_stack_depth)
