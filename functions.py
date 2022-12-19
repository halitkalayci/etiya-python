#fonksiyonlar
sayi1=1
sayi2=2


#def => definition
# parametre => fonksiyon çağırılırken verilmesi istenilen değerler
def topla(sayi1,sayi2):
    toplam=sayi1+sayi2
    #print(toplam)
    return toplam
# return => fonksiyonun geriye döneceği değeri ifade eder.
#def sayHi():
#    print("Hi")


#sayHi()

product1 = 10
product2 = 25
totalPrice = topla(product1,product2)
print(totalPrice)


def passedOrNot(note):
    if note < 50:
        print("Kaldınız")
        return False
    else:
        print("Geçtiniz")
        return True


if passedOrNot(60):
    print("Geçtiniz")
else:
    print("Kaldınız")