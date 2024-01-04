# UPDATE table_name
# SET column1 = value1, column2 = value2, ...
# WHERE condition;
import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
koneksi = sqlite3.connect('database_hewan.db')
kursor = koneksi.cursor()

# Data yang ingin diubah
id_hewan = 1
jml_baru = 900

# Menjalankan query UPDATE
kursor.execute(f"UPDATE HEWAN SET jml_sekarang = {jml_baru} WHERE id_hewan = {id_hewan}")
koneksi.commit()

# Menampilkan pesan setelah update berhasil
if kursor.rowcount > 0:
    print(f"Data hewan dengan ID {id_hewan} berhasil diupdate.")
else:
    print(f"Tidak ada data hewan dengan ID {id_hewan}.")

# Menutup koneksi
koneksi.close()
