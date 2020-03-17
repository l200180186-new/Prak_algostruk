def apakahKonsisten(matrix):
    hold = len(matrix[0])
    try:
        for i in range(len(matrix)):
            if hold != len(matrix[i]):
                return False
        return True
    except:
        return "Bukan Matriks tapi 1D array"
def Ukuran(matrix):
    if apakahKonsisten(matrix) == True: return (len(matrix),len(matrix[0]))
    else: return apakahKonsisten(matrix)
    def jumlah(A_matrix,B_matrix):
    if Ukuran(A_matrix)==Ukuran(B_matrix):
        for i in range(len(A_matrix)):
            for j in range(len(A_matrix)):
                A_matrix[i][j]+=B_matrix[i][j]
        return A_matrix
    return """Matrix tidak sesuai ukurannya atau ada yang tidak konsisten,\ninfo lebih lanjut gunakan : Ukuran(matriks) atau apakahKonsisten(matriks)"""
def kali(A_matrix,B_matrix):
    if Ukuran(A_matrix)==Ukuran(B_matrix):
        for i in range(len(A_matrix)):
            for j in range(len(A_matrix)):
                A_matrix[i][j]*=B_matrix[i][j]
        return A_matrix
    return """Matrix tidak sesuai ukurannya atau ada yang tidak konsisten,\ninfo lebih lanjut gunakan : Ukuran(matriks) atau apakahKonsisten(matriks)"""
def det(matrix):
    if Ukuran(matrix)[0]==Ukuran(matrix)[1]:
        if Ukuran(matrix)[0]==2:
            return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
        p_temp=len(matrix)
        a_temp=[1 for i in range (len(matrix)*2)]
        for i in range (len(matrix)):
            matrix[i] = matrix[i]+matrix[i][:-1]
            x         = list(reversed(matrix[i]))
            for j in range(p_temp):
                a_temp[j]       = matrix[i][i+j]  *a_temp[j]
                a_temp[j+p_temp]= -1*  x   [i+j]  *a_temp[j+p_temp]
        return sum(a_temp)
def buatNol( m , n=None):
    if n is None: n=m
    return [[0 for i in range (n)]for j in range(m)]
def buatIdentitas(m): 
    return [[1 if i==j else 0 for i in range(m)] for j in range(m)]
class Normal_node(object):
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class LList(object):
    def __init__(self,head):
        self.head=head
    def cari(self,yang_dicari):
        pointer=self.head
        counter=0
        while pointer is not None:
            if pointer.data==yang_dicari:
                print("data dengan isi {} ditemukan pada list number {}".format(yang_dicari, counter))
                break
            pointer=pointer.next
            counter+=1
        if pointer==None:
            print("data tidak ditemukan")
    def access(self):
        pointer=self.head
        while pointer is not None:
            print(pointer.data,end=" ")
            pointer=pointer.next
        print("")
    def insert(self,node,position):
        pointer= self.head
        previous= None
        try:
            for i in range(position):
                previous=pointer
                pointer=pointer.next
        except:
            print("Posisi melebihi panjang list")
        if previous is not None:   previous.next=node
        if position==0:            self.head=node
        node.next=pointer
    def tambahDepan(self,node):
        node.next,self.head=self.head,node
    def tambahAkhir(self,node):
        cursor=self.head
        previous=None
        while cursor is not None:
            previous=cursor
            cursor=cursor.next
        previous.next=node
    def hapus(self,position):
        pointer= self.head
        llist=[]
        while pointer is not None:
            llist.append(pointer)
            pointer=pointer.next
        if len(llist)<=position or position<0: print("Posisi salah")
        llist[position].next=None
        llist[position-1].next=llist[position+1]
class Advanced_Node(object):
    def __init__(self, data, next=None, previous=None):
        self.data    = data
        self.next    = next
        self.previous= previous
class DoubleLink(object):
    def __init__(self, head):
        self.head    = head
        self.tail    = head
    def tambahDepan(self,node):
        self.head.previous = node
        node.next = self.head
        self.head = node
    def tambahAkhir(self,node):
        prev,cursor = None,self.head
        while cursor is not None:
            prev,cursor = cursor,cursor.next
        prev.next,  node.previous  =  node, prev
        self.tail  =  node 
    def kunjungiDepan(self):
        cursor,buffer  =  self.head,[]
        while cursor is not None:
            buffer.append(cursor.data)
            cursor = cursor.next
        print(*buffer, sep=" ")
    def kunjungiBelakang(self):
        cursor,buffer  =  self.tail,[]
        while cursor is not None:
            buffer.append(cursor.data)
            cursor = cursor.previous
        print(*buffer, sep=" ")
