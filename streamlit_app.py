import streamlit as st

# Judul Aplikasi
st.title("Kalkulator Berat Badan Ideal")

# Input untuk tinggi badan
tinggi_badan = st.number_input("Masukkan tinggi badan (cm):", min_value=100, max_value=250, value=170)

# Pilihan jenis kelamin untuk perhitungan berat badan ideal
jenis_kelamin = st.radio("Pilih Jenis Kelamin", ["Laki-laki", "Perempuan"])

# Menghitung berat badan ideal menggunakan rumus Broca
if jenis_kelamin == "Laki-laki":
    berat_ideal = tinggi_badan - 100 - ((tinggi_badan - 150) / 4)
else:
    berat_ideal = tinggi_badan - 100 - ((tinggi_badan - 150) / 2.5)

# Menampilkan hasil
st.write(f"Berat badan ideal Anda adalah sekitar: {round(berat_ideal, 2)} kg")

# Jika ingin memberikan informasi lebih lanjut tentang BMI (opsional)
st.write("""
**Indeks Massa Tubuh (BMI):**
BMI adalah angka yang dihitung berdasarkan berat badan dan tinggi badan seseorang.
Berikut adalah kategori BMI:
- Kurus: BMI < 18.5
- Normal: 18.5 <= BMI < 24.9
- Kelebihan berat badan: 25 <= BMI < 29.9
- Obesitas: BMI >= 30
""")
