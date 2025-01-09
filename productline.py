import streamlit as st
import pandas as pd

# Memuat dataset yang sudah dibersihkan
df = pd.read_csv('Supermarket Sales Cleaned.csv')

# Membersihkan nama kolom untuk menghindari masalah dengan spasi yang tidak terlihat
df.columns = df.columns.str.strip()

# Fungsi untuk menghitung jumlah pembelian berdasarkan product line
def count_purchases_by_product_line(product_line):
    count = df[df['Product line'] == product_line].shape[0]
    return count

# Fungsi untuk mendapatkan rating berdasarkan product line
def get_ratings_by_product_line(product_line):
    ratings = df[df['Product line'] == product_line]['Rating']
    return ratings

# Fungsi untuk mendapatkan metode pembayaran berdasarkan product line
def get_payments_by_product_line(product_line):
    payments = df[df['Product line'] == product_line]['Payment'].value_counts()
    return payments

# Fungsi untuk mendapatkan detail product line tertentu
def get_product_line_details(product_line):
    total_purchases = df[df['Product line'] == product_line].shape[0]
    payment_methods = df[df['Product line'] == product_line]['Payment'].value_counts()
    ratings = df[df['Product line'] == product_line]['Rating'].describe()
    return total_purchases, payment_methods, ratings

# Antarmuka Streamlit
st.title('Aplikasi Analisis Product Line dan Pembelian')

# Hanya memilih product line
product_line = st.selectbox('Pilih product line:', df['Product line'].unique())  # Pilihan product line

if product_line:
    # Mendapatkan total pembelian, metode pembayaran, dan rating untuk product line yang dipilih
    total_purchases, payment_methods, ratings = get_product_line_details(product_line)
    st.write(f'Total pembelian untuk product line "{product_line}": {total_purchases}')
    st.write(f'Metode pembayaran untuk product line "{product_line}":')
    st.write(payment_methods)
    st.write(f'Rating untuk product line "{product_line}":')
    st.write(ratings)

//tambahkan untuk melihat rata-rata rating, total penjualan, dan jumlah trasaksi dari product line tersebut, 
