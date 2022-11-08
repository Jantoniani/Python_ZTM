import re

# pattern = re.compile('this')
# string = 'search this inside of this text please!'
#
# print('search' in string)
#
# a = pattern.search(string)
# b = pattern.findall(string)
# c = pattern.fullmatch(string)
# d = pattern.match(string)
#
# # Regular Expression gives us a Match object, not just a true or false.  Or will Return None if not match is found
#
# print(a.span())
# print(a.start())
# print(a.end())
# print(a.group())
# print(b)
# print(c)
# print(d)

# https://regex101.com > Regular Expression Playground
# https://regexone.com/ > Interactive RegEx


# Password Checker

# Password must be at least 8 characters long
# Password can contain any sort of letters, numbers, $%#@
# Password must end with a number

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = 'Andrei'
pattern2 = re.compile(r"[A-Za-z0-9$%#@]{8,}\d")

password = 'efwibhno'

a = pattern.search(string)
check = pattern2.fullmatch(password)
print(check)