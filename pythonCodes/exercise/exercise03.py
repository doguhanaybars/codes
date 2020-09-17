from pandas.io.excel import ExcelWriter
import pandas as pd

netflix = pd.read_csv('netflix1.csv')
csv_files = [netflix]

with ExcelWriter('my_excel.xlsx') as ew:
    for csv_file in csv_files:
        pd.read_csv(csv_file).to_excel(ew, sheet_name=csv_file)