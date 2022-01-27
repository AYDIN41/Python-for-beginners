import numpy as np
import matplotlib.pyplot as plt

"""x = np.arange(51)
y = np.arange(0,101,2)
z = x ** 3
fig = plt.figure(figsize=(8,6))
axis = fig.add_axes([0.1,0.1,0.8,0.8])
axis.plot(x,z,color = "red")
axis.set_xlabel("X Values")
axis.set_ylabel("Y Values")
axis.set_title("X vs Y Values")
axis2 = fig.add_axes([0.2,0.5,0.4,0.3])
axis2.plot(x,y)
print(plt.show())"""
x = np.arange(51)
y = np.arange(0,101,2)
z = x ** 3
fig,axis = plt.subplots(nrows=1,ncols=2,figsize=(8,6))
axis[0].plot(x,y,color="red",lw=3,marker="o",markersize=2,markerfacecolor="black",markeredgecolor="red",markeredgewidth=5)
axis[0].set_xlabel("x")
axis[0].set_ylabel("Y")
axis[0].set_title("X and Y")
axis[1].plot(x,z,color="purple",lw=3,linestyle="-.",markerfacecolor="black",markeredgecolor="purple",markeredgewidth=3)
axis[1].set_xlabel("x")
axis[1].set_ylabel("Y")
axis[1].set_title("X and Y")
plt.tight_layout()

print(plt.show())