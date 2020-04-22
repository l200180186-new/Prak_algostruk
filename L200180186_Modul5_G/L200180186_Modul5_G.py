#!/usr/bin/env python
# coding: utf-8

# In[1]:


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
        return self.NIM
    def ambilUangSaku   (self):
        return self.uangSaku
    def ambilNama       (self):
        return self.nama
        
class MhsTIF(Mahasiswa):
    def katakanPy(self):
        print('Python is cool.')


# In[9]:


def cariPosisiYangTerkecil(A, From, To):
    position = From
    for i in range(From+1, To):
        if A[i] < A[position]:
            position = i
    return position
A = [18, 13, 44, 25, 66, 107, 78, 89]
cariPosisiYangTerkecil(A, 2, len(A))


# In[25]:


#test object
c0  = MhsTIF("Ika"    ,10 ,"Sukoharjo"  ,240000)
c1  = MhsTIF("Budi"   ,51 ,"Sragen"     ,235000)
c2  = MhsTIF("Ahmad"  ,2  ,"Surakarta"  ,250000)
c3  = MhsTIF("Chandra",18 ,"Surakarta"  ,235000)
c4  = MhsTIF("Eka"    ,4  ,"Boyolali"   ,240000)
c5  = MhsTIF("Fandi"  ,31 ,"Salatiga"   ,250000)
c6  = MhsTIF("Deni"   ,13 ,"Klaten"     ,245000)
c7  = MhsTIF("Galuh"  ,5  ,"Wonogiri"   ,245000)
c8  = MhsTIF("Janto"  ,23 ,"Klaten"     ,245000)
c9  = MhsTIF("Hasan"  ,64 ,"Karanganyar",270000)
c10 = MhsTIF("Khalid" ,29 ,"Porwodadi"  ,265000)

Daftar=[c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]


# In[26]:


def sortingMHS(listing):
    for i in range ( len ( listing ) - 1 ) :
        for i in range ( len ( listing ) - 1 ) :
            if listing[i].ambilNIM() > listing[i+1].ambilNIM() :
                listing[i],listing[i+1]=listing[i+1],listing[i]
    return listing

k=sortingMHS(Daftar)
print(*k, sep="\n")


# In[27]:


def gabungListUrut(a,b):
    la= len(a) 
    lb= len(b)
    c = []
    i = 0
    j = 0
    while i<la and j<lb:
        if a[i] < b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    if i<la:
        c+=a[i:]
    else:
        c+=b[j:]
    return c
    
A = [1,2,5,6,9]
B = [3,4,7,8]
#satukanListUrut(B,A)
gabungListUrut(B,A)


# In[28]:


def bubblesort(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
    return A
bubblesort([0,8,6,3,4,2,1,7,9])


# In[29]:


def insertionsort(A):
    for i in range(1,len(A)):
        nilai,pos=A[i],i
        while pos > 0 and nilai < A[pos -1]:
            A[pos] = A[pos - 1]
            pos    = pos -1
        A[pos] = nilai
    return A
insertionsort([0,8,6,3,4,2,1,7,9])


# In[30]:


def selectionsort(A):
    n= len(A)
    for i in range(n-1):
        posisiterkecil = i
        for j in range(posisiterkecil+1,n):
            if A[j] < A[posisiterkecil]:
                posisiterkecil = j
        if posisiterkecil != i:
            A[i],A[posisiterkecil]=A[posisiterkecil],A[i]
    return A
selectionsort([0,8,6,3,4,2,1,7,9])


# In[31]:


from time import time
from random import shuffle
k=list(range(1,6001))
shuffle(k)
k1=k[:]
k2=k[:]
k3=k[:]
print("================= Sorting {} data =====================".format(len(k)))
aw=time();bubblesort   (k1) ;ak=time()  ;print("Bubble sort    : ",(ak-aw),"s")
aw=time();insertionsort(k2) ;ak=time()  ;print("Insertion sort : ",(ak-aw),"s")
aw=time();selectionsort(k3) ;ak=time()  ;print("Selection sort : ",(ak-aw),"s")

