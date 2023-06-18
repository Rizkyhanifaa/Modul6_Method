#  Function
# Luas dan Keliling Lingkaran

pi = 3.14

def keliling(jari):
    keliling = (2 * jari) * pi
    return keliling

def luas(jari):
    luas = pi * jari * jari
    return luas 

jari = float(input("Masukkan jari - jari : "))
print("Keliling Lingkaran : ", keliling(jari))
print("Luas Lingkaran : ", luas(jari))
