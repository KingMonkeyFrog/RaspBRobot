# RaspBRobot


filename = "data.txt"
file = open(filename, "w")

data = "Hello World"
file.write(data)

file.close()
We use file = open(filename, "w") to open/create a file, then we use file.write(data) to write data to the file. Finaly we use file.close() to close the file.

In the open() function "w" means write data. We can use "a" (append) if you don’t want to delete existing data in an existing file.

 

Here you see a basic example where we Open and Read Data from a File in Python:


filename = "data.txt"
file = open(filename, "r")

data = file.read()
print(data)

file.close()
In the open() function "r" means read data.

 

Typically, when logging data from one or more sensors to file you need to use a While loop:


from time import sleep

filename = "data.txt"
file = open(filename, "w")

while True:
    data = "Hello World\n"
    file.write(data)
    file.flush()
    sleep(5)
    
file.close()
