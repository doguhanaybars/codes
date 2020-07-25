import matplotlib.pyplot as plt

#Histogram
yaslar = [22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48]
yas_gruplari = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(yaslar,yas_gruplari,histtype="bar",rwidth=0.8)
plt.xlabel("yaş grupları")
plt.ylabel("Kişi Sayısı")
plt.title("Histogram Grafiği")
plt.show()
