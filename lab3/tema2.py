import numpy as np 
def ex1(n):
    v=[]
    if n==0: return v
    v.append(1)
    if n==1: return v
    v.append(1)
    if n==2: return v

    i=3# este al catele element este adaugat
    while(i<=n):
        v.append(v[i-1-1]+v[i-1-2])
        i+=1
    return v

#print(ex1(7))

def estePrim(nr):
    if nr==1: return False
    ok=True
    for d in range(2,int(np.sqrt(nr))+1):
        if nr%d==0:
            ok=False
            break
    return ok

def ex2(lista):
   v=[]
   for i in lista:
       if estePrim(i):
           v.append(i)
   return v
   
#print(ex2([1,2,3,4,5,6,7,8,9,10,11]))

def ex3(a,b):
    intersectie = list(set(a) & set(b))
    reuniune = list(set(a) | set(b))
    diferenta_a = list(set(a) - set(b))
    diferenta_b = list(set(b) - set(a))
    return intersectie, reuniune, diferenta_a, diferenta_b

#print(ex3([1, 2, 3, 4, 5],[3, 4, 5, 6, 7]))

def ex4(note,pozitie,start):
    curent=start
    v=[]
    v.append(note[curent])
    for i in pozitie:
        curent=(curent+i)%(len(note))
        v.append(note[curent])
    return v

#print(ex4(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))

def ex5(matrix):
    for i in range (len(matrix)):
        for j in range (len(matrix)):
            if i>j: matrix[i][j]=0
    return matrix

#print(ex5([
#    [2, 1, -1, 3],
#    [1, 2, 3, -1],
#    [3, 2, 2, 0],
#    [1, 1, 1, 1]
#]))

def ex6(nr,*liste):
    aparitie={}
    for i in liste:
       for j in i:
           if j in aparitie:
               aparitie[j]+=1
           else:
               aparitie[j]=1
        
    rezultat=[]

    for i in aparitie:
        if aparitie[i]==nr:
            rezultat.append(i)
    return rezultat

#print(ex6(2,[1,2,3],[2,3,4],["test"],[4,5,"test"]))


def palindrom(i):
    inv=0
    nr=i
    while nr:
        inv=inv*10+nr%10
        nr=nr//10
    if inv==i:
        return True
    return False

def ex7(lista):
    listaNrPalindrom=[]
    for i in lista:
        if palindrom(i):
            listaNrPalindrom.append(i)
    
    listaNrPalindrom=sorted(listaNrPalindrom)
    if len(listaNrPalindrom)==0: return (0)
    return (len(listaNrPalindrom),listaNrPalindrom[len(listaNrPalindrom)-1])

#print(ex7([12321,444,65,78,777]))

def ex8(x,lista,val=1,ind=True):
    rezultat=[]
    for i in lista:
        l=[]
        for ch in i:
            if ind:
                if ord(ch)%x==0:
                    l.append(ch)
            else:
                 if ord(ch)%x!=0:
                    l.append(ch)
        if l: rezultat.append(l)

    return rezultat

#print(ex8(2, ["test", "hello", "lab002"],ind=False))

def ex9(matrix):
    rezultat=[]
    for j in range(len(matrix[0])):
        max=matrix[0][j]
        for i in range(1,len(matrix)):
            if matrix[i][j]<=max:
                rezultat.append((i,j))
            else:
                max=matrix[i][j]
    return rezultat

#print(ex9([[1, 2, 3, 2, 1, 1],
#
#[2, 4, 4, 3, 7, 2],
#
#[5, 5, 2, 5, 6, 4],
#
#[6, 6, 7, 6, 7, 5]])) 

def ex10(*liste):
    rezultat=[]
    lenColMax = max(len(lista) for lista in liste)
    for j in range(lenColMax):
        t=tuple(lista[j] if len(lista)>j else None for lista in liste)
        rezultat.append(t)
    return rezultat
                
#print(ex10([1,2,3], [5,6,7], ["a", "b", "c"]))

def myFunc(e):
    return e[1][2]

def ex11(lista):
    return sorted( lista,key=myFunc)

#print(ex11([('abc', 'bcd'), ('abc', 'zza')]))

def ultimele2ch(e):
    return e[len(e)-2:]

def ex12(lista):
    rezultat=[]
    lista =sorted( lista,key=ultimele2ch)
    cuvPrecedent=lista[0]
    t=[]
    for i in range(len(lista)):
        if lista[i][len(lista[i])-2:]==cuvPrecedent[len(cuvPrecedent)-2:]:
            t.append(lista[i])
        else:
            cuvPrecedent=lista[i]
            rezultat.append(t)
            t=[]
            t.append(lista[i])
    rezultat.append(t)
    return rezultat
            

#print(ex12(['ana', 'banana', 'carte', 'arme', 'parte']))