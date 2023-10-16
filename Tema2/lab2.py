#set- elementele unice
#list []: l=[] l+=[7] l=[7,10]+[3,4] l=[7]*10 p=l[2:] p=l[:2]
#str1='abcde' str2=str1[::-1]
#touple () t1=(1,6,'a')    q=(x,y)   x,y=(10,20)  
#dictionary (map)  d1={'k1':16 'nume':'Alex' 'b':True}
# L= [n for n in range(100)]
#c= [" ".join(bin(n)[2:].rjust(8,'0')) for n in range(9)]
#l=[bin(n)[2:].rjust(8,'0') for n in range(9)]
#print(c)
#print(l)

import numpy as np

def ex0(n):
    return sum(range(1,n))
#print(ex0(10))

def ex1(a):
    return " ".join(hex(n)[2:] for n in a)

#print(ex1(n for n in range(ord('A'),ord('A')+26)))

def ex2(a):
    return " ".join(bin(n)[2:].rjust(8,'0') for n in a)
#print(ex2([0,1,2,3,4]))

def ex3(a,b):
    return format(float(a/b), ".100f")

#print(ex3(6,7))



def XkPlus1(xk,n,A):
    return xk-((pow(xk,n)-A)/(n*pow(xk,n-1)))

def ex5(ordin,numar):
    x1=XkPlus1(numar/2,ordin,numar)
    
    while(pow(x1,ordin)-0.01>numar):  
        x1=XkPlus1(x1,ordin,numar)
    print(format(float(x1), ".50f"))

#ex5(5,34)

def permN(n,cuv):
    p=len(cuv)
    n=n%p
    return "".join(cuv[(i+n)%p] for i in range (0, p))

def generareCuvP(n, p,alfabet, cuvCurent=""):
    if p == 0:
        print(permN(n,cuvCurent))
    else:
        for a in alfabet:
            generareCuvP(n,p-1,alfabet, cuvCurent + a)

def ex6(n, p,alfabet):
    if n < pow(len(alfabet),p):
       generareCuvP(n,p,alfabet)
   
#ex6(2,3,"abcdef")

def ex7(valori):
    matrix=[[0 for j in range(16)] for i in range(8)]
    nrL=0
    ok=False
    for v in valori:
        a=bin(v)[2:].rjust(16,'0')
        if ok and nrL%8==0:
            for i in range(8):
                for j in range(16):
                    print(matrix[i][j],end=" ")
                print()
            print()
            matrix=[[0 for j in range(16)] for i in range(8)]
            nrL=0
        for i in range(16):
            matrix[nrL][i]=int(a[i])
            
        nrL+=1
        ok=True

    
hex_values = [
    0x00, 0x00, 0xFC, 0x66, 0x66, 0x66, 0x7C, 0x60, 0x60, 0x60, 0x60, 0xF0, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0xC6, 0xC6, 0xC6, 0xC6, 0xC6, 0xC6, 0x7E, 0x06, 0x0C, 0xF8, 0x00,
   0x00, 0x00, 0x10, 0x30, 0x30, 0xFC, 0x30, 0x30, 0x30, 0x30, 0x36, 0x1C, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0xE0, 0x60, 0x60, 0x6C, 0x76, 0x66, 0x66, 0x66, 0x66, 0xE6, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x7C, 0xC6, 0xC6, 0xC6, 0xC6, 0xC6, 0x7C, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0xDC, 0x66, 0x66, 0x66, 0x66, 0x66, 0x66, 0x00, 0x00, 0x00, 0x00
]

#ex7(hex_values)

def ex4(coeficienti, termeni_liberi):
    numar_necunoscute = len(coeficienti)
    
    if numar_necunoscute > 4:
        print("Numarul de necunoscute depaseste 4.")
        return
    
    if len(termeni_liberi) != numar_necunoscute:
        print("Numarul de trrmeni liberi(ecuatii) trebuie sa fie egalo cu nr de necunoscute")
        return
    
    detA=np.linalg.det(coeficienti)

    if detA==0:
        print("Nu exista solutie")
    
    sol=[0 for i in range(numar_necunoscute)]
    for p in range(numar_necunoscute):
        x=[[termeni_liberi[i] if j==p else coeficienti[i][j] for j in range(numar_necunoscute)]for i in range(numar_necunoscute)]
        deltaX=np.linalg.det(x)
        solX=deltaX/detA
        sol[p]=solX
    return sol

coeficienti = [
    [2, 1, -1, 3],
    [1, 2, 3, -1],
    [3, 2, 2, 0],
    [1, 1, 1, 1]
]

termeni_liberi = [8, 3, 2, 1]

#print(ex4(coeficienti, termeni_liberi))


def ex8(x, y):
   
    if len(x) != len(y):
        raise ValueError("Lungimile secvențelor x și y trebuie să fie la fel.")
    n = len(x)
    suma_aproximare = 0

    for i in range(1, n):
    
        latime = x[i] - x[i - 1]
        arie_dreptunghi = latime * y[i]

        suma_aproximare += arie_dreptunghi

    return suma_aproximare

x = [0, 1, 2, 3, 4, 7]
y = [0, 1, 4, 9, 16, 10]

#print(ex8(x, y))





