# Bike Sharing Dashboard

Selamat datang di **Bike Sharing Dashboard**!  
Proyek ini merupakan analisis data dari dataset Bike Sharing, yang bertujuan untuk mengungkap insight menarik terkait tren penggunaan sepeda, pengaruh cuaca serta hari kerja/libur, dan pola penggunaan sepeda berdasarkan jam. Dashboard ini dibuat sebagai salah satu syarat submission di Dicoding Bootcamp.

---

## Daftar Isi

- [Overview](#overview)
- [Features](#features)
- [Instalasi](#instalasi)
- [Menjalankan Dashboard](#menjalankan-dashboard)
- [Struktur Proyek](#struktur-proyek)
- [Deployment](#deployment)
- [License](#license)

---

## Overview

Dashboard ini memberikan insight interaktif mengenai:
- **Tren Harian:** Memvisualisasikan fluktuasi penyewaan sepeda setiap harinya, dengan analisis mendalam terhadap pengaruh cuaca dan hari kerja/libur.
- **Pola Per Jam:** Menampilkan rata-rata dan total penyewaan sepeda per jam, sehingga dapat diketahui jam-jam dengan aktivitas penyewaan tertinggi.
- **Analisis Lanjutan:** Analisis tambahan seperti segmentasi berdasarkan hari dalam seminggu untuk mendapatkan insight yang lebih mendalam.

---

## Features

- **Interaktif & Responsif:** Dibangun dengan [Streamlit](https://streamlit.io/) untuk pengalaman pengguna yang dinamis.
- **Visualisasi yang Informatif:** Menggunakan Matplotlib dan Seaborn untuk menghasilkan grafik yang menarik dan mudah dipahami.
- **Insight Bisnis:** Menjawab pertanyaan bisnis utama mengenai tren penggunaan sepeda dan pola penggunaan per jam.
- **Kemudahan Deployment:** Siap dijalankan secara lokal maupun di-deploy ke Streamlit Cloud.

---

## Instalasi

Ikuti langkah-langkah berikut untuk menjalankan dashboard secara lokal:

1. **Clone Repository:**

   ```bash
   git clone https://github.com/yourusername/bike-sharing-dashboard.git
   cd bike-sharing-dashboard

2. **Buat Virtual Environment (Opsional, tapi direkomendasikan):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Untuk Windows: venv\Scripts\activate

3. **Instal Dependencies:**

   ```bash
   pip install -r requirements.txt

---
   
## Menjalankan Dashboard

Untuk menjalankan dashboard, pastikan Anda berada di direktori proyek, lalu eksekusi perintah berikut:

-   ```bash
   streamlit run dashboard/dashboard.py

Setelah itu, dashboard akan terbuka secara otomatis di browser pada alamat http://localhost:8501. Jika tidak, buka browser dan akses URL tersebut secara manual.

---
   
## Struktur Proyek

submission/
├── dashboard/
│   ├── dashboard.py
│   └── main.py
├── data/
│   ├── day.csv
│   ├── hour.csv
│   └── Readme.txt
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt

---
   
## Deployment

Dashboard ini telah dideploy pada Streamlit Cloud untuk memudahkan akses dan berbagi insight dengan publik.
Silakan cek tautan dashboard pada berkas url.txt untuk melihat versi live-nya.

---
   
## License

Proyek ini bersifat open source dan tersedia di bawah MIT License.

---

Selamat menggunakan dashboard ini! Jangan ragu untuk menghubungi saya melalui email jika ada pertanyaan atau masukan.

Happy Exploring! 🚲

-   ```yaml
---
   Dokumentasi di atas memberikan instruksi yang jelas dan menarik untuk pengguna, sekaligus menjelaskan struktur proyek dan fitur yang tersedia. Anda dapat menyesuaikan bagian tertentu (misalnya URL repository atau tautan deployment) sesuai kebutuhan Anda.