maasAli = 5000
maasAhmet = 4000
vergi = 0.27

print(maasAli - (maasAli*vergi))
print(maasAhmet - (maasAhmet*vergi))

# Değişken Tanımlama Kuralları
# rakam ile başlayamaz
number1 = 10
print(number1)
number1 = 20
print(number1)
number1 += 30
print(number1)

# Büyük küçük harf duyarlılığı vardır
age = 20
Age = 30

#Türkçe karakter kullanmayalım

yas = 20
_age = 20

x=1                 #int
y=2                 #float
name="Çınar"        #string
isSutudent = True   #bool

a=10
b=20
print(a+b) #30

a="10"
b="20"
print(a+b) #1020

firstName = "Sadık"
lastName = " Turan"
print(firstName + lastName) #Sadık Turan

x, y, name, isSutudent = (1, 2.3 , "Çınar", True)
print(x,y,name,isSutudent)

