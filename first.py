# Learn the module,comments
#  we use the .py extension to create a python file
#  we use the module to import the code from another file or use the code of another person with the help of pip
# pip is a package manager for python which helps us to install the packages and modules
#  we use the # symbol to write the comments in python
# pip install package_name to install the package pip install pyjokes to install the pyjokes package

print("Hello python I want to learn python")
print("I am learning python with the help of pyjokes package")
print("Hello world")


# print the Number

print(10)
print(20)
a = 78
b = 90
c = a + b
print(c)


import pyjokes

print(pyjokes.get_joke())
#  we can also use the pyjokes package to get the jokes in different languages and categories
print(pyjokes.get_joke(language="en", category="all"))


# Muliti comments

"""
my name is shainky rajput
I am learning python with the help of pyjokes package
I am enjoying learning python

"""


