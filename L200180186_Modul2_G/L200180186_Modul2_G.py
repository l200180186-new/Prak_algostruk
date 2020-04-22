class Pesan (object):
    def __init__(self, sebuahString):
        self.text = sebuahString
    def cetakIni(self):
        print(self.text)
    def cetakPakaiHurufKapital(self):
        print(self.text.upper())
    def cetakPakaiHurufKecil(self):
        print(self.txt.lower())
    def jumKar(self):
        return (len(self.text))
    def cetakJumlahKarakterku(self):
        print("Kalimatku mempunyai {} Karakter".format(len(self.text)))
    def Perbaru(self,stringBaru):
        self.text=stringBaru
    def Perbaru(self):
        return "x"
    def apakahTerkandung(self,test):
        return True if test in self.text else False
    def hitungKonsonant(self):
        return len([i for i in self.text.replace(" ","") if i not in "aiueo"])
    def hitungVocal(self):
        return len([i for i in self.text if i in "aiueo"])

class Manusia(object):
    keadaan='lapar'
    def __init__(self,nama):
        self.nama=nama
    def ucapkanSalam(self):
        print("Salam, Namaku ",self.nama)
    def makan(slf,s):
        print("saya baru saja makan ",s)
        self.keadaan='kenyang'
    def olahraga(self,k):
        print('saya barusaja latihan ',k)
        self.keadaan='lapar'
    def mengalikanDenganDua(self,n):
        return n*2
    
class SiswaSMA(Manusia):
    def __init__(self,nama,NIM,us,kota):
        self.nama       = nama
        self.kotaTinggal= kota
        self.uangSaku   = us
    def __str__(self):
        return "{}, Tinggal di {}.Uang saku Rp {} tiap bulannya".format(self.nama,self.kotaTinggal,self.uangSaku)
    def ambilUangSaku   (self):
        return self.uangSaku
    def ambilNama       (self):
        return self.nama
    def makan           (self,a):
        print ("Saya baru saja makan %s sambil belajar"% a)
        self.keadaan = 'kenyang'

class Mahasiswa(Manusia):
    def __init__(self,nama,NIM,kota,us):
        self.nama       = nama
        self.NIM        = NIM
        self.kotaTinggal= kota
        self.uangSaku   = us
        self.listKul    = []
    def __str__(self):
        return "{}, NIM {}. Tinggal di {}. Uang saku Rp {} tiap bulannya".format(self.nama,self.NIM,self.kotaTinggal,self.uangSaku)
    def ambilNIM        (self):
        return self.nama
    def ambilUangSaku   (self):
        return self.uangSaku
    def ambilNama       (self):
        return self.nama
    def makan           (self,a):
        print ("Saya baru saja makan %s sambil belajar"% a)
        self.keadaan = 'kenyang'
    #---------------------------------------------------------------#
    def ambilKotaTinggal(self):
        return self.kotaTinggal
    def perbaruiKotaTinggal(self,a):
        self.kotaTinggal = a
    def tambahUangSaku  (self,b):
        self.uangSaku   += b
    def listKuliah(self):
        return self.listKul
    def ambilKuliah(self,k):
        self.listKul.append(k)
    def hapusKuliah(self,k):
        if k in self.listKul : self.listKul.remove(k)
        
class MhsTIF(Mahasiswa):
    def katakanPy(self):
        print('Python is cool.')

class kelas_kosongan (object):
    pass
k=kelas_kosongan
k.x=23
k.y=47
print(k.x+k.y)
k.mystr='indonesia'
print(k.mystr)

#debugger 1
print(""">>> psn1=Pesan("Indonesia negeri yang indah")
>>> psn1.apakahTerkandung('ege')""")
psn1=Pesan("Indonesia negeri yang indah")
print(psn1.apakahTerkandung('ege'))

print(">>> psn1.apakahTerkandung('eka')")
print(psn1.apakahTerkandung('eka'))
print(">>> psn2=Pesan('surakarta')")
psn2=Pesan('surakarta')
print(">>> psn2.hitungKonsonant()")
print(psn2.hitungKonsonant())
print(">>> psn2.hitungVocal()")
print(psn2.hitungVocal())

print('>>> m9=Mahasiswa("Ucup","L200180186","Karanganyar",200000)')
m9=Mahasiswa("Ucup","L200180186","Karanganyar",200000)
print(m9.ambilKotaTinggal())
m9.perbaruiKotaTinggal("Surakarta")
print(m9.ambilKotaTinggal())
print(m9.ambilUangSaku())
m9.tambahUangSaku(200000)
print(m9.ambilUangSaku())

print("-------")
m9.ambilKuliah("MKP")
print(m9.listKuliah())
m9.hapusKuliah("MK")
print(m9.listKuliah())
m9.hapusKuliah("MKP")
print(m9.listKuliah())
print(m9.ambilUangSaku())
print(m9)
