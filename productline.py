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

# Fungsi untuk mendapatkan metode pembayaran berdasarkan product line
def get_payments_by_product_line(product_line):
    payments = df[df['Product line'] == product_line]['Payment'].value_counts()
    return payments

# Fungsi untuk mendapatkan detail product line tertentu
def get_product_line_details(product_line):
    total_purchases = df[df['Product line'] == product_line].shape[0]
    payment_methods = df[df['Product line'] == product_line]['Payment'].value_counts()
    return total_purchases, payment_methods

# Fungsi untuk mendapatkan kota berdasarkan product line
def get_cities_by_product_line(product_line):
    cities = df[df['Product line'] == product_line]['City'].value_counts()
    return cities

# Fungsi untuk mendapatkan gender berdasarkan product line
def get_genders_by_product_line(product_line):
    genders = df[df['Product line'] == product_line]['Gender'].value_counts()
    return genders

# Fungsi untuk mendapatkan pembelian untuk jenis kelamin tertentu
def get_purchases_by_gender_and_product_line(product_line, gender):
    purchases = df[(df['Product line'] == product_line) & (df['Gender'] == gender)]
    return purchases.shape[0]

# Fungsi untuk menghitung rata-rata pembelian
def get_average_purchases(product_line):
    total_purchases = df[df['Product line'] == product_line].shape[0]
    return total_purchases

# Antarmuka Streamlit
st.title('Aplikasi Analisis Product Line dan Pembelian')

# Hanya memilih product line
product_line = st.selectbox('Pilih product line:', df['Product line'].unique())  # Pilihan product line

if product_line:
    # Mendapatkan total pembelian dan metode pembayaran untuk product line yang dipilih
    total_purchases, payment_methods = get_product_line_details(product_line)
    st.write(f'Total pembelian untuk product line "{product_line}": {total_purchases}')
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

    # Menampilkan jumlah pembelian berdasarkan gender
    gender = st.selectbox('Pilih gender untuk analisis:', df['Gender'].unique())  # Pilihan gender
    if gender:
        purchases_by_gender = get_purchases_by_gender_and_product_line(product_line, gender)
        st.write(f'Jumlah pembelian untuk gender "{gender}" pada product line "{product_line}": {purchases_by_gender}')

    # Menampilkan rata-rata pembelian
    avg_purchases = get_average_purchases(product_line)
    st.write(f'Rata-rata jumlah pembelian untuk product line "{product_line}": {avg_purchases}')
