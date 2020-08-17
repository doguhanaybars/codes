var kullanicilar = [
    {email:"aybars@gmail.com",sifre:"12345"},
    {email:"firat@gmail.com",sifre:"12345"}
]

var tivitler = [
    {email:"aybars@gmail.com",tivit:"bugün hava çok güzel"},
    {email:"aybars@gmail.com",tivit:"bugün güzel"},
    {email:"firat@gmail.com",tivit:"bugün hava güzel"},
    {email:"firat@gmail.com",tivit:"bugün çok güzel"},

]

var email = prompt("email?")
var sifre = prompt("sifre?")

function giris(){
    if((email== kullanicilar[0].email && sifre == kullanicilar[0].sifre)||
    (email== kullanicilar[1].email && sifre == kullanicilar[1].sifre)){

        console.log(tivitler)

    }
    else{
        console.log('hatalı');
    }

}

giris(email,sifre)