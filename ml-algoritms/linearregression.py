import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Training data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([20, 35, 45, 60, 75])

# Create model
model = LinearRegression()

# Train
model.fit(X, y)

# Prediction
hours = np.array([[6]])
prediction = model.predict(hours)

print("Predicted score:", prediction[0])

# Visualization
plt.scatter(X, y)
plt.plot(X, model.predict(X))
plt.xlabel("Hours Studied")
plt.ylabel("Score")
plt.title("Linear Regression")
plt.show()