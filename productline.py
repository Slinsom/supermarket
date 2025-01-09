import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv('Supermarket Sales Cleaned.csv')

# Handle missing values by filling with the mean or mode
data.fillna(data.mean(), inplace=True)

# Sidebar for user input
st.sidebar.header('User Input Features')
price = st.sidebar.number_input('Price')
quantity = st.sidebar.number_input('Quantity')
total_sales = st.sidebar.number_input('Total Sales')

# Model training (example with RandomForest)
X = data[['Price', 'Quantity', 'Total']]
y = data['Product line']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Prediction
new_data = pd.DataFrame({'Price': [price], 'Quantity': [quantity], 'Total': [total_sales]})
prediction = model.predict(new_data)
st.write(f'Predicted Product Line: {prediction[0]}')

# Model Evaluation (Accuracy)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
st.write(f'Model Accuracy: {accuracy * 100:.2f}%')

# Visualization: Sales Distribution by Product Line
st.header('Sales Distribution by Product Line')
fig, ax = plt.subplots()
sns.countplot(x='Product line', data=data, ax=ax)
st.pyplot(fig)

# More features can be added similarly
