import numpy as np
array=np.array([3,"sudhakar",8.00],ndmin=5) #list as ndarray
arr=np.array((6,9,0.4,"vinesh"))    #tuple a ndarray
print(arr)
print(array)
print(type(array))
print(array.ndim)

dict={"id":1,"name":"sudhakar","city":"Andhra"}
#dict.clear()       Removes alla the elemets present in dictionary
print(dict)
d=dict.copy()       #copy the dictionary to a variable or object
d["name"]="vinesh"
print(d)

print(dict.get("name"))     #return the value of a specified key

print(dict.items())         #Return a list containing tuple of each key value pair
print(dict.keys())          #Returns all keys persent in the dictionary

dict.pop("id")      #removes the element with specified key
print(dict)

dict.popitem()      #removes the last inserted key-value pair
print(dict)
dict.update({"name":"ram"})
print(dict)

print(dict.values())