"""
CSEE 5590 0002 Python for Deep Learning
ICP 1

author: Srichakradhar Reddy
student ID: 16298670
email: snp8b@umsystem.edu

A program that accepts a sentence and replace each occurrence of ‘python’ with ‘pythons’
without using regex

• Sample input:
I love playing with python

• Sample output:
I love playing with pythons
"""


def main():
    # get input string
    input_string = input("String: ")

    # split into words
    words = input_string.split(" ")

    # check if words contain python in any case and add "s"
    print(
        " ".join([word + "s" if word.lower() == "python" else word for word in words])
    )


if __name__ == "__main__":
    main()
