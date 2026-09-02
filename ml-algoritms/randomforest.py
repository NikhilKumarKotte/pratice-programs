from sklearn.ensemble import RandomForestClassifier

X = [
    [20, 20000],
    [25, 25000],
    [30, 40000],
    [35, 50000],
    [40, 60000],
    [45, 70000]
]

y = [0, 0, 0, 1, 1, 1]

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

prediction = model.predict([[32, 45000]])

print("Prediction:", prediction[0])