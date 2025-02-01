import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from datetime import datetime

# Membaca dataset
day_df = pd.read_csv('../data/day.csv')
hour_df = pd.read_csv('../data/hour.csv')

# Menampilkan 5 Baris Pertama day_df
day_df.head()

# Menampilkan 5 Baris Pertama hour_df
hour_df.head()

day_df.info()
day_df.describe()

hour_df.info()
hour_df.describe()

# Mengonversi kolom tanggal menjadi datetime
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Cek Missing Values pada day_df
day_df.isnull().sum()

# Cek Missing Values pada hour_df
hour_df.isnull().sum()

# Distribusi Jumlah Penyewaan (cnt)
sns.histplot(day_df['cnt'], kde=True, color='skyblue')
plt.title('Distribusi Jumlah Penyewaan (cnt)')
plt.xlabel('Jumlah Penyewaan')
plt.ylabel('Frekuensi')
plt.tight_layout()
plt.show()

# Boxplot untuk variabel numerikal
sns.boxplot(x=day_df['temp'], color='lightgreen')
plt.title('Boxplot Suhu (temp)')
plt.xlabel('Suhu (dalam skala normalisasi)')
plt.tight_layout()
plt.show()

# Countplot untuk kondisi cuaca (weathersit)
sns.countplot(x=day_df['weathersit'], palette='pastel')
plt.title('Distribusi Kondisi Cuaca (weathersit)')
plt.xlabel('Kode Kondisi Cuaca')
plt.ylabel('Jumlah Observasi')
plt.tight_layout()
plt.show()

# Countplot untuk status hari kerja (workingday)
sns.countplot(x=day_df['workingday'], palette='muted')
plt.title('Distribusi Hari Kerja vs Libur')
plt.xlabel('0: Libur, 1: Hari Kerja')
plt.ylabel('Jumlah Hari')
plt.tight_layout()
plt.show()

# Hubungan Antara Variabel Numerikal (temp vs. cnt)
sns.scatterplot(data=day_df, x='temp', y='cnt', hue='weathersit', palette='viridis')
plt.title('Hubungan Suhu (temp) dan Jumlah Penyewaan (cnt)')
plt.xlabel('Suhu (normalisasi)')
plt.ylabel('Jumlah Penyewaan')
plt.tight_layout()
plt.show()

# Perbandingan cnt Berdasarkan Kategori (weathersit)
sns.boxplot(x='weathersit', y='cnt', data=day_df, palette='pastel')
plt.title('Penyewaan (cnt) Berdasarkan Kondisi Cuaca (weathersit)')
plt.xlabel('Kondisi Cuaca (weathersit)')
plt.ylabel('Jumlah Penyewaan')
plt.tight_layout()
plt.show()

# Hubungan antara cnt dan temp Berdasarkan workingday
sns.scatterplot(data=day_df, x='temp', y='cnt', hue='workingday', palette='Set1')
plt.title('Hubungan Suhu dan Penyewaan Berdasarkan Hari Kerja vs Libur')
plt.xlabel('Suhu (normalisasi)')
plt.ylabel('Jumlah Penyewaan')
plt.tight_layout()
plt.show()

# Menghitung matriks korelasi
numeric_df = day_df.select_dtypes(include=[np.number])
corr_matrix = numeric_df.corr()
corr_matrix = day_df.drop(columns=['day_of_week']).corr()

# Menampilkan heatmap korelasi
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Heatmap Korelasi Antar Variabel Numerikal')
plt.tight_layout()
plt.show()

# Memilih variabel yang dianggap penting untuk analisis
selected_columns = ['cnt', 'temp', 'atemp', 'hum', 'windspeed']
sns.pairplot(day_df[selected_columns], diag_kind='kde', corner=True)
plt.suptitle('Pairplot Variabel Utama', y=1.02)
plt.show()

# Menghitung rata-rata penyewaan berdasarkan status hari kerja (workingday)
agg_working = day_df.groupby('workingday')['cnt'].mean().reset_index()
agg_working  # Tampilkan hasil agregasi

# Menghitung rata-rata penyewaan berdasarkan kondisi cuaca (weathersit)
agg_weather = day_df.groupby('weathersit')['cnt'].mean().reset_index()
agg_weather  # Tampilkan hasil agregasi

# Menghitung rata-rata dan total penyewaan per jam
agg_hourly = hour_df.groupby('hr').agg({'cnt': ['mean', 'sum']}).reset_index()
# Ubah kolom menjadi flat (jika diperlukan)
agg_hourly.columns = ['hr', 'avg_cnt', 'total_cnt']
agg_hourly  # Tampilkan hasil agregasi

# Visualisasi 1: Tren Harian & Pengaruh Hari Kerja vs Libur
sns.lineplot(data=day_df, x='dteday', y='cnt', hue='workingday', palette='Set2')
plt.title('Tren Penyewaan Sepeda Harian: Hari Kerja vs Libur')
plt.xlabel('Tanggal')
plt.ylabel('Jumlah Penyewaan')
plt.legend(title="Hari Kerja (1) vs Libur (0)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualisasi 2: Penyewaan Sepeda Berdasarkan Kondisi Cuaca
sns.boxplot(x='weathersit', y='cnt', data=day_df, palette='pastel')
plt.title('Penyewaan Sepeda Berdasarkan Kondisi Cuaca')
plt.xlabel('Kondisi Cuaca (1: Clear, 2: Misty, 3: Light Rain, 4: Heavy Rain)')
plt.ylabel('Jumlah Penyewaan')
plt.tight_layout()
plt.show()

# Menghitung rata-rata penyewaan per jam
hourly_avg = hour_df.groupby('hr')['cnt'].mean().reset_index()
hourly_avg  # Menampilkan hasil agregasi

# Visualisasi 1: Rata-Rata Penyewaan Sepeda per Jam (Line Plot)
sns.lineplot(data=hourly_avg, x='hr', y='cnt', marker='o', color='coral')
plt.title('Rata-Rata Penyewaan Sepeda per Jam')
plt.xlabel('Jam')
plt.ylabel('Rata-Rata Penyewaan')
plt.xticks(range(0, 24))
plt.tight_layout()
plt.show()

# Visualisasi 2: Total Penyewaan Sepeda per Jam (Bar Plot)
sns.barplot(x='hr', y='cnt', data=hour_df, estimator=sum, ci=None, color='mediumseagreen')
plt.title('Total Penyewaan Sepeda per Jam')
plt.xlabel('Jam')
plt.ylabel('Total Penyewaan')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Menambahkan kolom hari dalam seminggu
day_df['day_of_week'] = day_df['dteday'].dt.day_name()

# Agregasi rata-rata penyewaan berdasarkan hari dalam seminggu
avg_by_day = day_df.groupby('day_of_week')['cnt'].mean().reset_index()
avg_by_day

# Visualisasi Agregasi Berdasarkan Hari
sns.barplot(x='day_of_week', y='cnt', data=avg_by_day, palette='viridis')
plt.title('Rata-Rata Penyewaan Sepeda Berdasarkan Hari dalam Seminggu')
plt.xlabel('Hari dalam Seminggu')
plt.ylabel('Rata-Rata Penyewaan')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
