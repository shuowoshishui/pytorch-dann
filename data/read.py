import torch
import torchvision
import matplotlib.pyplot as plt
from skimage import io
mnist_test= torchvision.datasets.MNIST(
    '/home/chenshuo/dann/data/MNIST/', train=False, download=False
)
print('test set:', len(mnist_test))

f=open('mnist_m_test.txt','w')
for i,(img,label) in enumerate(mnist_test):
    img_path="./mnist_m_test/"+str(i)+".jpg"
    io.imsave(img_path,img)
    f.write(img_path+' '+str(label)+'\n')
f.close()
