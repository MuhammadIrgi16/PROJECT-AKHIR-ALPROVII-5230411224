import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
koneksi = sqlite3.connect('database_hewan.db')
kursor = koneksi.cursor()

# Menjalankan query SUM
kursor.execute("SELECT SUM(jml_sekarang) FROM HEWAN")
total_jumlah = kursor.fetchone()[0]

print(f"Total populasi hewan langka = {total_jumlah}")

# Menutup koneksi
koneksi.close()
