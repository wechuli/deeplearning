#%%
import numpy as np

# Scalars(0D tensors)
# A tensor that contains one number is calles a scalar
x = np.array(12)
print(x)
print(type(x))

#%%
# Vectors(1D) tensors
# an array of numbers is called a vector, or 1D tensor. A 1D tensor is said to have excalty one axis
x = np.array([12,3,6,14])
print(x)

#%%
# Matrices(2D tensors)

x= np.array([[5,78,2,34,0],[5,7,2,304,0],[0,78,1,34,0]])
print(x)
# %%
# 3D tensors and higher-dimensional tensors
x = np.array([x,x,x])
print(x.shape)

#%%
from keras.datasets import mnist
(train_images,train_labels),(test_images,test_labels) = mnist.load_data()
# %%
import matplotlib.pyplot as plt
digit = train_images[4]
plt.imshow(digit,cmap=plt.cm.binary)
plt.show()