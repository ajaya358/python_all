print("hello welcome")
a=10
b=20
a
import pandas as pd
df = pd.read_csv("/content/train.csv")

df.head()
df=dt
df.info()
df.isnull().sum()
df.isnull().sum()
df= df.drop(columns="Cabin")
df.head()
df = df.drop(columns=['Name','PassengerId','Ticket'])
df.head()
df.isnull().sum()
df['Age'].fillna(df['Age'].median(),inplace=True)
df.isnull().sum()
df['Embarked'].fillna(df['Embarked'].mode()[0] ,inplace=True)
df.head()
df.isnull().sum()
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df["Sex"]= le.fit_transform(df['Sex'])
df.head()
le.classes_
df["Embarked"]= le.fit_transform(df['Embarked'])
le.classes_
X = df.drop(columns='Survived')
X.head()
Y = df['Survived']
Y.head()
from sklearn.model_selection import train_test_split
X_train,X_val,Y_train,Y_val = train_test_split(X,Y,test_size=0.8,random_state=42)
df.info()
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, Y_train)
from sklearn.metrics import accuracy_score
pred = model.predict(X_val)
accuracy_score(Y_val,pred)
X_train.head()
d=model.predict([[1,0,86,4,4,1.1250,2]])
print(d)
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
model.fit(X_train, Y_train)

importances = model.feature_importances_
print(importances)
feature_importance = pd.DataFrame({
    'feature': X_train.columns,
    'importance': model.feature_importances_
}).sort_values(by='importance', ascending=False)

print(feature_importance)
def ask_and_predict(model):
    print("Answer the following questions:")

    pclass = int(input("Passenger Class (1 = First, 2 = Second, 3 = Third): "))
    sex = input("Sex (male/female): ").lower()
    sex = 1 if sex == "female" else 0  # female=1, male=0

    age = float(input("Age: "))
    sibsp = int(input("No. of siblings/spouses aboard: "))
    parch = int(input("No. of parents/children aboard: "))
    fare = float(input("Fare paid: "))

    embarked = input("Embarked (C = Cherbourg, Q = Queenstown, S = Southampton): ").upper()
    embarked_dict = {"C": 0, "Q": 1, "S": 2}
    embarked = embarked_dict.get(embarked, 2)

    # Create input list
    person = [[pclass, sex, age, sibsp, parch, fare, embarked]]

    # Prediction probability
    prob = model.predict_proba(person)[0][1] * 100

    print(f"\n🚢 **Chances of Survival: {prob:.2f}%**")