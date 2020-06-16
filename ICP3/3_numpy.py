"""
CSEE 5590 0002 Python for Deep Learning
ICP 3
author: Srichakradhar Reddy
student ID: 16298670
email: snp8b@umsystem.edu

Using NumPy create random vector of size 20 having only float
in the range 1-20. Then reshape the array to 4 by 5
Then replace the max in each row by 0(axis=1)
"""

import numpy as np


def replace_maxmium(array, replace_value, axis):
    """ choose from x or y depending on condition: np.where(condition, x, y) """
    output = np.where(array == np.max(
        array, axis=1).reshape(-1, 1), 0 * array, array)
    print(output)


def main():

    # Using NumPy create random vector of size 20 having only float
    # in the range 1-20.

    # continuous uniform distribution in [0, 1).
    # To sample Unif[a, b): (b - a) * random_sample() + a
    random20 = np.random.random_sample(20) * 20 + 1
    print(random20)
    
    # Reshape the array to 4 by 5
    random20_4by5 = random20.reshape((4, 5))
    print(random20_4by5)

    # Replace the max in each row by 0(axis=1)
    replace_maxmium(random20_4by5, 0, 1)


if __name__ == "__main__":
    main()
