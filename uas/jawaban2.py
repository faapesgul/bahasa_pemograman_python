"""
function of Exception Handling adalah proses menanggapi kejadian yang tidak diinginkan atau tidak terduga saat program komputer dijalankan.
function of Exception Handling berkaitan dengan kejadian ini untuk menghindari program atau sistem yang mogok, dan tanpa proses ini,
exception akan mengganggu operasi normal suatu program.
"""

namas = ['fikri', 'alam', 'arya', 'putra']

try:
    print("Ambil index ke-4 pada nama = %d" % (namas[4]))
except:
    print("error, index ke-4 tidak ada")
