import tkinter as tk
from tkinter import messagebox

def info_klik():
    messagebox.showinfo("Lune Linux", "Fitur ini akan berjalan setelah instalasi OS selesai!")

# Konfigurasi Window Utama
jendela = tk.Tk()
jendela.title("Welcome to Lune Linux")
jendela.geometry("500x350")
jendela.configure(bg="#0B0C10") # Background dark navy

# Bagian Judul
judul = tk.Label(jendela, text="Welcome to Lune Linux", font=("Helvetica", 20, "bold"), bg="#0B0C10", fg="#66FCF1")
judul.pack(pady=35)

# Bagian Deskripsi
deskripsi = tk.Label(jendela, text="OS Ringan, Estetik, & Produktif untuk Mahasiswa.", font=("Helvetica", 12), bg="#0B0C10", fg="#C5C6C7")
deskripsi.pack(pady=5)

# Tombol Aksi
tombol_mulai = tk.Button(jendela, text="Mulai Kustomisasi", font=("Helvetica", 11, "bold"), bg="#1F2833", fg="#66FCF1", command=info_klik, width=20)
tombol_mulai.pack(pady=20)

tombol_tutup = tk.Button(jendela, text="Tutup", font=("Helvetica", 11), bg="#1F2833", fg="white", command=jendela.destroy, width=20)
tombol_tutup.pack(pady=5)

jendela.mainloop()
