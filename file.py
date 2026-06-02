#file handling is an important of any web application

#python have several built in function for creating ,reading,updating,and deleting files

#the key function for working with files in python is the "open()" function

#the open() function takes two parameters; filename , and mode

#there are four differnt methods (modes)  for opening a file

#   "r" : Read - defult value. opens a file for reading ,error if the file does not present

#   "a" : Append - opens a file for appending,creates the file if it does not exist

#   "w" : Write - opens a file for writing,creates the if does no exist

#   "x" : Create - creates the specified file ,returns error if the file exists

#   "t" : text - defult value. text mode

#   "b" : - Binary binary mode (e.g. images)

#You can also use "with" statement when opening a file
#they do not have to worry about closing your file ,the with statement take care of that
#you can return one line by using readline() method


#with open(r"C:\Users\Sudhakar\Documents\dbms.txt","r") as f:
 #   print(f.read())

#with open(r"C:\Users\Sudhakar\Documents\dbms.txt","r") as file:
 #   print(file.readline())
  #  print(file.readline())


#create
#a=open(r"C:\Users\Sudhakar\Documents\life.txt","x")

#write
b=open(r"C:\Users\Sudhakar\Documents\life.txt","w")
b.write("my name is sudhakar")

with open(r"C:\Users\Sudhakar\Documents\life.txt","r") as c:
    print(c.read())

