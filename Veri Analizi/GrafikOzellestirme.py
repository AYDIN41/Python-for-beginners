import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,6)
y = np.arange(2,11,2)
fig = plt.figure()
axes = fig.add_axes([0.3,0.3,0.6,0.6])
#linewidth ile grafik çizgisinin kalınlığı ayarlanıyor lw şeklinde de kullanılabilir
#grafiğin kesikli görünmesi için ise linestyle "--" methodunu kulllanıyoruz noktalı gitmwesi için ise : kullanıyoruz

#axes.plot(x,x**2,color = "green",lw = 7,linestyle=":")
#axes.plot(x,x**2,color = "green",lw = 7,linestyle="-.")
axes.plot(x,x**2,color = "green",lw = 3,linestyle="--",marker = "o",markersize=21,markerfacecolor="blue",markeredgecolor="yellow",markeredgewidth=5)
#grafiğin y ve x düzleminde uzunluğunu belirtmek için set_yveyaxlim() fonksiyonu kullanılıyor
axes.set_xlim(0,10)
axes.set_ylim(0,50)
print(plt.show())










