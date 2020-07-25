name = "Fırat"


def sayHello(name="user"):  # buradaki name teknik olarak yukarıdaki name ile alakalı değil... fonksiyon çağırılırken yazılan name in yukarıdaki name ile alakası var
    return "Hello " + name


msg = sayHello(name)
print(msg)
