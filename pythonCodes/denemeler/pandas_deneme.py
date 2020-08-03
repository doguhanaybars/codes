import pandas as pd 
import numpy as np 

data = np.array(["ali","fırat","kuas"])
s = pd.Series(data,index=[1,2,3])
print(s)