import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,6)
print(x)
y = np.arange(2,11,2)
print(y)
#print(plt.plot(x,y,"blue"))
#print(plt.show())
"""
print(plt.subplot(2,2,1))
print(plt.plot(x,y,"blue"))
print(plt.subplot(2,2,2))
print(plt.plot(x,y**2,"red"))
print(plt.subplot(2,2,3))
print(plt.plot(x**2,y,"pink"))
print(plt.subplot(2,2,4))
print(plt.plot(x**2,y//2,"purple"))
fig = plt.figure()
axis1 = fig.add_axes([0.1,0.1,0.8,0.8])

axis2 = fig.add_axes([0.2,0.6,0.3,0.2])
print(axis1.plot(y,x))
print(axis1.set_xlabel("Outer X"))
print(axis1.set_ylabel("Outer Y"))
print(axis1.set_title("Outer Graph"))
print(axis2.plot(x,y))
print(axis2.set_xlabel("Inner X"))
print(axis2.set_ylabel("Inner Y"))
print(axis2.set_title("Inner Graph"))"""
#fig,axes = plt.subplots(nrows=2,ncols=1)
"""for ax in axes:
    ax.plot(x,y)"""
"""axes[0].plot(x,y)
axes[0].set_title("First One")
axes[1].plot(x,x ** 5)
axes[1].set_title("Second One")
plt.tight_layout()"""
"""fig = plt.figure(figsize=(12,8))
axes = fig.add_axes([0,0,1,1])
axes.plot(x,y,color="blue")"""
fig,axes = plt.subplots(nrows=2,ncols=1,figsize = (8,6))
axes[0].plot(x,y,color="red")
axes[0].set_title("First One")
axes[1].plot(y,x,color="purple")
axes[1].set_title("Second Title")
plt.tight_layout()
#istenildiği gibi şekilde grafik kaydetmek için
#fig.savefig("Figure1.pdf")

fig = plt.figure(figsize=(6,4))
axes = fig.add_axes([0.252,0.3,0.5,0.5])
axes.plot(x,x**0.5,color="red",label="X Karekök")
axes.plot(x,x**2,color="black",label = "X Kare")
axes.plot(x,x**3,color="#7fe5f0",label = "X Küp")
axes.legend()
print(plt.show())




