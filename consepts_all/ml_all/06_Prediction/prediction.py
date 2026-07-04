from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Predict on test data
predictions = model.predict(X_test)
print("Predictions:", predictions)
print("Actual:     ", y_test)

# Predict on new custom input
new_sample = [[5.1, 3.5, 1.4, 0.2]]  # likely setosa
predicted_class = model.predict(new_sample)
print("\nNew sample prediction:", iris.target_names[predicted_class[0]])

# Prediction probabilities
proba = model.predict_proba(new_sample)
print("Probabilities:", proba)
