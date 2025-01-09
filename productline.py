import streamlit as st
import pandas as pd

# Memuat dataset yang sudah dibersihkan
df = pd.read_csv('supermarket_sales_cleaned.csv')

# Fungsi untuk mengklasifikasikan product line berdasarkan nama barang
def classify_product_line(product_name):
    product_line = df[df['Product'].str.contains(product_name, case=False, na=False)]['Product Line'].unique()
    return product_line

# Fungsi untuk menghitung jumlah pembelian berdasarkan product line dan kota
def count_purchases_by_product_line_and_city(product_line, city):
    count = df[(df['Product Line'] == product_line) & (df['City'] == city)].shape[0]
    return count

# Fungsi untuk mendapatkan rating berdasarkan product line dan kota
def get_ratings_by_product_line_and_city(product_line, city):
    ratings = df[(df['Product Line'] == product_line) & (df['City'] == city)]['Rating']
    return ratings

# Fungsi untuk mendapatkan jenis pembayaran berdasarkan product line dan kota
def get_payments_by_product_line_and_city(product_line, city):
    payments = df[(df['Product Line'] == product_line) & (df['City'] == city)]['Payment'].value_counts()
    return payments

# Fungsi untuk menampilkan informasi detail tentang product line tertentu
def get_product_line_details(product_line):
    total_purchases = df[df['Product Line'] == product_line].shape[0]
    payment_methods = df[df['Product Line'] == product_line]['Payment'].value_counts()
    cities = df[df['Product Line'] == product_line]['City'].value_counts()
    ratings = df[df['Product Line'] == product_line]['Rating'].describe()
    return total_purchases, payment_methods, cities, ratings

# Antarmuka Streamlit
st.title('Product Line Classification and Purchase Analysis App')

product_name = st.text_input('Enter product name:')
city = st.selectbox('Select city:', df['City'].unique())
product_line = st.selectbox('Select product line:', df['Product Line'].unique())

if product_name:
    classified_product_line = classify_product_line(product_name)
    if classified_product_line.size > 0:
        st.write(f'The product line for "{product_name}" is: {classified_product_line[0]}')
        
        purchase_count = count_purchases_by_product_line_and_city(classified_product_line[0], city)
        st.write(f'The number of purchases for product line "{classified_product_line[0]}" in {city} is: {purchase_count}')
        
        ratings = get_ratings_by_product_line_and_city(classified_product_line[0], city)
        st.write(f'Ratings for product line "{classified_product_line[0]}" in {city}:')
        st.write(ratings.describe())
        
        payments = get_payments_by_product_line_and_city(classified_product_line[0], city)
        st.write(f'Payment methods for product line "{classified_product_line[0]}" in {city}:')
        st.write(payments)
    else:
        st.write(f'No product line found for "{product_name}"')

if product_line:
    total_purchases, payment_methods, cities, ratings = get_product_line_details(product_line)
    st.write(f'Total purchases for product line "{product_line}": {total_purchases}')
    st.write(f'Payment methods for product line "{product_line}":')
    st.write(payment_methods)
    st.write(f'Cities with most purchases for product line "{product_line}":')
    st.write(cities)
    st.write(f'Ratings for product line "{product_line}":')
    st.write(ratings)

# Menjalankan aplikasi Streamlit
# streamlit run app.py 
