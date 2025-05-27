import streamlit as st

st.title("selamat datang di web informatika dinda cantik")
st.write("halo aku adinda ini adalah tugas informatika saya")

st.image("628e9904bcbaea08f62d9e30b32f4032.jpg", width=200)

st.title("Aplikasi sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2)== 0:
    st.write(f"{angka} adalah Bilangan Genap")
else:
    st.write(f"{angka} adalah Bilangan Ganjil")
    
