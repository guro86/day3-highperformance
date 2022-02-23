import numpy as np



#%%1a
nullv = np.zeros(10)
nullv[-1] = 1

print(nullv)

#%%b

vec = np.arange(10,50)
print(vec)


#%%c
print(np.flip(vec))

#%%d

print(np.arange(9).reshape(3,3))

#%%e

v = np.array([1,2,0,0,4,0])
print(v[v>0])

#%%f
print(
      np.random.rand(30).mean()
      )

#%%g

a = np.ones((10,10))
a[1:-1,1:-1] = 0
print(a)

#%%h

a = np.kron(np.ones((4,4)),np.eye(2))
print(a)

#%%i

a = np.tile(np.eye(2),[4,4])
print(a)

#%%j

Z = np.arange(11)
Z[3:9] *= -1
print(Z)

#%%k

Z = np.random.random(10)
Z = np.sort(Z)
print(Z)

#%% l
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = A == B
print(equal)

#%% m
Z = np.arange(10, dtype=np.int32)
print(Z.dtype)
Z = Z.astype(np.float32)
print(Z.dtype)

#%%n
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D = np.diag(C)
print(D)