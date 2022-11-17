#! kullanıcdan girdi almak
#! karar blokları
#! döngüler
print("2. gün başlangıç")

userInput = input()
print(f"Girilen değer: {userInput}")

#! type conversion
numberStr = "10";
print(type(numberStr))
number = int(numberStr)
print(number + 10)
print(type(number))





#indent
# n adet conditiona bağlı karar bloğu

userInput = input() #! kullanıcıdan input alma
lessonNote = float(userInput) #! ilgili inputu type conversion ile float'a çevirme
print(f"Ders notunuz: {lessonNote}") 

#! karar blokları ile işlem yapma
if lessonNote>50:
    print("Geçtiniz")
elif lessonNote == 50:
    print("Sınırda geçtiniz")
elif lessonNote == 49:
    print("Sınırda kaldınız")
else:
    print("Kaldınız")




