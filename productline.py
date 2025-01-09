import streamlit as st
import pandas as pd

# Memuat dataset yang sudah dibersihkan
df = pd.read_csv('Supermarket Sales Cleaned.csv')

# Membersihkan nama kolom untuk menghindari masalah dengan spasi yang tidak terlihat
df.columns = df.columns.str.strip()

# Fungsi untuk mengklasifikasikan product line berdasarkan nama produk
def classify_product_line(product_name):
    # Mencari product line berdasarkan nama produk (case-insensitive)
    product_line = df[df['Product'].str.contains(product_name, case=False, na=False)]['Product Line'].unique()
    return product_line

# Fungsi untuk menghitung jumlah pembelian berdasarkan product line dan kota
def count_purchases_by_product_line_and_city(product_line, city):
    # Menghitung jumlah baris yang sesuai dengan product line dan kota yang dipilih
    count = df[(df['Product Line'] == product_line) & (df['City'] == city)].shape[0]
    return count

# Fungsi untuk mendapatkan rating berdasarkan product line dan kota
def get_ratings_by_product_line_and_city(product_line, city):
    # Mengambil rating berdasarkan product line dan kota
    ratings = df[(df['Product Line'] == product_line) & (df['City'] == city)]['Rating']
    return ratings

# Fungsi untuk mendapatkan metode pembayaran berdasarkan product line dan kota
def get_payments_by_product_line_and_city(product_line, city):
    # Menghitung jumlah metode pembayaran yang digunakan berdasarkan product line dan kota
    payments = df[(df['Product Line'] == product_line) & (df['City'] == city)]['Payment'].value_counts()
    return payments

# Fungsi untuk mendapatkan detail product line tertentu
def get_product_line_details(product_line):
    # Menghitung total pembelian untuk product line
    total_purchases = df[df['Product Line'] == product_line].shape[0]
    # Menghitung metode pembayaran yang digunakan untuk product line
    payment_methods = df[df['Product Line'] == product_line]['Payment'].value_counts()
    # Menghitung jumlah pembelian berdasarkan kota untuk product line
    cities = df[df['Product Line'] == product_line]['City'].value_counts()
    # Mengambil deskripsi rating untuk product line
    ratings = df[df['Product Line'] == product_line]['Rating'].describe()
    return total_purchases, payment_methods, cities, ratings

# Antarmuka Streamlit
st.title('Aplikasi Klasifikasi Product Line dan Analisis Pembelian')

# Input untuk nama produk
product_name = st.text_input('Masukkan nama produk:')
city = st.selectbox('Pilih kota:', df['City'].unique())  # Pilihan kota
product_line = st.selectbox('Pilih product line:', df['Product Line'].unique())  # Pilihan product line

# Ketika nama produk dimasukkan
if product_name:
    classified_product_line = classify_product_line(product_name)  # Klasifikasikan berdasarkan nama produk
    if classified_product_line.size > 0:
        st.write(f'Product line untuk "{product_name}" adalah: {classified_product_line[0]}')
        
        # Hitung jumlah pembelian berdasarkan product line dan kota yang dipilih
        purchase_count = count_purchases_by_product_line_and_city(classified_product_line[0], city)
        st.write(f'Jumlah pembelian untuk product line "{classified_product_line[0]}" di {city} adalah: {purchase_count}')
        
        # Menampilkan rating untuk product line di kota yang dipilih
        ratings = get_ratings_by_product_line_and_city(classified_product_line[0], city)
        st.write(f'Rating untuk product line "{classified_product_line[0]}" di {city}:')
        st.write(ratings.describe() if not ratings.empty else "Tidak ada data rating.")
        
        # Menampilkan metode pembayaran yang digunakan untuk product line di kota yang dipilih
        payments = get_payments_by_product_line_and_city(classified_product_line[0], city)
        st.write(f'Metode pembayaran untuk product line "{classified_product_line[0]}" di {city}:')
        st.write(payments)
    else:
        st.write(f'Tidak ditemukan product line untuk "{product_name}"')

# Ketika product line dipilih
if product_line:
    # Mendapatkan detail tentang product line yang dipilih
    total_purchases, payment_methods, cities, ratings = get_product_line_details(product_line)
    st.write(f'Total pembelian untuk product line "{product_line}": {total_purchases}')
    st.write(f'Metode pembayaran untuk product line "{product_line}":')
    st.write(payment_methods)
    st.write(f'Kota dengan pembelian terbanyak untuk product line "{product_line}":')
    st.write(cities)
    st.write(f'Rating untuk product line "{product_line}":')
    st.write(ratings)
