<div align="center">

# ⚡ Analisis Kompleksitas Algoritma 🚀
### **Iterative vs Recursive Exponentiation**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

<p align="center">
  <img src="https://media.giphy.com/media/dummy/giphy.gif" alt="Algorithm Animation" width="600" onerror="this.style.display='none'"/>
  <br>
  <i>Visualisasi Perbandingan Performa Algoritma Pangkat</i>
</p>

</div>

---

## 📖 Deskripsi Proyek

Selamat datang di repository **Tugas Besar Analisis Kompleksitas Algoritma**! 🎓

Aplikasi ini dirancang dengan antarmuka yang modern dan interaktif menggunakan **Streamlit** untuk membedah performa dua pendekatan algoritma fundamental:
1.  **🔵 Iteratif**: Pendekatan _looping_ klasik.
2.  **🟣 Rekursif**: Pendekatan _self-calling function_.

Kami membandingkan **Running Time** (waktu eksekusi) kedua metode ini untuk melihat siapa yang lebih efisien dalam menangani perhitungan bilangan berpangkat ($Base^{Exp}$).

---

## ✨ Fitur Utama

| Fitur | Deskripsi |
| :--- | :--- |
| 🎛️ **Input Dinamis** | Kontrol penuh untuk nilai `Basis` dan `Pangkat` secara real-time. |
| ⏱️ **Presisi Tinggi** | Pengukuran waktu eksekusi hingga fraksi milidetik. |
| 📊 **Visualisasi Data** | Grafik interaktif untuk membandingkan pertumbuhan waktu eksekusi. |
| 📈 **Range Analysis** | Analisis tren performa dari input kecil hingga besar. |
| 🎨 **UI Modern** | Tampilan *Dark Mode* yang nyaman dengan visualisasi data yang *catchy*. |

---

## 🛠️ Instalasi & Menjalankan

Ikuti langkah mudah berikut untuk memulai:

### 1. Prasyarat
Pastikan Anda memiliki [Python](https://www.python.org/) yang terinstal di sistem Anda.

### 2. Install Dependensi
Buka terminal dan jalankan perintah berikut untuk menginstal pustaka yang dibutuhkan:
```bash
pip install -r requirements.txt
```

### 3. Jalankan Aplikasi 🚀
Nyalakan server Streamlit dengan perintah:
```bash
streamlit run streamlit_app.py
```
Aplikasi akan otomatis terbuka di browser Anda!

---

## 💻 Cuplikan Kode

Berikut adalah inti dari algoritma yang kami bandingkan:

### 🔄 Pangkat Iteratif
```python
def pangkatIteratif(basis, pangkat):
    result = 1
    for i in range(pangkat):
        result *= basis
    return result
```
> **Kompleksitas**: $O(n)$ Time | $O(1)$ Space

### 🔁 Pangkat Rekursif
```python
def pangkatRekursif(basis, pangkat):
    if pangkat == 0:
        return 1    
    return basis * pangkatRekursif(basis, pangkat - 1) 
```
> **Kompleksitas**: $O(n)$ Time | $O(n)$ Space (Stack Overhead)

---

<div align="center">

### 👨‍💻 Kontributor
**Babass - Gathfann**
<br>
2025 © Tubes AKA

[Laporkan Masalah](https://github.com/Start-End-Zero/AnalisisAlgo/issues) · [Request Fitur](https://github.com/Start-End-Zero/AnalisisAlgo/pulls)

</div>
