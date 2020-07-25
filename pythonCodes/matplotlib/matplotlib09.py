import matplotlib.pyplot as plt

# Stack Plot
yil = [2011,2012,2013,2014,2015]
oyuncu1 = [8,10,12,7,9]
oyuncu2 = [7,12,5,15,21]
oyuncu3 = [18,20,22,25,19]
plt.plot([],[],color="y",label="oyuncu1")
plt.plot([],[],color="r",label="oyuncu2")
plt.plot([],[],color="b",label="oyuncu3")
plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3, colors=["y","r","b"])
plt.title("Yıllara göre atılan goller")
plt.xlabel("yil")
plt.ylabel("Gol Sayısı")
plt.legend()
plt.show()