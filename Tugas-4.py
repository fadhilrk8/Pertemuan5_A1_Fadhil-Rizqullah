jumlah_data = int(input("Masukkan jumlah data: "))

total = 0

for i in range(jumlah_data):
    data = float(input(f"Masukkan data ke-{i + 1}: "))
    total += data

rata_rata = total / jumlah_data

print(f"Rata-rata dari {jumlah_data} data adalah {rata_rata}")
