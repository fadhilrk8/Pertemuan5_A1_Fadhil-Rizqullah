awal = int(input("Masukkan saldo awal\t: "))
sisa = awal #apabila tidak ada pengeluaran
while (True):
    pengeluaran = int(input("Masukkan pengeluaran hari ini (-1 untuk keluar): "))
    if pengeluaran == -1: #untuk break
        print("Sisa saldo", sisa) #apabila break
        break
    sisa = sisa - pengeluaran
    if sisa < 0:
        print("Saldo tidak cukup")
        print("Saldo sisa", sisa + pengeluaran)
        break
