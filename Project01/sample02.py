import datetime
import pandas as pd

tarihsaat = datetime.datetime.now().strftime("%d-%m-%Y %H:%M");
result = tarihsaat+".csv"

read1 = pd.read_csv("netflix1.csv")
read2 = pd.read_csv("netflix2.csv")

df1= pd.DataFrame(read1)
df2= pd.DataFrame(read2)

df1.to_csv(result)
