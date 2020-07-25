import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2,100)
fig,axs =  plt.subplots(3)
axs[0].plot(x, x, color="red")
axs[0].set_title("linear")
axs[1].plot(x, x**2, color="green")
axs[1].set_title("quadratic")
axs[2].plot(x, x**3, color="yellow")
axs[2].set_title("cubic")
plt.tight_layout()
plt.show()

