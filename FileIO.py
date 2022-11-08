# File I/O (Input/Output)

# Input something from the outside worls
# Output something to the outside world

# Python has a built-in function, open, that allows us to open files

# The below works but is not technically the correct way to read a file
# my_file = open('test.txt')
#
# print(my_file)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
# my_file.seek(0)
# print(my_file.readlines())
# my_file.close()


# This example below is the technically correct way to read files.  With this method, you don't have to close the file
# like in the example above
# with open('test.txt') as my_file:
#     print(my_file.readlines())


# Open has a default parameter of read, if you want to write then you can change the mode to w or r+ to read and write
# with open('test.txt', mode='r+') as my_file:
#     text = my_file.write('hey it\'s me!')
#     print(my_file.readlines())

# Using the append (a) mode will write to the end of the file instead of overwriting what is there already
# with open('test.txt', mode='a') as my_file:
#     text = my_file.write('Hello, is it me you\'re looking for?')

# with open('test.txt', mode='r') as my_file:
#     print(my_file.readlines())

# Using write (w) mode will create a new file if one doesn't exist or completely overwrite the existing file
with open('hello.txt', mode='w') as my_file:
    text = my_file.write('Hello, I am a new file!')

try:
    with open('sad.txt', mode='r') as my_file:
        print(my_file.read())
except FileNotFoundError as error:
    print('File does not exist')
    raise error
except IOError as error:
    print('IO Error')
    raise error
