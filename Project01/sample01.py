import datetime
today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1)
tarihsaat = datetime.datetime.now().strftime("%d-%m-%Y %H:%M");
print("Yesterday :" ,yesterday)
print("Today : ",today)
print("Tomorrow : ",tomorrow)

print(tarihsaat)