import pandas as pd



csvData = pd.read_csv("netflix.csv")

# numberofcolumbs = len(csvData.columns)
# column_name=[]
# for i in range(0,numberofcolumbs):
#     print(csvData.columns[i])
    
#     column_name.append(csvData.columns[i])
    

# column_name
# # for x in range(numberofcolumbs):
# #     result = csvData[csvData.columns[x]].hist()

result = csvData.tipi.hist() 


result.figure.savefig('deneme.pdf')