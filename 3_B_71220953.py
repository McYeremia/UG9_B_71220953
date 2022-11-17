print ("====== CATATAN BELANJA ======")
print ("====== Daftar 1 ======")
daftarb1 = ['Gunting','Odol','Shampoo','Sabun','Ciduk']
print ("Daftar Belanja 1: ",daftarb1)
print (" ")
print ("====== Daftar 2 ======")
daftarb2 = ['Kopi','Gula','Garam','Micin','Kecap']
print ("Daftar Belanja 2",daftarb2)
print (" ")
print ("Jawab dengan angka [1/2]")
print ("1. Rubah belanjaan")
print ("2. Keluar")
a = input("Masukan Pilihan : ")
if a == 2:
    print
else:
    if a == 1:
        b = input("Masukan nama item ke daftar 1 : ")
        c = int(input("Masukan index yang ingin dirubah : "))
        daftarb1[c]=b
        d = input ("Masukan nama item ke daftar 2 : ")
        e = int(input("Masukan index yang ingin dirubah : "))
        daftarb2[e]=d
        print (" ")
        print ("===== Daftar 1 =====")
        print ("Daftar Belanja 1: ", daftarb1)
        print (" ")
        print ("===== Daftar 2 =====")
        print ("Daftar Belanja 2: ", daftarb2)
    else:
        print ("Wrong Input")
