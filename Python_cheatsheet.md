## Python cheet sheet

## 15 data types

# str String is immutable

bool

int

float

complex 

# list are mutable, can be changed
```py
groceries = ["brocolli", "zuchini", "pumpkin"]
groceries[0] = "chocolate" # replace element 0 with "chocolate"
groceries.append("chocolate")   # add chocolate at the end
groceries.remove("zuchini")
print(groceries[2]) # access element 2
len(groceries) # returns length
pop #removes last element

list(range(5)) # creates [0,1,2,3,4,5]

```

# tupleS are immutable, can not change over time

```PY
hero_squad = ("Doctor Strange", "The Hulk", "Silver Surfer")
print("The number of heroes in our squad is:", len(hero_squad))
print (hero_squad[1])
```

range

# Dictionaries mutable

```py
laptop_specs = {
    "brand": "Dell",   # Key : Value, Key must be unique
    "model": "G5",
    "CPU": "Intel i7",
    "GPU": "RTX 3090m"
}
print("My laptop's CPU is:", laptop_specs["CPU"])  # acessing
laptop_specs["RAM"] = "32GB"
laptop_specs["HDD"] = "2TB SSD"  # adding
laptop_specs.pop("CPU")



```

# Set:  no specific sequence, can not have duplicate entries

```py
music_playlist = {"Rocket Man - Elton John", "Here Comes The Sun - The Beatles"}
music_playlist.add("Wild World - Cat Stevens")  # add element
music_playlist.remove("Rocket Man - Elton John") # remove element
print("Is Wild World in set:", "Wild World - Cat Stevens" in music_playlist) # returns true
```

frozenset

bytes

bytearray

memoryview

NoneType 

## Operators

    **: exponentiation
    ^: exclusive-or (bitwise)
    %: modulus (returns remainder of division)
    //: divide with integral result (discard remainder)



## interpolate

```py
print(f'I am {365 * 34} days old!')
```

## Concatenate
```py
print("Hello " + "there " + "human!")
```

## Controllflow

# Else IF

```py
age = 40

if age > 100:
    print("You get a super seniors discount!")
elif age > 60:
    print("You get a seniors discount!")
else: # This will be executed only if all above if/elif statements result in False.
    print("Sorry, my young friend you are not eligable for a seniors discount!")

```
# match case


```py
water_pressure = 3

match water_pressure:
    case 1:
        print("Danger: water pressure critically low! Shut down system!")
    case 2:
        print("Warning: water pressure low. Check for leaks!")
    case 3:
        print("Water pressure nominal.")
    case _:                                         # Default value
        print("Unknown water pressure level!")
```

# While loop

```py
count = 0   
while count < 3:
    print("I'M LOOPING!")
    count += 1



count = 0

while True:
    print(count)
    count += 1

    if count > 20:
        # Even though this loop looks like it will until count reaches 100, the break statement jumps in to shut it down when count gets above 20.
        break
```

# for loop

```py
MY_LIST = ["oranges", "lemons", "the bells of St Clemens"]

for item in MY_LIST:
    print(item)

    MY_LIST = ["a", "b", "c"]
for index, element in enumerate(MY_LIST):
    print(f"Index {index}: {element}")
# output: 
# Index 0: a
# Index 1: b
# Index 2: c


for x in range(10):  # Each time the outer loop counts up 1 the inner loop runs 10 times

    outer_count += 1

    for y in range(10):
        inner_count += 1

for number in range(5):
    print(number)  # 0, 1, 2, 3, 4

    # range(start, stop, step)
for i in range(0, 8, 2):
 print(i)  # creates 0, 2, 4, 6, 8

```

## functions
```py
 def greeting(): 
    print("hello")

greeting()
```

# Scope  Children can accdess parents scope

```py
 name = "Alice"  #parent
def greeting(): 
    print("hello " + name)  #child
greeting()
```

# Parnets  can not access childrens scope

```py
def greeting():
    name = "Bob" 
    print("hello " + name)
greeting()
print(name)  # creates an error because name is local to greeting()
```

# Multiple return values


```py
def day_of_week(): 
   day = date.today().strftime('%A')
   if (day == "Wednesday"): 
       return "It is Wednesday my dudes"

   return f"It's {day}"
```

# optional parameter or default argument

