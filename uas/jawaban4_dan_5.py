"""
Aplikasi bisa berkomunikasi dengan database dari sisi Bahasa pemograman python dengan cara :

1. Membangun sebuah koneksi ke database (saya akan menggunakan).
2. Membuat sebuah kursor untuk berkomunikasi dengan data.
3. Memanipulasi data menggunakan SQL.
4. Menetapkan Perubahan.
5. Menutup koneksi ke database.
"""

import os
import sqlite3

db = os.path.join(os.path.dirname(os.path.abspath(__file__)), '_system.db')

# BEGIN JADIKAN KOMENTAR PADA IF-ELSE STATEMENT INI JIKA DATABASE TIDAK INGIN DIHAPUS
if os.path.exists(db):
    os.remove(db)
else:
    print("The file does not exist")
# END JADIKAN KOMENTAR PADA IF ELSE STATEMENT INI JIKA DATABASE TIDAK INGIN DIHAPUS #

conn = sqlite3.connect(db)
curs = conn.cursor()
curs.execute('CREATE TABLE IF NOT EXISTS configurations (name, value)')
values = [('FIKRI', 100), ('ALAM', 90), ('ARYA', 110), ('PUTRA', 80)]
curs.executemany('INSERT INTO configurations VALUES (?, ?)', values)
conn.commit()
rows = curs.execute("SELECT * FROM configurations").fetchall()
print(rows)
conn.close()
