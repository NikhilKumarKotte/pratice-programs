from sklearn.tree import DecisionTreeClassifier

# [Age, Salary]
X = [
    [20, 20000],
    [25, 25000],
    [30, 40000],
    [35, 50000],
    [40, 60000],
    [45, 70000]
]

# 0 = No
# 1 = Yes
y = [0, 0, 0, 1, 1, 1]

model = DecisionTreeClassifier()

model.fit(X, y)

prediction = model.predict([[32, 45000]])

if prediction[0] == 1:
    print("Customer will buy")
else:
    print("Customer will not buy")