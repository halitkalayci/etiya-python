# runtime exception vs compile-time exception
# exception
# handled exception
try:
    examNote = float(input("Lütfen sınav notunuzu giriniz: "))
    print(examNote)
except ValueError:
    print("Deneme 123")
except:
    print("Doğru bir girdi girmediniz..")
finally:
    print("Try except bloğu sona erdi..")

print("Bitti..")
