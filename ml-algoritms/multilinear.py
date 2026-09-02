import numpy as np
from sklearn.linear_model import LinearRegression

# Features:
# [hours studied, hours slept, attendance]
X = np.array([
    [2, 6, 70],
    [3, 7, 75],
    [4, 7, 80],
    [5, 8, 85],
    [6, 8, 90]
])

# Exam scores
y = np.array([45, 50, 60, 70, 80])

model = LinearRegression()

model.fit(X, y)

# New student
new_student = np.array([[5, 7, 85]])

prediction = model.predict(new_student)

print("Predicted score:", prediction[0])