import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("nba.csv")
df = df.drop(["Number"], axis = 1).groupby("Team").mean()
df.head().plot(subplots=True)
plt.legend()
plt.show()