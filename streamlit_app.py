import streamlit as st
import math
t = st.number_input("Masukan Tinggi) (cm) ",0)
st.title("Menghitung :blue[Berat Badan] :Manusia:")
r = st.number_input("Masukan Berat Badan) (cm) ",0)
if st.button("Hitung Volume", type="primary"):
  v = math.pi*(r**2)*t
  st.success(f'Berat Badan adalah {v:. 2f}')
