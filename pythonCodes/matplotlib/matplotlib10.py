import matplotlib.pyplot as plt

#Pie Grafiği
goal_types = 'Penaltı','Kaleye Atılan Şut','Serbest Vuruş'
goals = [12,35,7]
colors = ['y','r','b']
plt.pie(goals,labels=goal_types,colors=colors, shadow=True,explode=(0.05,0.05,0.05), autopct="%1.1f%%")
plt.show()