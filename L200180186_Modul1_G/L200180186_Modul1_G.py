#nomer 1
def cetakSiku(x):
    [print("*"*jumlah) for jumlah in range (1,x+1)]
    # print * sebanyak j unutk j di jangkauan 1 hingga x+1

#nomer 2
def gambarlahPersegiEmpat(x,y):
    [print("@"*y) if (i==1 or i==x) else print("@"*(y//y)+" "*(y-2)+"@"*(y//y)) for i in range (1,x+1)]
    # print @ sebanyak y jika i=1 atau i=x jika tidak print(begitu) untuk i dalam jangkauan i hingga x+1 
    
#nomer 3a
import re
def jumlahHurufVokal(StringTest):
    test=re.findall("[a-z]",StringTest.lower())
    return (len(StringTest),  len([i for i in test if i in ("aiueo")]))
    # Kembalikan nilai dari tuple atas jumlah String dan jumlah list dari string yang masuk dalam vokal

#nomer 3b
def jumlahHurufKonsonant(StringTest):
    test=re.findall("[a-z]",StringTest.lower())
    return (len(StringTest),len([i for i in test if i not in ("aiueo")]))
    # Kembalikan nilai dari tuple atas jumlah String dan jumlah list dari string yang masuk dalam Konsonant

#nomer 4
def rerata(daftar):
    return sum(daftar)/len(daftar)
    # Kembalikan nilai dari jumlah list dan bagi dengan jumlah elemen listnya
    
#nomer 5
from math import sqrt
def apakahPrima(x):
    n =int(x)
    assert n>=0
    if n in [2,3,5,7,11]:
        return True
    elif n in [0,1,4,6,8,9,10]:
        return False
    else:
        for i in range (2,int(akar(n)+1)): 
            if n%i==0: return False        # Jika n modulo i sama dengan 0 kembalikan False
        return True

#nomer 6
def primeLoader(x,y):
    daftar=list((range(x,y)))              # Buat list dengan jarak antara x hingga y
    while(x < int(sqrt(y)+1 )):
        if x in daftar:
            [daftar.remove(j) for j in range(x*2, y+1, x) if j in daftar]
            # buang semua angka yg berkelipatan dan masih terdapat didalam daftar
        x += 1
    return daftar

#noemr 7
def faktorPrima(x):
    Hasil=[]
    for i in range(2,(int(akar(x))+1)):
        while x%i==0:
            x=x//i
            Hasil.append(i)
        if apakahPrima(x)==True:
            Hasil.append(x)
            break
    return Hasil

#nomer 8
def apakahTerkandung(check,text):
    return True if check.lower() in text.lower() else False

#nomer 9
def nomer_9():
    for i in range (1,100):
        if i%3==0 and i%5==0:
            print("Python UMS")
        elif i%5==0:
            print ("UMS")
        elif i%3==0:
            print ("Python")
        else:
            print(i)

#nomer 10
from math import sqrt as akar
def selesaikanABC(a,b,c):
    D=float(b**2 -4*a*c)
    return "Determinan negatif, Persamaan tidak memiliki akar real" if D<0 else ((-b+akar(D))/(2*a),(-b -akar(D))/(2*a))

#nomer 11
def apakahKabisat (tahun):
    if (tahun%4==0):
        return False if tahun%100==0 and tahun%400!=0 else True
    else:
        return False

#Nomer 12
from random import randint
def Game():
    Tebak=randint(1,100)
    print("Permainan Tebak Angka.\nSaya menyimpan sebuah angka bulat antara 1 hingga 100. Coba tebak")
    for i in range (0,7):
        tebakan=int(input("Masukan Tebakan ke-%s dari 7:>"% (i+1))  )
        if Tebak>tebakan:
            print("Itu terlalu Kecil. Coba lagi")
        elif Tebak<tebakan:
            print("Itu terlalu Besar. Coba lagi")
        else:
            print("Ya. anda benar")
            break

#Nomer 13
def katakan(angka):
    pengkata    = {"0":"", "1":"satu", "2":"dua", "3":"tiga", "4":"empat", "5":"lima", "6":"enam", "7":"tujuh", "8":"delapan", "9":"sembilan"}
    pembenah    = { "  ratus" : " ",    "  puluh" : " " ,    "satu puluh "   : "sepuluh",
                    "sepuluhsatu"    :"sebelas"         ,    "sepuluhdua"    : "dua belas",
                    "sepuluhtiga"    :"tiga belas"      ,    "sepuluhempat"  : "empat belas",
                    "sepuluhlima"    :"lima belas"      ,    "sepuluhenam"   : "tujuh belas ",
                    "sepuluhtujuh"   :"tujuh belas "    ,    "sepuluhdelapan": "delapan belas",
                    "sepuluhsembilan":"sembilan belas"  ,    "satu ratus"    : "seratus",
                    "satu ribu"      :"seribu"          ,    "  "            : " " }
                    # list yang pengubah 2
                    
    posisi2     = ("","ribu","juta")
    hasil=[pengkata[i] for i in reversed(str(angka))]   # Ganti angka dengan terbilang
    for i in reversed(range(len(hasil))):               #+
        if (i+1)%3==0:                                  #|
            hasil.insert(i,"ratus")                     #| Masukan ratus dan puluh         
        elif (i+1)%3==2:                                #|
            hasil.insert(i,"puluh")                     #+
    for i in reversed(range(len(hasil))):
        if i%5==0:
            hasil.insert(i,posisi2[i//5])               # Masukan ribu dan juta
    hasil=" ".join(reversed(hasil))                     # Balik dan jadikan satu
    for i in pembenah.keys():
        hasil=hasil.replace(i,pembenah[i])              # Benahi kesalahan pengucapan dengan dictionary
    return (hasil[0].upper()+hasil[1:])                 # jika anda mengeluh, saya katakan bahwa ini lebih cepat dari pada rekursi,
                                                        # bukan saya tidak mau menulis rekursi

#nomer 14
def formatRupiah(x):
    return ("Rp. {:,}".format(x)).replace(",",".")      # kembalikan Rp. dengan separator , dan diisi oleh angka x kemudian replace , dengan .

###Debugger "Select barisnya lalu tekan alt + 4 untuk menghilangkan comment"
##cetakSiku(5)                                              # Nomer 1
##gambarlahPersegiEmpat(4,5)                                # Nomer 2
print ( jumlahHurufVokal("Surakarta")     )               # Nomer 3a
print ( jumlahHurufKonsonant("Surakarta") )               # Nomer 3b
##print ( rerata([1,2,3,4,5])               )               # Nomer 4
##print ( apakahPrima(17)                   )               # Nomer 5
##print ( apakahPrima(97)                   )
##print ( apakahPrima(123)                  )
##print ( primeLoader(2,1000)               )               # Nomer 6
##print ( faktorPrima(120)                  )               # Nomer 7
##print ( apakahTerkandung( "io",
##                          "Indonesia tanah air beta"))    # Nomer 8
##nomer_9()                                                 # Nomer 9
##print ( selesaikanABC(1,2,3)              )               # Nomer 10
##print ( apakahKabisat(1900),
##        apakahKabisat(2004),
##        apakahKabisat(2000),
##        apakahKabisat(2003)               )               # Nomer 11
##Game()                                                    # Nomer 12
##print ( katakan(12611050)                 )               # Nomer 13
##print(formatRupiah ( 500            ))                    # Nomer 14
##print(formatRupiah ( 1500           ))
##print(formatRupiah ( 5000000        ))
##print(formatRupiah ( 5000000000000  ))
