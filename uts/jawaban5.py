def jualan():
    a = "capucino"
    b = "teh"
    print("Pilihan")
    print("1.", a)
    print("2.", b)
    print("3. Exit")


def __totalCalculated(value):
    ppn = 10 / 100
    total = value + (value * ppn)
    print("Jumlah yang harus di bayarkan ", total)


def capucino():
    cap = "memilih capucino"
    print(cap)
    capucino = int(input("masukkan harga : "))
    __totalCalculated(capucino)


def teh():
    te = "memilih TEH"
    print(te)
    teh = int(input("masukkan harga : "))
    __totalCalculated(teh)


def welcome():
    nim = 20210801368
    nama = "Fikri Alam Arya Putra"
    print("NIM : ", nim)
    print("NAMA : ", nama)


while True:
    welcome()
    jualan()
    pil = int(input("masukkan pilihan : "))
    if pil == 1:
        capucino()
    elif pil == 2:
        teh()
    elif pil == 3:
        break
    else:
        print("pilihan salah")
