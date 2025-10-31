import tkinter as tk
from tkinter import messagebox
import random
import time

# Simulasi database sederhana
USER_DATA = {
    "zikry": "zikry2805"
}

# Simpan kode OTP yang valid
current_otp = None


def generate_otp():
    """Menghasilkan kode OTP 6 digit acak"""
    otp = random.randint(100000, 999999)
    return otp


def verify_login():
    """Verifikasi username dan password"""
    username = entry_username.get()
    password = entry_password.get()

    if username in USER_DATA and USER_DATA[username] == password:
        global current_otp
        current_otp = str(generate_otp())
        messagebox.showinfo("Kode OTP", f"Kode OTP Anda: {current_otp}")
        show_otp_window()
    else:
        messagebox.showerror("Error", "Username atau password salah!")


def verify_otp():
    """Verifikasi kode OTP"""
    otp_input = entry_otp.get()

    if otp_input == current_otp:
        messagebox.showinfo("Sukses", "Login berhasil! 🎉")
        otp_window.destroy()
    else:
        messagebox.showerror("Error", "Kode OTP salah!")


def show_otp_window():
    """Menampilkan jendela OTP"""
    global otp_window, entry_otp

    login_window.withdraw()  # sembunyikan jendela login

    otp_window = tk.Toplevel()
    otp_window.title("Verifikasi OTP")
    otp_window.geometry("300x200")

    tk.Label(otp_window, text="Masukkan kode OTP:", font=("Arial", 12)).pack(pady=10)
    entry_otp = tk.Entry(otp_window, font=("Arial", 12))
    entry_otp.pack(pady=5)

    tk.Button(otp_window, text="Verifikasi", font=("Arial", 12), command=verify_otp).pack(pady=15)


# === GUI utama ===
login_window = tk.Tk()
login_window.title("Login 2 Langkah")
login_window.geometry("350x250")

tk.Label(login_window, text="Login Tahap Pertama", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(login_window, text="Username:", font=("Arial", 12)).pack()
entry_username = tk.Entry(login_window, font=("Arial", 12))
entry_username.pack(pady=5)

tk.Label(login_window, text="Password:", font=("Arial", 12)).pack()
entry_password = tk.Entry(login_window, font=("Arial", 12), show="*")
entry_password.pack(pady=5)

tk.Button(login_window, text="Login", font=("Arial", 12), command=verify_login).pack(pady=15)

login_window.mainloop()
