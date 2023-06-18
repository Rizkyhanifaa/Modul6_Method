# Kalkulator sederhana
# Procedure
def pil(bil1, bil2):
    if pilihan == '1' :
        hasil = bil1 + bil2
        print("Hasil Penjumlahan : ", hasil)
    elif pilihan == '2':
        hasil = bil1 * bil2
        print("Hasil Perkalian : ", hasil)
    elif pilihan == '3':
        hasil = bil1 / bil2
        print("Hasil Pembagian : ", hasil)
    elif pilihan == '4':
        hasil = bil1-bil2
        print("Hasil Pengurangan : ", hasil)
    elif pilihan == '5':
        hasil = bil1 ** bil2
        print("Hasil Perpangkatan : ", hasil)
    else:
        print("Operasi tidak ditemukan")

while(True):
    print("\n-------- KALKULATOR -------- ")
    print("1. Penjumlahan")
    print("2. Perkalian")
    print("3. Pembagian")
    print("4. Pengurangan")
    print("5. Pangkat")

    pilihan = input("Masukkan pilihan : ")
    pertama =  int(input("\nBilangan pertama : "))
    kedua = int(input("Bilangan kedua : "))

    pil(pertama, kedua) 

    ulangi = input("Apakah akan menghitung lagi ? (ya / tidak) :")
    if ulangi.lower() == "tidak" :
        break

 





