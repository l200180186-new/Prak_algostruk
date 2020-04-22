#!/usr/bin/env python
# coding: utf-8

# # IMPORTED CLASS

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


# # OTHER SORT

# In[2]:


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
def insertionsort(A):
    for i in range(1,len(A)):
        nilai,pos=A[i],i
        while pos > 0 and nilai < A[pos -1]:
            A[pos] = A[pos - 1]
            pos    = pos -1
        A[pos] = nilai
    return A
def bubblesort(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
    return A


# # YANG DEPAN

# In[3]:


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


# In[4]:


def MergeSort(A):
    if len(A)>1:
        mid =len(A)//2
        a,b=A[:mid],A[mid:]
        MergeSort(a)
        MergeSort(b)
        la = len(a)     ; lb = len(b)
        k  = 0
        i  = 0          ; j = 0
        while i<la and j<lb:
            if a[i] < b[j]:
                A[k] = a[i]
                i+=1
            else:
                A[k] = b[j]
                j+=1
            k+=1
        if i < la :
            A[k:] = a[i:]
        elif j < lb :
            A[k:] = b[j:]
    return A
f=[0,8,6,3,4,2,1,7,9]
MergeSort(f)


# In[5]:


def Quicksort(A):
    Recursion(A,0,len(A)-1)
    return A
def Recursion(A,start,last):
    if start<last:
        pivotposition = partition(A,start,last)
        Recursion(A,start,pivotposition-1)
        Recursion(A,pivotposition+1,last)
def partition(A,start,Right_cursor):
    pivot=A[start]
    Left_cursor=start+1
    while True:
        while Left_cursor<=Right_cursor and A[Left_cursor]<=pivot:
            Left_cursor+=1
        while A[Right_cursor] >= pivot and Left_cursor <= Right_cursor:
            Right_cursor-=1
        if Left_cursor>Right_cursor:
            break
        else:
            A[Left_cursor],A[Right_cursor]=A[Right_cursor],A[Left_cursor]
    A[start],A[Right_cursor]=A[Right_cursor],A[start]
    return Right_cursor

Quicksort([5,7,8,6,3,4,2,1,0,9])


# # NUMBER 1 MERGESORT

# In[6]:


#make object
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


# In[7]:


def MergeSort_MhsTIF(A):
    if len(A)>1:
        mid =len(A)//2
        a,b=A[:mid],A[mid:]
        MergeSort_MhsTIF(a)
        MergeSort_MhsTIF(b)
        la = len(a)     ; lb = len(b)
        k  = 0
        i  = 0          ; j = 0
        while i<la and j<lb :
            if a[i].ambilNIM() < b[j].ambilNIM():
                A[k] = a[i]
                i+=1
            else:
                A[k] = b[j]
                j+=1
            k+=1
        if i < la :
            A[k:] = a[i:]
        elif j < lb :
            A[k:] = b[j:]
    return A

Daftar=[c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]
print(*MergeSort_MhsTIF(Daftar),sep="\n")


# # NUMBER 1 QUICKSORT

# In[8]:


def Quicksort_MHS(A):
    Recursion_MHS(A,0,len(A)-1)
    return A
def Recursion_MHS(A,start,last):
    if start<last:
        pivotposition = partition_MHS(A,start,last)
        Recursion_MHS(A,start,pivotposition-1)
        Recursion_MHS(A,pivotposition+1,last)
def partition_MHS(A,start,Right_cursor):
    pivot=A[start]
    Left_cursor=start+1
    while True:
        while Left_cursor<=Right_cursor and A[Left_cursor].ambilNIM()<=pivot.ambilNIM():
            Left_cursor+=1
        while A[Right_cursor].ambilNIM() >= pivot.ambilNIM() and Left_cursor <= Right_cursor:
            Right_cursor-=1
        if Left_cursor>Right_cursor:
            break
        else:
            A[Left_cursor],A[Right_cursor]=A[Right_cursor],A[Left_cursor]
    A[start],A[Right_cursor]=A[Right_cursor],A[start]
    return Right_cursor
print(*Quicksort_MHS(Daftar),sep="\n")


# # NOMER 3

# In[9]:


from time import time
from random import shuffle
k=list(range(1,100001))
shuffle(k)
k1=k[:]
k2=k[:]
k3=k[:]
k4=k[:]
k5=k[:]
k6=k[:]
k7=k[:]
print("================= Sorting {} data =====================".format(len(k)))
#aw=time();bubblesort   (k1) ;ak=time()  ;print("Bubble sort    : ",(ak-aw)/1,"s")
#aw=time();insertionsort(k2) ;ak=time()  ;print("Insertion sort : ",(ak-aw)/1,"s")
#aw=time();selectionsort(k3) ;ak=time()  ;print("Selection sort : ",(ak-aw)/1,"s")
aw=time();MergeSort    (k4) ;ak=time()  ;print("Merge sort     : ",(ak-aw)/1,"s")
aw=time();Quicksort    (k5) ;ak=time()  ;print("Quick sort     : ",(ak-aw)/1,"s")
aw=time();sorted(k6)       ;ak=time()   ;print("Tunsort        : ",(ak-aw)/1,"s") 


# # NOMER 4 TRACE MERGESORT

# In[10]:


def MergeSort_Trace(A):
    print("Memecah \t\t:",A)
    if len(A)>1:
        mid =len(A)//2
        a,b=A[:mid],A[mid:]
        MergeSort(a)
        MergeSort(b)
        la = len(a)     ; lb = len(b)
        k  = 0
        i  = 0          ; j = 0
        print("Menggabungkan \t\t:", a,",",b)
        while i<la and j<lb:
            if a[i] < b[j]:
                A[k] = a[i]
                i+=1
            else:
                A[k] = b[j]
                j+=1
            k+=1
        if i < la :
            A[k:] = a[i:]
        elif j < lb :
            A[k:] = b[j:]
        print("Hasil Mengabungkan \t:",A)
    return A
f=[80, 7, 24, 16, 43, 91, 35, 2, 19, 72]
MergeSort(f)


# # NOMER 4 QUICKSORT TRACE

# In[11]:


def Quicksort_Trace(A):
    Recursion_Trace(A,0,len(A)-1)
    print("Data telah urut")
    return A
def Recursion_Trace(A,start,last):
    if start<last:
        pivotposition = partition_Trace(A,start,last)
        Recursion_Trace(A,start,pivotposition-1)
        Recursion_Trace(A,pivotposition+1,last)
def partition_Trace(A,start,Right_cursor):
    pivot=A[start]
    print("Atur posisi untuk pivot",A[start])
    print("Array saat ini",A)
    Left_cursor=start+1
    while True:
        while Left_cursor<=Right_cursor and A[Left_cursor]<=pivot:
            print("Comparison",A[Left_cursor],"dengan",pivot)
            Left_cursor+=1
        print(A[Left_cursor],"lebih besar dari pivot, mencari penukar")
        while A[Right_cursor] >= pivot and Left_cursor <= Right_cursor:
            print("Comparison",A[Right_cursor],"dengan",pivot)
            Right_cursor-=1
        if Left_cursor>Right_cursor:
            break
        else:
            print("Tukar",A[Left_cursor],"dengan",A[Left_cursor])
            A[Left_cursor],A[Right_cursor]=A[Right_cursor],A[Left_cursor]
    print("Tukar",A[Left_cursor],"dengan",A[Right_cursor])
    A[start],A[Right_cursor]=A[Right_cursor],A[start]
    return Right_cursor
f=[80, 7, 24, 16, 43, 91, 35, 2, 19, 72]
Quicksort(f)


# # NOMER 5 IMPROVING MERGESORT

# In[12]:


# mas pass aku mumet dalan metune


# In[ ]:





# # NOMER 6 QUICKSORT WITH 3 MEDIAN PIVOT

# In[13]:


from statistics import median
def Quicksort2(A):
    Recursion2(A,0,len(A)-1)
    return A
def Recursion2(A,start,last):
    if start<last:
        pivotposition = partition2(A,start,last)
        Recursion2(A,start,pivotposition-1)
        Recursion2(A,pivotposition+1,last)
def partition2(A,start,Right_cursor):
    pivot=median([A[start],A[Right_cursor],A[(start+Right_cursor)//2]])
    Left_cursor=start
    while True:
        while Left_cursor<=Right_cursor and A[Left_cursor]<=pivot:
            Left_cursor+=1
        while A[Right_cursor] >= pivot and Left_cursor <= Right_cursor:
            Right_cursor-=1
        if Left_cursor>Right_cursor:
            break
        else:
            A[Left_cursor],A[Right_cursor]=A[Right_cursor],A[Left_cursor]
    A[start],A[Right_cursor]=A[Right_cursor],A[start]
    return Right_cursor


# In[14]:


aw=time();Quicksort2(k7)       ;ak=time()       ;print("Quicksort2        : ",(ak-aw)/1,"s") 
aw=time();Quicksort (k )       ;ak=time()       ;print("Quick sort        : ",(ak-aw)/1,"s")


# # Mergesort on linked list

# In[15]:


class node:
    def __init__(self, data,Next=None):
        self.data=data
        self.next=Next
    def __str__(self):
        print(self.data)
class link:
    def __init__(self, head):
        self.head=head
    def append(self, node):
        pointer=self.head
        while pointer.next is not None:
            pointer=pointer.next
        pointer.next=node
    def Middlelist(self, head): 
        if (head == None): 
            return head 
        pointer_1 = head 
        pointer_2 = head 
        while (pointer_2.next is not None and pointer_2.next.next is not None): 
            pointer_1 = pointer_1.next
            pointer_2 = pointer_2.next.next
        return pointer_1 
    def rec_mergesort(self, a, b): 
        result = None
        if a == None: 
            return b 
        if b == None: 
            return a 
        if a.data <= b.data: 
            result = a 
            result.next = self.rec_mergesort(a.next, b) 
        else: 
            result = b 
            result.next = self.rec_mergesort(a, b.next) 
        return result 
    def mergesort_linked_list (self):
        self.head = self.mergeSort(self.head)

    def mergeSort(self, h): 
        if h == None or h.next == None: 
            return h 
        middle = self.Middlelist(h) 
        nexttomiddle = middle.next
        middle.next = None
        left = self.mergeSort(h)
        right = self.mergeSort(nexttomiddle) 
        return  self.rec_mergesort(left, right)

    def printer(self):
        pointer=self.head
        buffer=list()
        while pointer is not None:
            buffer.append(pointer.data)
            pointer=pointer.next
        print(*buffer,sep=" ")

li = link(node( 0)) 
li.append(node( 7)) 
li.append(node( 1)) 
li.append(node( 5)) 
li.append(node( 4)) 
li.append(node( 3)) 
li.append(node( 2))  
li.mergesort_linked_list()
li.printer()

