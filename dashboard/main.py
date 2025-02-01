# ## Import Semua Packages/Library yang Digunakan
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from datetime import datetime

# ## Data Wrangling:

## Gathering Data
# Membaca dataset
day_df = pd.read_csv('../data/day.csv')
hour_df = pd.read_csv('../data/hour.csv')

# Menampilkan 5 baris pertama untuk masing-masing dataset
print("5 Baris Pertama day_df:")
print(day_df.head())
print("\n5 Baris Pertama hour_df:")
print(hour_df.head())

## Assessing Data
print("\nInformasi dan Ringkasan Statistik untuk day_df:")
print(day_df.info())
print(day_df.describe())

print("\nInformasi dan Ringkasan Statistik untuk hour_df:")
print(hour_df.info())
print(hour_df.describe())

## Cleaning Data
# Mengonversi kolom tanggal menjadi datetime
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Cek missing values
print("\nCek Missing Values pada day_df:")
print(day_df.isnull().sum())
print("\nCek Missing Values pada hour_df:")
print(hour_df.isnull().sum())

# ## Exploratory Data Analysis (EDA)
## Explore ...
# Visualisasi tren penyewaan sepeda harian
plt.figure(figsize=(12, 6))
sns.lineplot(data=day_df, x='dteday', y='cnt', color='steelblue')
plt.title('Tren Penyewaan Sepeda Harian')
plt.xlabel('Tanggal')
plt.ylabel('Jumlah Penyewaan')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ## Visualization & Explanatory Analysis
""" Pertanyaan 1: Bagaimana tren penggunaan sepeda harian selama
periode tertentu dan apakah faktor cuaca serta hari kerja/holiday
berpengaruh signifikan terhadapnya?"""
# Visualisasi 1: Tren Harian & Pengaruh Hari Kerja vs Libur
plt.figure(figsize=(12, 6))
sns.lineplot(data=day_df, x='dteday', y='cnt', hue='workingday', palette='Set2')
plt.title('Tren Penyewaan Sepeda Harian: Hari Kerja vs Libur')
plt.xlabel('Tanggal')
plt.ylabel('Jumlah Penyewaan')
plt.legend(title="Hari Kerja (1) vs Libur (0)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualisasi 2: Penyewaan Sepeda Berdasarkan Kondisi Cuaca
plt.figure(figsize=(10, 6))
sns.boxplot(x='weathersit', y='cnt', data=day_df, palette='pastel')
plt.title('Penyewaan Sepeda Berdasarkan Kondisi Cuaca')
plt.xlabel('Kondisi Cuaca (1: Clear, 2: Misty, 3: Light Rain, 4: Heavy Rain)')
plt.ylabel('Jumlah Penyewaan')
plt.tight_layout()
plt.show()

"""Pertanyaan 2:
Bagaimana pola penggunaan sepeda berdasarkan jam dalam sehari,
dan pada jam berapa terdapat puncak penggunaan?"""
# Menghitung rata-rata penyewaan per jam
hourly_avg = hour_df.groupby('hr')['cnt'].mean().reset_index()

# Visualisasi 1: Rata-Rata Penyewaan Sepeda per Jam (Line Plot)
plt.figure(figsize=(12, 6))
sns.lineplot(data=hourly_avg, x='hr', y='cnt', marker='o', color='coral')
plt.title('Rata-Rata Penyewaan Sepeda per Jam')
plt.xlabel('Jam')
plt.ylabel('Rata-Rata Penyewaan')
plt.xticks(range(0, 24))
plt.tight_layout()
plt.show()

# Visualisasi 2: Total Penyewaan Sepeda per Jam (Bar Plot)
plt.figure(figsize=(12, 6))
sns.barplot(x='hr', y='cnt', data=hour_df, estimator=sum, ci=None, color='mediumseagreen')
plt.title('Total Penyewaan Sepeda per Jam')
plt.xlabel('Jam')
plt.ylabel('Total Penyewaan')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ## Analisis Lanjutan (Opsional)
"""Pengelompokkan Hari Berdasarkan Volume Penyewaan
(Tanpa menggunakan algoritma machine learning kompleks, cukup segmentasi sederhana)"""
day_df['day_of_week'] = day_df['dteday'].dt.day_name()
avg_by_day = day_df.groupby('day_of_week')['cnt'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='day_of_week', y='cnt', data=avg_by_day, palette='viridis')
plt.title('Rata-Rata Penyewaan Sepeda Berdasarkan Hari dalam Seminggu')
plt.xlabel('Hari dalam Seminggu')
plt.ylabel('Rata-Rata Penyewaan')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()