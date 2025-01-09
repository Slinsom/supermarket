import streamlit as st
import pandas as pd

# Memuat dataset yang sudah dibersihkan
df = pd.read_csv('Supermarket Sales Cleaned.csv')

# Membersihkan nama kolom untuk menghindari masalah dengan spasi yang tidak terlihat
df.columns = df.columns.str.strip()

# Fungsi untuk mendapatkan metode pembayaran berdasarkan product line
def get_payments_by_product_line(product_line):
    payments = df[df['Product line'] == product_line]['Payment'].value_counts()
    return payments

# Fungsi untuk mendapatkan detail product line tertentu
def get_product_line_details(product_line):
    payment_methods = df[df['Product line'] == product_line]['Payment'].value_counts()
    return payment_methods

# Fungsi untuk mendapatkan kota berdasarkan product line
def get_cities_by_product_line(product_line):
    cities = df[df['Product line'] == product_line]['City'].value_counts()
    return cities

# Fungsi untuk mendapatkan gender berdasarkan product line
def get_genders_by_product_line(product_line):
    genders = df[df['Product line'] == product_line]['Gender'].value_counts()
    return genders

# Fungsi untuk menghitung rata-rata unit price
def get_average_unit_price(product_line):
    unit_price = df[df['Product line'] == product_line]['Unit price']
    avg_unit_price = unit_price.mean()
    return avg_unit_price

# Fungsi untuk menghitung rata-rata quantity
def get_average_quantity(product_line):
    quantity = df[df['Product line'] == product_line]['Quantity']
    avg_quantity = quantity.mean()
    return avg_quantity

# Fungsi untuk menghitung rata-rata rating
def get_average_rating(product_line):
    ratings = df[df['Product line'] == product_line]['Rating']
    avg_rating = ratings.mean()
    return avg_rating

# Fungsi untuk menghitung rata-rata pembelian
def get_average_purchases(product_line):
    total_purchases = df[df['Product line'] == product_line].shape[0]
    return total_purchases

# Antarmuka Streamlit
st.title('Aplikasi Analisis Product Line dan Pembelian')

# Hanya memilih product line
product_line = st.selectbox('Pilih product line:', df['Product line'].unique())  # Pilihan product line

if product_line:
    # Mendapatkan metode pembayaran untuk product line yang dipilih
    payment_methods = get_product_line_details(product_line)
    st.write(f'Metode pembayaran untuk product line "{product_line}":')
    st.write(payment_methods)

    # Mendapatkan jumlah pembeli berdasarkan kota
    cities = get_cities_by_product_line(product_line)
    st.write(f'Pembeli berdasarkan kota untuk product line "{product_line}":')
    st.write(cities)

    # Mendapatkan jumlah pembeli berdasarkan gender
    genders = get_genders_by_product_line(product_line)
    st.write(f'Pembeli berdasarkan gender untuk product line "{product_line}":')
    st.write(genders)

    # Menampilkan rata-rata unit price
    avg_unit_price = get_average_unit_price(product_line)
    st.write(f'Rata-rata unit price untuk product line "{product_line}": ${avg_unit_price:.2f}')

    # Menampilkan rata-rata quantity
    avg_quantity = get_average_quantity(product_line)
    st.write(f'Rata-rata quantity untuk product line "{product_line}": {avg_quantity:.2f}')
    
    # Menampilkan rata-rata rating
    avg_rating = get_average_rating(product_line)
    st.write(f'Rata-rata rating untuk product line "{product_line}": {avg_rating:.2f}')

    # Menampilkan rata-rata pembelian
    avg_purchases = get_average_purchases(product_line)
    st.write(f'Rata-rata jumlah pembelian untuk product line "{product_line}": {avg_purchases}')
