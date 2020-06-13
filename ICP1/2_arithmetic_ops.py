"""
CSEE 5590 0002 Python for Deep Learning
ICP 1

author: Srichakradhar Reddy
student ID: 16298670
email: snp8b@umsystem.edu

Takes two numbers from user and perform arithmetic operations on them.
"""


def main():
    # get input
    try:
        a = int(input("Number 1: "))
        b = int(input("Number 2: "))

        # add
        print("Sum:\t\t", a + b)

        # subtract
        print("Difference:\t", a - b)

        # multiply
        print("Product:\t", a * b)

        # divide
        print("Division:\t", a / b)

        # integer division
        print("Fraction:\t", a // b)

        # modulus
        print("Modulus:\t", a % b)

        # power
        print("Power:\t\t", a ** b)

    except ValueError:
        print("Please enter numbers")


if __name__ == "__main__":
    main()
