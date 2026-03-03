"""
1. write a program to print the twinkle twinkle little star poem in python
2. use REPL and print the table of 5 using it
3. install the external module and use it to perform an operation of your choice
4. write a program to print the content of directory using the os module search online for the function whixh does that
5. lable the program written in problem 4 with the help of comments

"""

print("""Twinkle, twinkle, little star, how I wonder what you are. Up above the world so high,
like a diamond in the sky. Twinkle, twinkle, little star, how I wonder what you are.
When the blazing sun is set, and the grass with dew is wet. Then you show your little
light, twinkle, twinkle all the night. Twinkle, twinkle little star, how I wonder what you
are.
Then the traveler in the dark thanks you for your tiny spark. How could he see where to
go if you did not twinkle so? Twinkle, twinkle little star, how I wonder what you are.
As your bright and tiny spark lights the traveler in the dark, though I know not what you
are, twinkle, twinkle, little star. Twinkle, twinkle, little star, how I wonder what you are.""")

print("Table of 5")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# installing the pyjokes package and using it to get a joke
import pyjokes
import os
print(pyjokes.get_joke())
# using the os module to print the content of directory
print(os.listdir())


