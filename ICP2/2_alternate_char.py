"""
CSEE 5590 0002 Python for Deep Learning
ICP 2

author: Srichakradhar Reddy
student ID: 16298670
email: snp8b@umsystem.edu

Write a program that returns every other char of a given string starting with first
using a function named “string_alternative”
Str = “Good evening”
Output: Go vnn
Note: You need to create a function named “string_alternative” for this program
and call it from main function.
"""


def main():
    # get the input string from user
    s = input("string input:")

    # use string_alternative function to get output
    print("Output:" + string_alternative(s))

def string_alternative(s):
    return ''.join([s[i] for i in range(0,len(s),2)])

if __name__ == "__main__":
    main()