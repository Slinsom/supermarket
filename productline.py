import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Memuat dataset
data = pd.read_csv('Supermarket Sales Cleaned.csv')

# Mengisi nilai NaN untuk kolom numerik dengan rata-rata
data.select_dtypes(include=['number']).fillna(data.mean(), inplace=True)

# Sidebar untuk input pengguna
st.sidebar.header('User Input Features')
price = st.sidebar.number_input('Price')
quantity = st.sidebar.number_input('Quantity')
total_sales = st.sidebar.number_input('Total Sales')

# Melatih model (contoh menggunakan RandomForest)
X = data[['Price', 'Quantity', 'Total']]
y = data['Product line']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Prediksi
new_data = pd.DataFrame({'Price': [price], 'Quantity': [quantity], 'Total': [total_sales]})
prediction = model.predict(new_data)
st.write(f'Predicted Product Line: {prediction[0]}')

# Visualisasi
st.header('Sales Distribution by Product Line')
fig, ax = plt.subplots()
sns.countplot(x='Product line', data=data, ax=ax)
st.pyplot(fig)

# Menambahkan fitur lainnya sesuai kebutuhan
