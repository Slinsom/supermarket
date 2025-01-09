import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv('supermarket.csv')

# Preprocessing
data = pd.get_dummies(data, columns=['Gender', 'Payment'])

# Feature selection
features = ['Unit price', 'Quantity', 'Tax 5%', 'Total', 'cogs', 'gross margin percentage', 'gross income', 'Rating']
X = data[features]
y = data['Product line']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'product_line_classifier.pkl')

# Load model
model = joblib.load('product_line_classifier.pkl')

st.title('Klasifikasi Product Line Penjualan Supermarket')
input_data = {
    'Unit price': st.number_input('Unit price'),
    'Quantity': st.number_input('Quantity'),
    'Tax 5%': st.number_input('Tax 5%'),
    'Total': st.number_input('Total'),
    'cogs': st.number_input('cogs'),
    'gross margin percentage': st.number_input('gross margin percentage'),
    'gross income': st.number_input('gross income'),
    'Rating': st.number_input('Rating')
}

input_df = pd.DataFrame([input_data])

if st.button('Klasifikasikan'):
    prediction = model.predict(input_df)
    st.write(f'Product line yang diprediksi adalah: *{prediction[0]}*')

# Contoh input untuk aplikasi
st.sidebar.title('Contoh Input')
st.sidebar.write('Masukkan data penjualan seperti harga unit, kuantitas, total, dll.')
