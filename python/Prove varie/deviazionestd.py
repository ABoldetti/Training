import numpy as np
a=[2.007,2.0043,1.995,1.9967,2.00221,2.0176,2.0101,2.0083,2.0043,1.9976,1.9835,2.0256,2.0143,2.0116,2.0041,2.0058,2.0039,1.9882,2.0311,2.0162,2.0119]
b=[]
avg=np.mean(a)
for i in range (len(a)):
    b[i]=a[i]-avg
    b[i]=b[i]**2

sum=np.sum(b)
devstd=sum/len(a)
print(devstd)

