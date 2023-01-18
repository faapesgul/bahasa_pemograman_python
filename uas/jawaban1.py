"""
function and recursive adalah fungsi dalam kode yang mengacu pada dirinya sendiri untuk dieksekusi. Fungsi rekursif bisa sederhana atau rumit.
Mereka memungkinkan penulisan kode yang lebih efisien, misalnya, dalam daftar atau kompilasi kumpulan angka, string, atau variabel lain melalui satu
proses berulang.
"""


def cetakNamaSaya(x):
    if x == 0:
        return
    else:
        print("Nama Saya Fikri Alam Arya Putra")
        return cetakNamaSaya(x-1)


cetakNamaSaya(5)
