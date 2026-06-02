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