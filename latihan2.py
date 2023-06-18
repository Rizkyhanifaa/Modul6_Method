
# Latihan soal Luas & Keliling Persegi
# Menggunakan Procedure
print('-------')
def keliling_luas_persegi(sisi):
    keliling = 4 * sisi
    luas = sisi * sisi
    print("Keliling = %d" % keliling)
    print("Luas = %d" % luas)

s = int(input("Masukkan panjang sisi :"))
keliling_luas_persegi(s)