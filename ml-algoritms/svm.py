from sklearn.svm import SVC

X = [
    [1, 2],
    [2, 3],
    [3, 3],
    [6, 7],
    [7, 8],
    [8, 9]
]

y = [0, 0, 0, 1, 1, 1]

model = SVC(kernel="linear")

model.fit(X, y)

prediction = model.predict([[4, 5]])

print("Predicted class:", prediction[0])