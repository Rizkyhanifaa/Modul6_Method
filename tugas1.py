# Procedure
# Menampilkan bil ganjil / genap

def bilangan(angka):
    if angka % 2 == 0 :
        print("Bilangan yang anda masukkan adalah Genap")
    else:
        print("Bilangan yang anda masukkan adalah Ganjil")
x = int(input("Masukkan Bilangan : "))
bilangan(x)


