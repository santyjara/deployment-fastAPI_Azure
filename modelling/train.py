import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import datasets
import joblib

# import some data to play with
iris = datasets.load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)


# Create an instance of Logistic Regression Classifier and fit the data.
logreg = LogisticRegression(C=1e5, max_iter=1000)
logreg.fit(X_train, y_train)
print(logreg.score(X_test, y_test))
print(logreg.predict([[30, 20, 10,2]]))

# Save the model
joblib.dump(logreg, "app/model.joblib")
