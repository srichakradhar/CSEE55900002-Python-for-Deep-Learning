"""
CSEE 5590 0002 Python for Deep Learning
ICP 3
author: Srichakradhar Reddy
student ID: 16298670
email: snp8b@umsystem.edu

Correlation between ‘survived’(target column) and ‘sex’ column
for the Titanic use case in class
"""

import pandas as pd

# read the train data
df = pd.read_csv('Python_Lesson4/train_preprocessed.csv')

print(df.columns)

# Correlation between ‘survived’ (target column) and ‘sex’ column
print(
    df['Survived'].corr(df['Sex'])
)