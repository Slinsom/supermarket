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

# Fungsi untuk menghitung rata-rata rating, total penjualan, dan jumlah transaksi
def get_additional_info(product_line):
    # Rata-rata rating
    avg_rating = df[df['Product line'] == product_line]['Rating'].mean()
    
    # Total penjualan (asumsi 'Total' adalah kolom untuk total penjualan)
    total_sales = df[df['Product line'] == product_line]['Total'].sum()
    
    # Jumlah transaksi (sama dengan jumlah pembelian)
    transaction_count = df[df['Product line'] == product_line].shape[0]
    
    return avg_rating, total_sales, transaction_count

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
    
    # Mendapatkan informasi tambahan (rata-rata rating, total penjualan, jumlah transaksi)
    avg_rating, total_sales, transaction_count = get_additional_info(product_line)
    
    st.write(f'Rata-rata rating untuk product line "{product_line}": {avg_rating:.2f}')
    st.write(f'Total penjualan untuk product line "{product_line}": {total_sales:.2f}')
    st.write(f'Jumlah transaksi untuk product line "{product_line}": {transaction_count}')