```py
def print_greeting(greeting="hi"):
    print(greeting + "!!!")

print_greeting()  # output hi
```
# keyword arguments

```py
def calculate_cost(price, shipping, tax_rate, member_discount): 
    return (price + (price * tax_rate)) + shipping - member_discount


print(calculate_cost(shipping=50, member_discount=20, price=200, tax_rate=0.2))  # the order of the arguments can be changed
```

## string operations

```py

sample_str = 'hello text'

# Check if last character is 't'
     if sample_str[-1] == 't':
    if sample_str.endswith('t'):
       print("Last character is 't' ")

```
## error handling

```py
# try/catch block
user_input  = input('enter your number  ')
try:
    print(100/ int(user_input))
except ValueError:
    print('please only enter numbers with base 10')
except Exception as e: # parent class off all exception, alternative ZeroDivisionErrpor, ValueError                 
    print(f'this causes a {e} error')
    # print('devided by zero') # bad practice
else:
    print('you guessed the right number')
finally:
    print('I will always execute')
```
## OOD, Classes

```py

class Person:
    def __init__(self, age = 26,shoesize = 0):
        self._age = age
        self._shoesize = shoesize

    # def __init__(self, shoesize = 0):
    #     self._shoesize = shoesize

    def get_age(self):
        return self._age

    def set_age(self, newAge):
        if (newAge > 0):
            self._age = newAge
        else:
            print ("New age is not valid!")

    def print_age(self):
        print(f'my age is{self._age}')

def output():
    alex = Person()

    alex.print_age()

    print(alex.get_age())

    alex.set_age(-1)

```

## file Operation
Mode
					Description
			
r
					Opens a file for reading. (default)
			
w
					Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
			
x
					Opens a file for exclusive creation. If the file already exists, the operation fails.
			
a
					Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
			
t
					Opens in text mode. (default)
			
b
					Opens in binary mode.
			
+
					Opens a file for updating (reading and writing)


## pyinstaller

# copies all into single exe

pyinstaller -F yourprogram.py  
or 
pyinstaller -F --paths=<your_path>\Lib\site-packages  yourprogram.py


```py
  File "PIL/ImageTk.py", line 65, in _pyimagingtkcall

_tkinter.TclError: invalid command name "PyImagingPhoto"
_pyimagingtkcall("PyImagingPhoto", self.__photo, block.id)  # line 191

```

## Bash Wrapper

in file 'my_wrapper.sh' :
#!/bin/bash
python relative/path/to/my/module.py

to activate as executable:
chmod +x my_wrapper.sh 

## file read

>>> f = open("test.txt",'r',encoding = 'utf-8')
>>> f.read(4)    # read the first 4 data
'This'

>>> f.read(4)    # read the next 4 data
' is '

>>> f.read()     # read in the rest till end of file
'my first file\nThis file\ncontains three lines\n'

>>> f.read()  # further reading returns empty sting
''
>>> f.tell()    # get the current file position
56

>>> f.seek(0)   # bring file cursor to initial position
0

>>> print(f.read())  # read the entire file
This is my first file
This file
contains three lines

>>> for line in f:
...     print(line, end = '')
...
This is my first file
This file
contains three lines


Python File I/O

In this tutorial, you'll learn about Python file operations. More specifically, opening a file, reading from it, writing into it, closing it, and various file methods that you should be aware of.
Video: Reading and Writing Files in Python
Files

Files are named locations on disk to store related information. They are used to permanently store data in a non-volatile memory (e.g. hard disk).

Since Random Access Memory (RAM) is volatile (which loses its data when the computer is turned off), we use files for future use of the data by permanently storing them.

When we want to read from or write to a file, we need to open it first. When we are done, it needs to be closed so that the resources that are tied with the file are freed.

Hence, in Python, a file operation takes place in the following order:

    Open a file
    Read or write (perform operation)
    Close the file

Opening Files in Python

Python has a built-in open() function to open a file. This function returns a file object, also called a handle, as it is used to read or modify the file accordingly.

>>> f = open("test.txt")    # open file in current directory
>>> f = open("C:/Python38/README.txt")  # specifying full path

We can specify the mode while opening a file. In mode, we specify whether we want to read r, write w or append a to the file. We can also specify if we want to open the file in text mode or binary mode.

