# Iris classification model


```python
# Load modules
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
```


```python
# Load dataset
path = "../data/iris.csv"
df = pd.read_csv(path)
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>classification</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.4</td>
      <td>3.7</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.8</td>
      <td>3.4</td>
      <td>1.6</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.8</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.1</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.3</td>
      <td>3.0</td>
      <td>1.1</td>
      <td>0.1</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.8</td>
      <td>4.0</td>
      <td>1.2</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Select features and target variable
X = df[['sepal_length','sepal_width','petal_length','petal_width']]
y = df['classification']

# Split the dataset into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)

# Train the Support Vector Machine (SVM) model
model = SVC(gamma='scale')
model.fit(X_train, y_train)

# Use the trained model to make predictions on the test set
predictions = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
conf_matrix = confusion_matrix(y_test, predictions)
print(f"Accuracy: {accuracy}")
print("Confusion Matrix:")
print(conf_matrix)
```

    Accuracy: 0.9666666666666667
    Confusion Matrix:
    [[11  0  0]
     [ 0 12  1]
     [ 0  0  6]]
    

**Remarks:**

- The accuracy of the model is about 96.67%, which is quite high. For the iris dataset, which many typically considered to be an easy classification ML problem, high accuracy is expected.
- From these evaluation results, we can say that the SVC model is performing well on the iris dataset.


```python
# Save the trained model to a pickle file for later use
pd.to_pickle(model, "../models/new_model.pickle")

# Load the model from the pickle file
model = pd.read_pickle("../models/new_model.pickle")

# Take input from user
sepal_length = float(input("Enter sepal_length (cm): "))
sepal_width = float(input("Enter sepal_width (cm): "))
petal_length = float(input("Enter petal_length (cm): "))
petal_width = float(input("Enter petal_width (cm): "))

# Define the feature names
feature_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

# Create a DataFrame for the input data
input_data = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]], columns=feature_names)

# Make a prediction using the input features from the user
result = model.predict(input_data)

print(f"The predicted iris class is: {result}")
```

    The predicted iris class is: ['Iris-versicolor']
    
