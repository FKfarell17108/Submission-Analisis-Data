import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi tampilan
sns.set_theme(style="whitegrid")
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# Fungsi untuk memuat data
@st.cache_data
def load_data():
    try:
        # Load daily data
        day_df = pd.read_csv('../data/day.csv')
        day_df['dteday'] = pd.to_datetime(day_df['dteday'])

        # Load hourly data
        hour_df = pd.read_csv('../data/hour.csv')
        hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

        # Mapping nilai kategori
        for df in [day_df, hour_df]:
            df['season'] = df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
            df['weathersit'] = df['weathersit'].map({
                1: 'Clear',
                2: 'Misty',
                3: 'Light Rain',
                4: 'Heavy Rain'
            })

        return day_df, hour_df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame(), pd.DataFrame()

day_df, hour_df = load_data()

# ===== Bagian Header =====
st.title('🚲 Bike Sharing Analytics Dashboard')
st.markdown("---")

# ===== Metrics Section =====
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Penyewaan", f"{day_df['cnt'].sum():,}")
with col2:
    st.metric("Rata-rata Harian", f"{day_df['cnt'].mean():.0f}")
with col3:
    st.metric("Data Harian", f"{len(day_df)} hari")
with col4:
    st.metric("Data Per Jam", f"{len(hour_df):,} observasi")
st.markdown("---")

# ===== Filter Data =====
year_filter = st.selectbox("Pilih Tahun:", options=['Semua'] + sorted(day_df['yr'].unique()))
season_filter = st.multiselect("Pilih Musim:", options=day_df['season'].unique(), default=day_df['season'].unique())

prev_year = 2011 if year_filter == 2012 else None
if prev_year and prev_year in day_df['yr'].unique():
    prev_avg = day_df[day_df['yr'] == prev_year]['cnt'].mean()
    diff = day_df[day_df['yr'] == year_filter]['cnt'].mean() - prev_avg
    st.metric("Rata-rata Harian", f"{day_df['cnt'].mean():.0f}", f"{diff:.0f}")

# Apply filters
filtered_day = day_df.copy()
filtered_hour = hour_df.copy()
if year_filter != 'Semua':
    filtered_day = filtered_day[filtered_day['yr'] == year_filter]
    filtered_hour = filtered_hour[filtered_hour['yr'] == year_filter]
if season_filter:
    filtered_day = filtered_day[filtered_day['season'].isin(season_filter)]
    filtered_hour = filtered_hour[filtered_hour['season'].isin(season_filter)]

# ===== Visualisasi =====
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Trend Harian", "Analisis Musim", "Pengaruh Cuaca", "Pola Per Jam", "Hari Kerja vs Libur"])

with tab1:
    st.subheader("Trend Penyewaan Harian")
    fig, ax = plt.subplots(figsize=(16, 6))
    sns.lineplot(data=filtered_day, x='dteday', y='cnt', ax=ax, color=sns.color_palette("Blues")[2])
    plt.xlabel("Tanggal")
    plt.ylabel("Jumlah Penyewaan")
    plt.xticks(rotation=45) 
    st.pyplot(fig)

with tab2:
    st.subheader("Analisis Musim dan Cuaca")
    if not filtered_day.empty:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(filtered_day.pivot_table(values='cnt', index='season', columns='weathersit', aggfunc='mean'), annot=True, cmap='coolwarm', fmt='.0f')
        plt.xlabel("Kondisi Cuaca")
        plt.ylabel("Musim")
        st.pyplot(fig)
    else:
        st.warning("Data tidak tersedia untuk analisis.")

with tab3:
    st.subheader("Pengaruh Kondisi Cuaca")
    if not filtered_day.empty:
        fig = plt.figure(figsize=(10, 6))
        sns.barplot(data=filtered_day, x='weathersit', y='cnt', ci=None, color=sns.color_palette("Blues")[2])
        plt.xlabel("Kondisi Cuaca")
        plt.ylabel("Rata-rata Penyewaan")
        st.pyplot(fig)
    else:
        st.warning("Data tidak tersedia.")

with tab4:
    st.subheader("Pola Penyewaan Per Jam")
    if not filtered_hour.empty:
        col1, col2 = st.columns(2)
        with col1:
            hourly_avg = filtered_hour.groupby('hr')['cnt'].mean().reset_index()
            fig = plt.figure(figsize=(10, 6))
            sns.lineplot(data=hourly_avg, x='hr', y='cnt', marker='o', color=sns.color_palette("Blues")[2])
            plt.title('Rata-Rata Penyewaan per Jam')
            plt.xlabel('Jam dalam Sehari')
            plt.ylabel('Rata-Rata Penyewaan')
            plt.xticks(range(0, 24))
            st.pyplot(fig)
        with col2:
            fig = plt.figure(figsize=(10, 6))
            sns.barplot(data=filtered_hour, x='hr', y='cnt', ci=None, color=sns.color_palette("Blues")[2])
            plt.title('Jumlah Penyewaan per Jam')
            plt.xlabel('Jam dalam Sehari')
            plt.ylabel('Jumlah Penyewaan')
            plt.xticks(rotation=45)
            st.pyplot(fig)
    else:
        st.warning("Data tidak tersedia untuk analisis pola per jam.")

with tab5:
    st.subheader("Perbandingan Hari Kerja vs. Libur")
    if not filtered_day.empty:
        fig = plt.figure(figsize=(8, 6))
        sns.barplot(data=filtered_day, x='workingday', y='cnt', ci=None)
        plt.xticks([0, 1], ['Hari Libur', 'Hari Kerja'])
        plt.xlabel("Jenis Hari")
        plt.ylabel("Rata-rata Penyewaan")
        st.pyplot(fig)
    else:
        st.warning("Data tidak tersedia.")

# ===== Data Table =====
with st.expander("Lihat Data Mentah"):
    tab1, tab2 = st.tabs(["Data Harian", "Data Per Jam"])
    with tab1:
        st.dataframe(filtered_day)
    with tab2:
        st.dataframe(filtered_hour)

st.markdown("---")
st.caption("Dashboard dibuat menggunakan Streamlit - Bike Sharing Dataset")
