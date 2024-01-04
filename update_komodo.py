# UPDATE table_name
# SET column1 = value1, column2 = value2, ...
# WHERE condition;
import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
koneksi = sqlite3.connect('database_hewan.db')
kursor = koneksi.cursor()

# Data yang ingin diubah
id_hewan = 3
asal_baru = "Nusa Tenggara Timur"

# Menjalankan query UPDATE
kursor.execute(f"UPDATE HEWAN SET asal = '{asal_baru}' WHERE id_hewan = {id_hewan}")
koneksi.commit()

# Menampilkan pesan setelah update berhasil
if kursor.rowcount > 0:
    print(f"Data hewan dengan ID {id_hewan} berhasil diupdate.")
else:
    print(f"Tidak ada data hewan dengan ID {id_hewan}.")

# Menutup koneksi
koneksi.close()
