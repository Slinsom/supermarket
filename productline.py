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

# Fungsi untuk menghitung rata-rata rating dan pembelian
def get_average_ratings_and_purchases(product_line):
    ratings = df[df['Product line'] == product_line]['Rating']
    total_purchases = df[df['Product line'] == product_line].shape[0]
    avg_rating = ratings.mean()
    return avg_rating, total_purchases

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

    # Menampilkan rata-rata rating dan pembelian
    avg_rating, avg_purchases = get_average_ratings_and_purchases(product_line)
    st.write(f'Rata-rata rating untuk product line "{product_line}": {avg_rating:.2f}')
    st.write(f'Rata-rata jumlah pembelian untuk product line "{product_line}": {avg_purchases}')
