# Masukkan data anda berupa nama dan nilai sebelum di konversi
name = input("masukkan nama anda :")
nilai = float(input("Masukkan nilai anda :"))
# Mengkonversi nilai anda
if nilai < 60:
    print("Halo",name,"!","Nilai anda setelah di konversi adalah E")
    print("=====Tetap Semangat dan Terus Belajar=====")
elif nilai <= 64:
    print("Halo",name,"!","Nilai anda setelah di konversi adalah C")
elif nilai <= 69:
    print("Halo",name,"!","Nilai anda setelah di konversi adalah C+")
elif nilai <= 74:
    print("Halo",name,"!","Nilai anda setelah di konversi adalah B")
elif nilai <= 79:
    print("Halo",name,"!","Nilai anda setelah di konversi adalah B+")
elif nilai <= 84:
    print("Halo",name,"!","Nilai anda setelah di konversi adalah A-")
elif nilai <= 100:
    print("Halo",name,"!","Nilai anda setelah di konversi adalah A")
    print("=====Pertahankan Prestasimu=====")
else:
    print("Maaf nilai anda tidak valid untuk di konversi !!")