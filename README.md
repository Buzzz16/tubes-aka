# Analisis Perbandingan Efisiensi Algoritma Iteratif dan Rekursif

## Deskripsi
Proyek ini adalah Tugas Besar (Tubes) mata kuliah **Analisis Kompleksitas Algoritma**.
Aplikasi ini dibangun menggunakan Streamlit untuk memvisualisasikan dan membandingkan efisiensi waktu eksekusi antara algoritma **Iteratif** dan **Rekursif** dalam perhitungan bilangan eksponen.

## Fitur
- Input dinamis untuk nilai Basis dan Pangkat.
- Perhitungan hasil eksponen menggunakan kedua metode.
- Pengukuran presisi waktu eksekusi (Running Time) dalam milidetik.
- Analisis perbandingan langsung antara kedua metode.

## Cara Menjalankan

1.  Pastikan Python sudah terinstal.
2.  Install dependensi yang diperlukan:
    ```bash
    pip install -r requirements.txt
    ```
3.  Jalankan aplikasi Streamlit:
    ```bash
    streamlit run streamlit_app.py
    ```

## Kode Dasar
Implementasi didasarkan pada logika berikut:
- **Iteratif**: Menggunakan loop `for` untuk mengalikan basis sebanyak pangkat kali.
- **Rekursif**: Menggunakan fungsi yang memanggil dirinya sendiri sampai basis case (`exp == 0`) tercapai.
