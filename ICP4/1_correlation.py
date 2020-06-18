import pandas as pd

# read the train data
df = pd.read_csv('Python_Lesson4/train_preprocessed.csv')

print(df.columns)

# Correlation between ‘survived’ (target column) and ‘sex’ column
print(
    df['Survived'].corr(df['Sex'])
)