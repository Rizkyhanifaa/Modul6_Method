
# Latihan soal Luas & Keliling Persegi

# Menggunakan Function
def keliling_persegi(sisi):
    keliling = 4 * sisi
    return keliling

def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

s = int(input("Masukkan panjang sisi :"))
print("Keliling = %d" % keliling_persegi(s))
print("Luas = %d" % luas_persegi(s))

