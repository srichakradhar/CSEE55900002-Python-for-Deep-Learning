"""
CSEE 5590 0002 Python for Deep Learning
ICP 1

author: Srichakradhar Reddy
student ID: 16298670
email: snp8b@umsystem.edu

–Input the string “Python” as a list of characters from console, delete at least 2 characters,
reverse the resultant string and print it.

• Sample input:
python
• Sample output:
ntyp
"""


def main():
    # get input
    input_string = input("String: ")

    print(trim_reverse(input_string))


def trim_reverse(input_string, trim_size=2):

    l = len(input_string)

    # cannot trim more characters than there are
    if trim_size > l:
        print("Cannot trim more than string length:", l)
        return ""

    # slice and reverse the string
    return input_string[: l - trim_size][::-1]


if __name__ == "__main__":
    main()
