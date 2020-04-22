import re                                           # +     importing modul re
s = 'sebuah contoh kata:teh!!'                      # +     deklarasi variable s dengan value string value
cocok = re.findall(r'kata:\w\w\w',s)                # +     deklarasi cocok dengan value dari memilikiil fungsi findall pada re dengan 2 parameter, 
                                                    # +     parameter 1 adalah pattern dan dan parameter 2 adalah textnya
if cocok:                                           # -+    jika cocok bernilai True. 
                                                    # -+    boolean True dimemilikiilkan oleh tipe lain asal tidak kosong maupun bernilai 0 untuk int dan "" untuk string 
    print("menemukan", cocok)                       # --+   stdout dengan value menemukan dan digabung dengan value cocok
else:                                               # -+    jika tidak 
    print("tidak menemukan")                        # --+   stdout value tidak menemukan

#page 68 modified code                              < --------------------------------------------------------------------------------------------
def findall(words='',saring=''):                    # +     definisikan fungsi findall dengan 2 parameter (words, saring) bernilai default ''
    cocok = re.findall(saring,words)                # -+    deklarasi cocok dengan value dari memilikiil fungsi findall pada re dengan 2 parameter, 
                                                    # --+   parameter 1 adalah pattern dan dan parameter 2 adalah textnya
    if cocok:                                       # --+   jika cocok bernilai True. 
                                                    # --+  boolean True bisa dilakukan tipe lain asal tidak kosong maupun bernilai 0 untuk int dan "" untuk string 
        print("menemukan", cocok)                   # ---+  stdout dengan value menemukan dan digabung dengan value cocok
    else:                                           # --+   jika tidak 
        print("tidak menemukan")                    # ---+  stdout value tidak menemukan

saring = r'kata:\w\w\w'                             # +     declare saring as a string with value of kata: folowwed by 3 words character
findall("sebuah contoh kata:batagor!!",saring)      # +     ditemukan memilikiil ['kata:bat'] karena syarat terpenuhi karena kata: telah diikuti 3 alfabet karakter
findall("sebuah contoh kata:es teh!!" ,saring)      # +     tidak ada memilikiil karena kata: diikuti oleh 'es ' dimana terdiri dari 2 alfabet dan 1 spasi

del saring, s, findall                              # +     hapus variable agar mudah saat melihat di debugger vscode(AREPL) 

buffer=list()                                       # +     definisikan buffer sebagai list menampung memilikiil

cocok=re.findall(r'eee', 'teeeh')                   # +     cari semua yang memiliki pattern 'eee' pada teeh
buffer.append(cocok)                                # +     tambahkan cocok ( ['eee'] -> karena teeeh memiliki eee ) ke buffer 
cocok=re.findall(r'ehs', 'teeeh')                   # +     cari semua yang memiliki pattern 'eee' pada teeh
buffer.append(cocok)                                # +     tambahkan cocok ( [] -> karena teeeh not memiliki ehs ) ke buffer
cocok=re.findall(r'..h', 'teeeh')                   # +     cari semua yang memiliki pattern 'eee' pada teeh
buffer.append(cocok)                                # +     tambahkan cocok ( ['eeh'] -> karena teeeh memiliki 2 random char then followed with h char) ke buffer
cocok=re.findall(r'\d\d\d','t123h di 2019 bulan 02')# +     cari semua yang memiliki pattern 'eee' pada teeh
buffer.append(cocok)                                # +     tambahkan cocok ( ['123','201'] -> karena 't123h di 2019 bulan 02' memiliki 3 angka berurutan ,saya berpkir kalau fungsi ini memakai pencarian linear ) ke buffer
cocok=re.findall(r'\w\w\w','@@a*bd#def*tghh!!')     # +     cari semua yang memiliki pattern 'eee' pada teeh
buffer.append(cocok)                                # +     tambahkan cocok ( ['def', 'tgh'] -> karena memiliki 3 huruf alfanumerik yang beurutan )to buffer

print(*buffer, sep="\n")                            # +     print tiap item pada buffer dengan pemisah tiap item '\n' (enter di reg ex)

#69

buffer.clear()                                      # +     hapus seluruh isi buffer

cocok=re.findall(r'te+', 'ghdteeeh')                # +     temukan semua 'te' dimana e nya boleh sepanjang apapun 
buffer.append(cocok)                                # +     hasil ['teee'] dimasukan pada buffer
cocok=re.findall(r'e+' , 'teeheeee')                # +     temukan semua 'e' dimana e nya boleh sepanjang apapun
buffer.append(cocok)                                # +     hasil ['ee',''eeee] dimasukan pada buffer
polanya=r'\d\s*\d\s*\d'                             # -+     cari semua yang berpola angka diikuti oleh spasi sebanyak apa pun dan memiliki angka lagi serta spasi sebanyak apapun dan diikuti angka lagi 
                                                    # -+     (sebanyak apapun disini bisa berarti tidak ada)
cocok=re.findall(polanya    ,"xx1 2   3xx")         # +     temukan pola diats pada text parameter ke 2
buffer.append(cocok)                                # +     hasil ['1 2   3'] dimasukan ke buffer
cocok=re.findall(polanya    ,"xx12  3xx")           # +     temukan pola diats pada text parameter ke 2
buffer.append(cocok)                                # +     hasil ['12  3'] dimasukan ke buffer
cocok=re.findall(polanya    ,"xx123xx")             # +     temukan pola diats pada text parameter ke 2
buffer.append(cocok)                                # +     hasil ['123'] dimasukan ke buffer
cocok=re.findall(r'k\w+'    ,"mejakursi")           # +     cari k diikuti dengan alfanumerik apapun sepanjang apapun
buffer.append(cocok)                                # +     hasil ['kursi'] dimasukan ke buffer
cocok=re.findall(r'k[\w\s]+',"mejakursi tamu saya") # +     cari k diikuti dengan boleh oleh alfanumerik, maupun spasi sepanjang apapun dan boleh berulang ulang 
buffer.append(cocok)                                # +     hasil ['kursi tamu saya'] dimasukan ke buffer
 
