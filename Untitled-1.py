print([x**2 for x in range (7)])
print([(x,x**2) for x in range (7)])
print([x**2 for x in range (15) if x%2==0])
print([[0 for i in range(3)] for j in range(3)])
print([[1 if i==j else 0 for i in range(3)] for j in range(3)])
d= "Yogyakarta dan Surakarta"
print([ i for i in d if i in "aiueoAIUEO"])
print([x for x in range(20,50)])# if apakahPrima(x)])
class Node(object):
    def __init__(self,data,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev
a=Node(11)
b=Node(52)
c=Node(18)
d=Node(30)
a.next=b
b.next=c

print(a.data)
print(a.next.data)
print(a.next.next.data)

def kunjungi(head):
    curNode=head
    while curNode is not None:
        print(curNode.data)
        curNode= curNode.next
def tambahkan(nodeBaru, NodeTambah):
    nodeBaru.next=NodeTambah
def sisipkan (nodeBaru, nodeTambah, posisi):
    curNode=nodeTambah
    n=[]
    while curNode is not None:
        n.append(curNode)
        curNode=curNode.next
    n[posisi-1].next=nodeBaru
    nodeBaru.next=n[posisi]
kunjungi(a)
sisipkan(d,a,1)
kunjungi(a)



def apakahKonsisten(matriks):
   lt=[len(matriks[x]) for x in range(len (matriks))]
   return True if sum(lt)/len(lt)==float(len(matriks[0])) else False

def ambilUkuran(m):
    if apakahKonsisten(m)==True: return (len(m),len(m[1]))
    else : return False

def jumlah(a,b):
    if ambilUkuran(a)==ambilUkuran(b):
        return [[ a[j][i]+b[j][i] for i in range(len(a))] for j in range (len(a[0]))]

def kali(a,b):
    if ambilUkuran(a)==ambilUkuran(b):
        return [[ a[j][i]*b[j][i] for i in range(len(a))] for j in range (len(a[0]))]

def det(a):
    if apakahKonsisten(a)==True::
        buffer=[0 for i in range (2*len(a)) ]
        for i in range(10):
            pass
print(jumlah([[1,2],[1,2]],[[1,2],[3,2]]))
print(kali([[1,2],[1,2]],[[1,2],[3,2]]))
