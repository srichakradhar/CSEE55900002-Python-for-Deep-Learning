"""
CSEE 5590 0002 Python for Deep Learning
ICP 3
author: Srichakradhar Reddy
student ID: 16298670
email: snp8b@umsystem.edu

Implement Naïve Bayes and linear SVM methods using scikit-learn library
Use dataset available in https://umkc.box.com/s/ea6wn1cidukan67t02j60nmp1ljln3kdUse
train_test_splitto create training and testing part
Evaluate the model on testing partusing score and
classification_report(y_true, y_pred)
"""

import pandas as pd
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import time
from sklearn import metrics

# read the data
data = pd.read_csv("Python_Lesson4/glass.csv")

print(data.shape)

X_train, X_test = train_test_split(
    data, test_size=0.2, random_state=int(time.time()))

# features columns
features = [
    "RI", "Na", "Mg", "Al", "Si", "K", "Ca", "Ba", "Fe"
]

# Naïve Bayes Classifier
gauss = GaussianNB()

# train the classifier
gauss.fit(
    X_train[features].values,
    X_train["Type"]
)

# make predictions
y_pred = gauss.predict(X_test[features])

print("Naïve Bayes\nTotal number of points: {}\nMislabeled points : {}\nAccuracy {:05.2f}%"
      .format(
          X_test.shape[0],
          (X_test["Type"] != y_pred).sum(),
          100 * (1 - (X_test["Type"] != y_pred).sum() / X_test.shape[0])
      ))

print("\n")

# Naïve Bayes Classifier performance
print(metrics.classification_report(X_test["Type"], y_pred))

# Linear Support Vector Classification
svc_linear = SVC(kernel='linear')

# train linear SVM model
svc_linear.fit(
    X_train[features].values,
    X_train["Type"]
)

Y_pred = svc_linear.predict(X_test[features])

# Linear SVM Model performance
acc_svc = round(svc_linear.score(
    X_test[features].values, X_test["Type"]) * 100, 2)

print("Linear SVM accuracy is:", acc_svc)

# Support vector classifier (SVC) with the radial basis function kernel (RBF)
svc_rbf = SVC(kernel='rbf')
svc_rbf.fit(
    X_train[features].values,
    X_train["Type"]
)

# model predictions
Y_pred = svc_rbf.predict(X_test[features])

# SVM RBF Model performance
acc_svc = round(svc_rbf.score(
    X_test[features].values, X_test["Type"]) * 100, 2)
print("SVM RBF model accuracy is:", acc_svc)
print("\n")

print(metrics.classification_report(X_test["Type"], Y_pred))
