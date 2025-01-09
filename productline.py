import streamlit as st
import pandas as pd

# Memuat dataset yang sudah dibersihkan
df = pd.read_csv('Supermarket Sales Cleaned.csv')

# Membersihkan nama kolom untuk menghindari masalah dengan spasi yang tidak terlihat
df.columns = df.columns.str.strip()

# Fungsi untuk menghitung jumlah pembelian berdasarkan product line dan kota
def count_purchases_by_product_line_and_city(product_line, city):
    count = df[(df['Product line'] == product_line) & (df['City'] == city)].shape[0]
    return count

# Fungsi untuk mendapatkan rating berdasarkan product line dan kota
def get_ratings_by_product_line_and_city(product_line, city):
    ratings = df[(df['Product line'] == product_line) & (df['City'] == city)]['Rating']
    return ratings

# Fungsi untuk mendapatkan metode pembayaran berdasarkan product line dan kota
def get_payments_by_product_line_and_city(product_line, city):
    payments = df[(df['Product line'] == product_line) & (df['City'] == city)]['Payment'].value_counts()
    return payments

# Fungsi untuk mendapatkan detail product line tertentu
def get_product_line_details(product_line):
    total_purchases = df[df['Product line'] == product_line].shape[0]
    payment_methods = df[df['Product line'] == product_line]['Payment'].value_counts()
    cities = df[df['Product line'] == product_line]['City'].value_counts()
    ratings = df[df['Product line'] == product_line]['Rating'].describe()
    return total_purchases, payment_methods, cities, ratings

# Antarmuka Streamlit
st.title('Aplikasi Analisis Product Line dan Pembelian')

city = st.selectbox('Pilih kota:', df['City'].unique())  # Pilihan kota
product_line = st.selectbox('Pilih product line:', df['Product line'].unique())  # Pilihan product line

if product_line:
    # Mendapatkan total pembelian, metode pembayaran, kota, dan rating untuk product line yang dipilih
    total_purchases, payment_methods, cities, ratings = get_product_line_details(product_line)
    st.write(f'Total pembelian untuk product line "{product_line}": {total_purchases}')
    st.write(f'Metode pembayaran untuk product line "{product_line}":')
    st.write(payment_methods)
    st.write(f'Kota dengan pembelian terbanyak untuk product line "{product_line}":')
    st.write(cities)
    st.write(f'Rating untuk product line "{product_line}":')
    st.write(ratings)
