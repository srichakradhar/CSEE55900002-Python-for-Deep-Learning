"""
CSEE 5590 0002 Python for Deep Learning
ICP 2

author: Srichakradhar Reddy
student ID: 16298670
email: snp8b@umsystem.edu

Reads weights (lbs.) of N students into a list and convert these weights
to kilograms in a separate list using:
1) Loops and
2) List comprehensions
N: No of students (Read input from user)
Ex: L1: [150, 155, 145, 148]
Output: [68.03, 70.3, 65.77, 67.13]
"""

def main():
    n_students = input("Number of students: ")
    weights_in_lbs = []

    # Parse the input - check for invalid entries
    try:
        n_students = int(n_students)
    except ValueError:
        print("Please enter a number!")
        exit(1)

    # Read the input weights
    for i in range(n_students):
        weights_in_lbs.append(int(input("Weight of Student " +  str(i + 1) + ": ")))

    # convert from pounds to kgs
    weights_in_kgs = lbs_to_kgs(weights_in_lbs)

    # print the results
    print("Weights in lbs:", weights_in_lbs)
    print("Weights in kgs:", weights_in_kgs)


def lbs_to_kgs(weights):
    """
    Convert weights from Pounds to Kilograms
    
    Parameters:
    @weights: array of float / int values
    
    Outputs:
    Weights converted to kilograms.
    
    """
    return [round(w * 0.453592, 2) for w in weights]

if __name__ == "__main__":
    main()