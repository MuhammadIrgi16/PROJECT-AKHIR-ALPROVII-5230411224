import sqlite3

koneksi = sqlite3.connect("database_hewan.db")
kursor = koneksi.cursor()

koneksi.execute('''
                CREATE TABLE HEWAN(
                 id_hewan INTEGER PRIMARY KEY AUTOINCREMENT,
                 nama_hewan VARCHAR(50),
                 jenis VARCHAR(50),
                 asal VARCHAR(50),
                 jml_sekarang INTEGER(10),
                 thn_ditemukan INTEGER(10)
                )
                ''')
koneksi.close()