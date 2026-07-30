import numpy as np
array = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]],dtype=np.int64)
print(array)
print('array of type:',array.dtype)
print('number of dimensions:', array.ndim)
print('number of shape:', array.shape)
print('number of elements:', array.size)

a = np.zeros((3,3))
b = np.empty((3,3))
c = np.arange(10,20,2)
d = np.arange(6).reshape(2,3)
e = np.linspace(1,10,6).reshape(2,3)
print(a)
print(b)
print(c)
print(d)
print(e)