print(*buffer, sep="\n")                            # +     print tiap item pada buffer dengan pemisah tiap item '\n' (enter di reg ex)

s='Alamatku adalah dita-b@google.com mas'           # +     deklarasi s sebagai string dari 'Alamatku adalah dita-b@google.com mas' 
cocok=re.findall(r'\w+@\w+',s)                      # +     cari pattern alfanumerik sebanyak mungkin dan dikuti oleh @ serta dilanjutkan alfanumerik sebanyak mungkin
 
print(cocok[0])                                     # +     print cocok terakhir dengan index 0

#70

cocok=re.findall(r'([\w.-]+@[\w.]+)',s)             # +     cari pattern dengan ambil semua alfanumerik, titk, dan - di ikuti oleh @ serta alfanumerik, titk, dan - dengan jumlah sebanyak banyaknya
print(cocok[0])                                     # +     print hasil index pertama dari diatas
cocok=re.findall(                                   # +     cari pattern 
    r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9.]+' # +     a sampai z baik besar atau kecil dan angka serta _.+- diikuti oleh @ serta diikuti lagi oleh filter pertama
    ,s)                                             # +     pada    

del buffer, polanya                                 # +     hapus  buffer dan polanya

cocok=re.findall(r'([\w.-]+)@([\w.]+)',s)           # +     cari pattern dengan ambil semua alfanumerik, titk, dan - di ikuti oleh @ serta alfanumerik, titk, dan - dengan jumlah sebanyak banyaknya
print(*cocok,sep='\n')                              # +     print setiap item cocok dan 
s='Alamatku sri@google.com serta joko@abc.com oke bro. atau don@email.com'
pola=r'[\w.-]+@[\w.]+'                              # +     pattern dengan ambil semua alfanumerik, titk, dan - di ikuti oleh @ serta alfanumerik, titk, dan - dengan jumlah sebanyak banyaknya
e = re.findall(pola,s)                              # +     cari dengan pattern pola dan text   
print(e)                                            # +     print hasil e
 
#71

pola=r'([\w.-]+)@([\w.]+)'                          # +     cari pattern dengan ambil semua alfanumerik, titk, dan - di ikuti oleh @ serta alfanumerik, titk, dan - dengan jumlah sebanyak banyaknya
e=re.findall(pola,s)                                # +     cari dengan pattern pola dan text   
print(e)                                            # +     print hasil e
for i in e :                                        # untuk tiap e (dianggap i)
    print ( f'user {i[0]} dengan host: {i[1]}' )    # print dengan format user i[0] dengan host i[1]

del i, cocok, e, pola, s                            # hapus variable i,e,cocok, pola, s





#tugas

import re,time
def getinside(files):
    text_file = open(files,'r',encoding="latin-1")
    text=text_file.read()
    text_file.close()
    return text
text=getinside('bodyIndonesia.txt')
dump=re.findall(r'[^\w]me[\w]+',text)
no_1 = list(dict.fromkeys(dump))
del dump

dump=re.findall(r'[^\w]di\w\w[\w]+',text)
no_2 = list(dict.fromkeys(dump))
del dump

dump=re.findall(r'di \w+',text)
no_3 = list(dict.fromkeys(dump))
del dump, text

text=getinside('Knowledge Economic Index - Wikipedia.html')
class list_negara:
    def __init__(self):
        self.lister=[]
    def add(self,object):
        self.lister.append(object)
    def cetaknegara(self,sample=True):
        buffer=[]
        if sample:
            for i in self.lister[:5]:
                buffer.append(i.nama)
        else:    
            for i in self.lister:
                buffer.append(i.nama)
        print(*buffer, sep="\n")
    def cetakInno(self,sample=True):
        buffer=[]
        if sample:
            for i in self.lister[:5]:
                buffer.append(i.index)
        else:    
            for i in self.lister:
                buffer.append(i.index)
        print(*buffer, sep="\n")
    def maketuple(self):
        buffer=[]
        for i in self.lister:
            buffer.append((i.nama,i.index))
        return buffer
class negara:
    def __init__(self,somethings):
        self.somethings=somethings
        self.nama=re.findall(r'/wiki/[\w_]+',self.somethings)[0][6:]
        try:    self.index = float(re.findall(r'<td>.+</td>',self.somethings)[3][4:-5])
        except: self.index = (re.findall(r'<td>.+</td>',self.somethings)[3][4:-5])
        
lister=list_negara()
test=text.split("<tr>")[3:]

for i in test:
    lister.add(negara(i))

del test

print(no_1, no_2, no_3, sep="\n")
lister.cetaknegara(sample=False) #hapus samplenya agar enak yang melihat
lister.cetakInno(sample=False)
print(lister.maketuple())

# pendekatan no 3 pada 1 dan 2 adalah memeriksa apakah itu adalah kalimat baru dengan cara pastikan dpan me dan di bukanlah huruf alfanumerik lain
# pendekatan no 4 saya potong semua <tr> nya lalu saya masukan pada for loop untuk membangun object agar lebih mudah dalam mengontrol data
# oleh karena itu saya membuat sesuatu list object sederhana 
# dan saya buat fungsi utuk menghandle properti objectnya
# banyak del disini karena untuk keperluan debugging (saya boros variable) 