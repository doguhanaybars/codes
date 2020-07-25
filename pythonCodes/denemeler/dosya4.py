# with open("newfile.txt","r+",encoding=("utf-8")) as file:
#     file.seek(20)
#     file.write("deneme")

#*********SAYFA SONUNDA GÜNCELLEME*************
# with open("newfile.txt","r+",encoding=("utf-8")) as file:
#     print(file.read())
#***********SAYFA BAŞINDA GÜNCELLEME***********
# with open("newfile.txt","a",encoding=("utf-8")) as file:
#     file.write("\nEmel Turan")


# with open("newfile.txt","r+",encoding=("utf-8")) as file:
#      content = file.read()
#      content = "Efe Turan\n" + content
#      print(content)
#      file.seek(0)
#      file.write(content)



#***********SAYFA ORTASINA GÜNCELLEME*************

with open("newfile.txt","r+",encoding=("utf-8")) as file:
    list  = file.readlines()
    help(list.insert)
    list.insert(1,"Yılmaz Korkmaz\n")
    print(list)
    file.seek(0)
    # for i in list:
    #     file.write(i)
    file.writelines(list)

with open("newfile.txt","r",encoding=("utf-8")) as file:
    print(file.read())