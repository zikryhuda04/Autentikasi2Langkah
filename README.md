# 🔐 Autentikasi 2 Langkah (Two-Factor Authentication) Berbasis GUI - Python

Proyek ini merupakan implementasi sederhana dari **sistem autentikasi dua langkah (2FA)** menggunakan **bahasa Python** dan **antarmuka grafis Tkinter**.  
Tujuannya adalah untuk meningkatkan keamanan proses login dengan menambahkan verifikasi **kode OTP (One-Time Password)** setelah pengguna memasukkan username dan password.

---

## 🚀 Fitur Utama
- Login tahap pertama menggunakan **username dan password**
- Login tahap kedua menggunakan **kode OTP acak 6 digit**
- **Antarmuka GUI** berbasis Tkinter (tidak perlu terminal)
- Validasi input dan notifikasi menggunakan **messagebox**
- Simulasi OTP (ditampilkan di layar, bisa dikembangkan ke pengiriman email/SMS)

---

## 🧩 Alur Program
1. Pengguna membuka aplikasi dan mengisi username serta password.
2. Jika data benar, sistem akan menghasilkan **kode OTP acak**.
3. Kode OTP ditampilkan pada layar (sebagai simulasi).
4. Pengguna memasukkan OTP tersebut ke jendela verifikasi.
5. Jika OTP sesuai, login dinyatakan **berhasil**.

---

## 🧠 Teknologi yang Digunakan
- **Python 3**
- **Tkinter** – untuk GUI
- **Random** – untuk menghasilkan OTP
- **Messagebox** – untuk menampilkan notifikasi (info/error)

---

## 💻 Cara Menjalankan Program
1. Pastikan Python 3 sudah terinstal di komputer kamu.  
   Cek dengan perintah:
   ```bash
   python --version
