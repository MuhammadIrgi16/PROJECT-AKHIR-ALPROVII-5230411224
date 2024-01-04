import sqlite3

koneksi = sqlite3.connect('database_hewan.db')
kursor = koneksi.cursor()

kursor.execute("SELECT * FROM HEWAN ORDER BY nama_hewan ASC")
#menampilan semua data dalam database
baris_tabel = kursor.fetchall()

#buat tabel HEWAN
print('data HEWAN 2023')
print("||","="*111,"||", sep = '')
print("{:<7} {:<20} {:<15} {:<20} {:<20} {:<2}".format("||ID", "Nama Hewan", "Jenis", "Asal", "Jumlah Sekarang", "Tahun Terakhir Ditemukan  ||"))
print("||","="*111,"||", sep = '')

for baris in baris_tabel:
    print("||{:<5} {:<20} {:<15} {:<20} {:<20} {:<26}||".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))

print("||","="*111,"||", sep = '')

koneksi.close()