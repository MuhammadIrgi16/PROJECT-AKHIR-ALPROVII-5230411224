# UPDATE table_name
# SET column1 = value1, column2 = value2, ...
# WHERE condition;
import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
koneksi = sqlite3.connect('database_hewan.db')
kursor = koneksi.cursor()

# Data yang ingin diubah
jenis = 'Mamalia'

# Menjalankan query UPDATE
kursor.execute(f"DELETE FROM HEWAN WHERE jenis = '{jenis}'")
koneksi.commit()

# Menampilkan pesan setelah update berhasil
if kursor.rowcount > 0:
    print(f"Data hewan dengan jenis = {jenis} berhasil dihapus.")
else:
    print(f"Tidak ada data hewan dengan jenis = {jenis}.")
# Menutup koneksi
koneksi.close()