The default is reading in text mode. In this mode, we get strings when reading from the file.

On the other hand, binary mode returns bytes and this is the mode to be used when dealing with non-text files like images or executable files.
Mode
					Description
			
r
					Opens a file for reading. (default)
			
w
					Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
			
x
					Opens a file for exclusive creation. If the file already exists, the operation fails.
			
a
					Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
			
t
					Opens in text mode. (default)
			
b
					Opens in binary mode.
			
+
					Opens a file for updating (reading and writing)
			

f = open("test.txt")      # equivalent to 'r' or 'rt'
f = open("test.txt",'w')  # write in text mode
f = open("img.bmp",'r+b') # read and write in binary mode

Unlike other languages, the character a does not imply the number 97 until it is encoded using ASCII (or other equivalent encodings).

Moreover, the default encoding is platform dependent. In windows, it is cp1252 but utf-8 in Linux.

So, we must not also rely on the default encoding or else our code will behave differently in different platforms.

Hence, when working with files in text mode, it is highly recommended to specify the encoding type.

f = open("test.txt", mode='r', encoding='utf-8')

Closing Files in Python

When we are done with performing operations on the file, we need to properly close the file.

Closing a file will free up the resources that were tied with the file. It is done using the close() method available in Python.

Python has a garbage collector to clean up unreferenced objects but we must not rely on it to close the file.

f = open("test.txt", encoding = 'utf-8')
# perform file operations
f.close()

This method is not entirely safe. If an exception occurs when we are performing some operation with the file, the code exits without closing the file.

A safer way is to use a try...finally block.

try:
   f = open("test.txt", encoding = 'utf-8')
   # perform file operations
finally:
   f.close()

This way, we are guaranteeing that the file is properly closed even if an exception is raised that causes program flow to stop.

The best way to close a file is by using the with statement. This ensures that the file is closed when the block inside the with statement is exited.

We don't need to explicitly call the close() method. It is done internally.

with open("test.txt", encoding = 'utf-8') as f:
   # perform file operations

Writing to Files in Python

In order to write into a file in Python, we need to open it in write w, append a or exclusive creation x mode.

We need to be careful with the w mode, as it will overwrite into the file if it already exists. Due to this, all the previous data are erased.

Writing a string or sequence of bytes (for binary files) is done using the write() method. This method returns the number of characters written to the file.

with open("test.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")

# This program will create a new file named test.txt in the current directory if it does not exist. If it does exist, it is overwritten.

# We must include the newline characters ourselves to distinguish the different lines.
# Reading Files in Python

# To read a file in Python, we must open the file in reading r mode.

# There are various methods available for this purpose. We can use the read(size) method to read in the size number of data. If the size parameter is not specified, it reads and returns up to the end of the file.

# We can read the text.txt file we wrote in the above section in the following way:

>>> f = open("test.txt",'r',encoding = 'utf-8')
>>> f.read(4)    # read the first 4 data
'This'

>>> f.read(4)    # read the next 4 data
' is '

>>> f.read()     # read in the rest till end of file
'my first file\nThis file\ncontains three lines\n'

>>> f.read()  # further reading returns empty sting
''

# We can see that the read() method returns a newline as '\n'. Once the end of the file is reached, we get an empty string on further reading.

# We can change our current file cursor (position) using the seek() method. Similarly, the tell() method returns our current position (in number of bytes).

>>> f.tell()    # get the current file position
56

>>> f.seek(0)   # bring file cursor to initial position
0

>>> print(f.read())  # read the entire file
This is my first file
This file
contains three lines

We can read a file line-by-line using a for loop. This is both efficient and fast.

>>> for line in f:
...     print(line, end = '')
...
This is my first file
This file
contains three lines

# In this program, the lines in the file itself include a newline character \n. So, we use the end parameter of the print() function to avoid two newlines when printing.

# Alternatively, we can use the readline() method to read individual lines of a file. This method reads a file till the newline, including the newline character.

f.readline()  # read each line by itself
'This is my first file\n'

f.readline()
'This file\n'

f.readline()
'contains three lines\n'

# 'write each line in a list'
f.readlines()
#output: 
['This is my first file\n', 'This file\n', 'contains three lines\n']

f.writelines(['writes', 'a', 'list', 'of' , 'lines'])
