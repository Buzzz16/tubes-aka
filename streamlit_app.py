import streamlit as st
import time
import sys
import pandas as pd
import altair as alt

# -----------------------------------------------------------------------------
# Konfigurasi Halaman
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Analisis Kompleksitas Algoritma",
    page_icon="⚡",
    layout="wide"  # Menggunakan layout wide untuk grafik yang lebih jelas
)

# -----------------------------------------------------------------------------
# Custom CSS for Premium UI (Dark Mode)
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    /* Global Font */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"]  {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Container Spacing */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 5rem;
    }

    /* Cards Styling (Metrics & Content) - Dark Glassmorphism */
    div[data-testid="stMetric"], div[data-testid="stMarkdownContainer"] > div.stAlert {
        background-color: #1E293B; /* Slate 800 */
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.5);
        border: 1px solid #334155; /* Slate 700 */
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    div[data-testid="stMetric"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5);
        border-color: #0EA5E9; /* Sky 500 */
    }

    /* Headers & Text */
    h1, h2, h3, h4, h5, h6 {
        color: #E0F2FE !important; /* Sky 100 */
    }
    p, li, span, label {
        color: #CBD5E1 !important; /* Slate 300 */
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #0F172A; /* Slate 900 */
        border-right: 1px solid #334155;
    }
    section[data-testid="stSidebar"] h1 {
        color: #F8FAFC !important;
    }
    
    /* Input Fields - Dark Mode */
    .stNumberInput > div > div > input {
        background-color: #1E293B;
        color: #F8FAFC;
        border-radius: 10px;
        border: 1px solid #475569;
    }
    .stNumberInput > div > div > input:focus {
        border-color: #0EA5E9;
        color: #FFFFFF;
        box-shadow: 0 0 0 2px rgba(14, 165, 233, 0.3);
    }
    /* Label Input */
    .stNumberInput label p {
         color: #E2E8F0 !important;
    }

    /* Primary Button Styling - Neon Blue */
    div.stButton > button {
        background: linear-gradient(135deg, #0284C7 0%, #0369A1 100%);
        color: white;
        border-radius: 12px;
        padding: 0.6rem 1.5rem;
        border: 1px solid #0EA5E9;
        font-weight: 600;
        box-shadow: 0 0 10px rgba(14, 165, 233, 0.2);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        width: 100%;
    }
    div.stButton > button:hover {
        background: linear-gradient(135deg, #0EA5E9 0%, #0284C7 100%);
        box-shadow: 0 0 20px rgba(14, 165, 233, 0.6);
        transform: translateY(-1px);
        border-color: #38BDF8;
    }
    div.stButton > button p {
        color: white !important;
    }

    /* Footer */
    footer {visibility: hidden;}
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0F172A;
        color: #64748B;
        text-align: center;
        padding: 15px;
        border-top: 1px solid #1E293B;
        font-size: 0.85rem;
        z-index: 100;
    }
    .footer p {
        color: #64748B !important;
    }
</style>

<div class="footer">
    <p>Tugas Besar Analisis Kompleksitas Algoritma | babas - gathfan © 2025</p>
</div>
""", unsafe_allow_html=True)

# Menambah batas rekusi untuk berjaga-jaga input besar
sys.setrecursionlimit(20000)

# -----------------------------------------------------------------------------
# Definisi Algoritma Core
# -----------------------------------------------------------------------------

def power_recursive(base, exp):
    """Menghitung pangkat secara rekursif."""
    if exp == 0:
        return 1    
    return base * power_recursive(base, exp - 1)

def power_iterative(base, exp):
    """Menghitung pangkat secara iteratif."""
    result = 1
    for i in range(exp):
        result *= base
    return result

# -----------------------------------------------------------------------------
# Helper Functions
# -----------------------------------------------------------------------------

def measure_time(func, *args):
    """Mengukur waktu eksekusi fungsi dalam milidetik."""
    start_time = time.perf_counter()
    result = func(*args)
    end_time = time.perf_counter()
    execution_time_ms = (end_time - start_time) * 1000
    return result, execution_time_ms

# -----------------------------------------------------------------------------
# Halaman: Teori & Pengantar
# -----------------------------------------------------------------------------
def show_theory_page():
    st.title("📚 Teori Kompleksitas Algoritma")
    st.markdown("### Studi Kasus: Bilangan Eksponen ($Base^{Exp}$)")
    
    st.markdown("""
    Dalam ilmu komputer, terdapat berbagai cara untuk menyelesaikan masalah yang sama. 
    Proyek ini membandingkan dua pendekatan untuk menghitung pangkat:
    
    #### 1. Algoritma Iteratif
    - **Konsep:** Menggunakan perulangan (`for` loop) untuk mengalikan basis sebanyak $n$ kali.
    - **Kompleksitas Waktu (Time Complexity):** $O(n)$ - Linear. Waktu eksekusi bertambah secara proporsional dengan besarnya pangkat.
    - **Kompleksitas Ruang (Space Complexity):** $O(1)$ - Konstan. Hanya membutuhkan memori untuk menyimpan variabel hasil.
    """)
    
    st.image("fotoCode/pangkatIteratif.png", caption="Kode Implementasi Iteratif", width=500)
    st.image("fotoCode/psudo-pangkatIteratif.png", caption="Pseudocode Iteratif", width=500)
    
    st.markdown("""
    #### 2. Algoritma Rekursif
    - **Konsep:** Fungsi memanggil dirinya sendiri dengan masalah yang lebih kecil ($n-1$) hingga mencapai basis ($n=0$).
    - **Kompleksitas Waktu:** $O(n)$ - Linear. Melakukan $n$ kali pemanggilan fungsi.
    - **Kompleksitas Ruang:** $O(n)$ - Linear. Membutuhkan stack memory untuk menyimpan setiap pemanggilan fungsi (Call Stack).
    """)

    st.image("fotoCode/pangkatRekursif.png", caption="Kode Implementasi Rekursif", width=500)
    st.image("fotoCode/psudo-pangkatRekursif.png", caption="Pseudocode Rekursif", width=500)
    
    st.markdown("""
    ---
    ### ⚠️ Isu Recursion Overhead
    Meskipun kedua algoritma memiliki Time Complexity $O(n)$, secara praktis **Iteratif seringkali lebih cepat** daripada Rekursif. 
    Hal ini disebabkan oleh **Overhead** pada Rekursif, yaitu biaya sistem untuk:
    1. Membuat stack frame baru.
    2. Menyimpan alamat kembali (return address).
    3. Menyimpan parameter lokal.
    """)

# -----------------------------------------------------------------------------
# Halaman: Single Test
# -----------------------------------------------------------------------------
def show_single_test_page():
    st.title("⚡ Single Input Analysis")
    st.markdown("Uji performa untuk satu kali perhitungan.")

    col1, col2 = st.columns(2)
    with col1:
        # Basis bisa positif/negatif/nol, jadi tidak ada min_value
        basis = st.number_input("Masukkan Basis:", value=2, step=1)
    with col2:
        pangkat = st.number_input("Masukkan Pangkat:", min_value=0, value=900, step=10)

    if st.button("Mulai Analisis", type="primary"):
        # Warning untuk rekursi dalam
        if pangkat > 3000:
            st.warning("⚠️ Pangkat > 3000 dapat menyebabkan RecursionError atau Stack Overflow pada Python standar.")

        try:
            # Hitung Iteratif
            res_iter, time_iter = measure_time(power_iterative, basis, pangkat)
            
            # Hitung Rekursif
            res_rec, time_rec = measure_time(power_recursive, basis, pangkat)

            # Validasi Hasil
            st.divider()
            if res_iter == res_rec:
                 st.success("✅ Hasil perhitungan kedua algoritma valid dan identik.")
            else:
                 st.error("❌ Terjadi ketidakcocokan hasil!")

            # Tampilkan Metrics
            m_col1, m_col2 = st.columns(2)
            with m_col1:
                st.info("🔵 Rekursif")
                st.metric("Waktu Eksekusi", f"{time_rec:.6f} ms")
            
            with m_col2:
                st.success("🟢 Iteratif")
                delta = time_iter - time_rec
                st.metric("Waktu Eksekusi", f"{time_iter:.6f} ms", delta=f"{delta:.6f} ms", delta_color="inverse")

            # Kesimpulan Mini
            st.caption(f"Iteratif lebih {'cepat' if time_iter < time_rec else 'lambat'} {(abs(time_iter - time_rec)):.6f} ms dibandingkan Rekursif.")

            # Visualisasi Bar Chart
            st.divider()
            st.subheader("📊 Visualisasi Perbandingan")
            chart_df = pd.DataFrame({
                "Algoritma": ["Rekursif", "Iteratif"],
                "Waktu Eksekusi (ms)": [time_rec, time_iter]
            })
            
            # Menggunakan Altair untuk custom color yang akurat
            c = alt.Chart(chart_df).mark_bar().encode(
                x=alt.X('Waktu Eksekusi (ms)', axis=alt.Axis(title='Waktu (ms)')),
                y=alt.Y('Algoritma', axis=alt.Axis(title='Metode')),
                color=alt.Color('Algoritma', scale=alt.Scale(domain=['Rekursif', 'Iteratif'], range=['#76b5c5', '#87c55f'])),
                tooltip=['Algoritma', 'Waktu Eksekusi (ms)']
            ).properties(height=200)
            
            st.altair_chart(c, use_container_width=True)

        except RecursionError:
            st.error("❌ Terjadi RecursionError! Stack limit terlampaui. Gunakan pendekatan Iteratif untuk input sebesar ini.")
        except Exception as e:
            st.error(f"Error: {e}")

# -----------------------------------------------------------------------------
# Halaman: Range Analysis (Grafik)
# -----------------------------------------------------------------------------
def show_range_test_page():
    st.title("📈 Range & Graph Analysis")
    st.markdown("Analisis tren pertumbuhan waktu eksekusi terhadap besarnya input.")

    with st.expander("⚙️ Konfigurasi Range Input", expanded=True):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            basis = st.number_input("Basis:", value=2)
        with col2:
            start_exp = st.number_input("Start Pangkat:", value=10)
        with col3:
            end_exp = st.number_input("End Pangkat:", value=2000)
        with col4:
            step_exp = st.number_input("Interval (Step):", value=50)

    if st.button("Generate Grafik & Analisis", type="primary"):
        if start_exp >= end_exp:
            st.error("End Pangkat harus lebih besar dari Start Pangkat.")
            return

        # Data collection
        data_points = []
        progress_bar = st.progress(0)
        
        # Range list
        input_sizes = list(range(start_exp, end_exp + 1, step_exp))
        total_steps = len(input_sizes)

        try:
            for idx, exp in enumerate(input_sizes):
                # Update progress
                progress_bar.progress((idx + 1) / total_steps)

                # Ukur Iteratif
                _, t_iter = measure_time(power_iterative, basis, exp)
                
                # Ukur Rekursif (Skip jika terlalu besar untuk mencegah crash)
                if exp > 5000:
                    t_rec = None 
                else:
                    try:
                        _, t_rec = measure_time(power_recursive, basis, exp)
                    except RecursionError:
                        t_rec = None

                data_points.append({
                    "Input Size (Pangkat)": exp,
                    "Iteratif (ms)": t_iter,
                    "Rekursif (ms)": t_rec
                })

            # Create DataFrame
            df = pd.DataFrame(data_points)

            # 1. Line Chart Visualisasi
            st.subheader("1. Visualisasi Perbandingan (Line Chart)")
            st.line_chart(df.set_index("Input Size (Pangkat)")[["Iteratif (ms)", "Rekursif (ms)"]])

            # 2. Analisis Statistik
            st.subheader("2. Kesimpulan Analisis")
            avg_iter = df["Iteratif (ms)"].mean()
            avg_rec = df["Rekursif (ms)"].dropna().mean()
            
            col_res1, col_res2 = st.columns(2)
            with col_res1:
                st.metric("Rata-rata Waktu Iteratif", f"{avg_iter:.6f} ms")
            with col_res2:
                if pd.notna(avg_rec):
                    st.metric("Rata-rata Waktu Rekursif", f"{avg_rec:.6f} ms")
                    ratio = avg_rec / avg_iter if avg_iter > 0 else 0
                    st.info(f"💡 Secara rata-rata, **Iteratif {ratio:.1f}x lebih cepat** daripada Rekursif pada range ini.")
                else:
                    st.warning("Data rekursif tidak lengkap (mungkin karena limit rekursi).")

            # 3. Tabel Data
            st.subheader("3. Data Mentah")
            st.dataframe(df, use_container_width=True)

        except Exception as e:
            st.error(f"Terjadi kesalahan saat pemrosesan: {e}")

# -----------------------------------------------------------------------------
# Main Routing
# -----------------------------------------------------------------------------
def main():
    # Sidebar Navigation
    st.sidebar.title("Navigasi")
    page = st.sidebar.radio("Pilih Mode:", ["🏠 Teori", "⚡ Single Test", "📈 Range & Grafik"])

    st.sidebar.divider()
    st.sidebar.info("Tugas Besar Analisis Kompleksitas Algoritma")

    if page == "🏠 Teori":
        show_theory_page()
    elif page == "⚡ Single Test":
        show_single_test_page()
    elif page == "📈 Range & Grafik":
        show_range_test_page()

if __name__ == "__main__":
    main()
