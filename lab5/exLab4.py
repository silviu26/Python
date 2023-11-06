#ex 1
class Stack:
    def __init__(self):
        self.vector=[]
    
    def push(self,item):
        self.vector.append(item)
    
    def pop(self):
        if self.vector==None:
            return None
        self.vector=self.vector[:len(self.vector)-1]
        return self.vector
    
    def peek(self):
        if self.vector==None:
            return None
        return self.vector[len(self.vector)-1]
    

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack:", stack.vector)
print("Pop:", stack.pop())
print("Peek:", stack.peek())

#ex 2
class Queue:
    def __init__(self):
        self.vector=[]
    
    def push(self,item):
        self.vector.append(item)
    
    def pop(self):
        if self.vector==None:
            return None
        self.vector=self.vector[1:len(self.vector)]
        return self.vector
    
    def peek(self):
        if self.vector==None:
            return None
        return self.vector[0]
    
q = Queue()
q.push(1)
q.push(2)
q.push(3)

print("Queue:", q.vector)
print("Pop:", q.pop())
print("Peek:", q.peek())

#ex 3
class Matrix:
    def __init__(self,n,m):
        self.n=n
        self.m=m
        self.matrix=[[0 for j in range(m)] for i in range(n)]

    def get(self,i,j):
        if 0<=i <self.n and 0<= j <self.m:
            return self.matrix[i][j]
        else:
            print("index invalid")
    
    def set(self,i,j,value):
        if 0<=i <self.n and 0<= j <self.m:
            self.matrix[i][j]=value
        else:
            print("index invalid")

    def transpusa(self):
        tran = Matrix(self.m, self.n)
        for i in range(self.n):
            for j in range(self.m):
                tran.set(j, i, self.get(i, j))
        return tran
    
    def multiply(self, other):
        if self.m != other.n:
            raise ValueError("dimensiuni incompatibele")
        r = Matrix(self.n, other.m)
        for i in range(self.n):
            for j in range(other.m):
                value = 0
                for k in range(self.m):
                    value += self.get(i, k) * other.get(k, j)
                r.set(i, j, value)
        return r
    
    def transform(self,func):
        for i in range(self.n):
            for j in range(self.m):
                self.set(i, j, func(self.get(i, j)))


matrix = Matrix(2, 3)
matrix.set(0, 0, 1)
matrix.set(0, 1, 2)
matrix.set(0, 2, 3)
matrix.set(1, 0, 4)
matrix.set(1, 1, 5)
matrix.set(1, 2, 6)

print()
print("Matrix:")
for i in range(matrix.n):
    for j in range(matrix.m):
        print(matrix.get(i,j), end=" ")
    print()
print()

trans = matrix.transpusa()
print("Transpusa:")
for i in range(trans.n):
    for j in range(trans.m):
        print(trans.get(i,j), end=" ")
    print()
print()

matrix1 = Matrix(3, 3) #matricea identitate
matrix1.set(0, 0, 1)
matrix1.set(1, 1, 1)
matrix1.set(2, 2, 1)

product_matrix = matrix.multiply(matrix1)
print("matrix * matrix1:")
for i in range(product_matrix.n):
    for j in range(product_matrix.m):
        print(product_matrix.get(i,j), end=" ")
    print()
print()

matrix.transform(lambda x: x * 2)
print("matrix cu functie:")
for i in range(matrix.n):
    for j in range(matrix.m):
        print(matrix.get(i,j), end=" ")
    print()
print()