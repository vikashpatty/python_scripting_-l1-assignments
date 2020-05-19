# Exercise – 2: Filename: ex2.py
# Implement the function isWhiteLine(), which takes a string and returns TRUE if the
# string contains only white space & tab characters.
# Making use of the above function, write a program, which should read a file given as
# command-line argument, and print only non-blank lines onto the standard output.
import sys
def isWhiteLine(s):
    if s.isspace()==True:
        print('True')
    else:
        print('False')
s=str(input('Enter the string: '))
isWhiteLine(s)
