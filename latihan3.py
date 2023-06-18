# Perbandingan Bilangan Lebih Kecil / Besar
def bilangan1(bil1, bil2):
    
    if bil1 > bil2:
        print("Bilangan yang lebih besar adalah ", bil1)
    elif bil1 == bil2:
        print("Tidak ada")
    else:
        print("Bilangan yang lebih besar adalah ", bil2)
awal = int(input("Masukkan Bilangan : "))
akhir = int(input("Masukkan Bilangan : "))
bilangan1(awal, akhir)
