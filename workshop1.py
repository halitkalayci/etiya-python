
#! 1. kullanıcı gireceği ders sayısını belirtecek
lessonCount = int(input("Kaç adet ders notu gireceksiniz?"))

#! 2. girilen ders sayısı kadar 2 adet soru sorulacak.
#! (1. ders için vize notu giriniz. 1. ders için final notu giriniz)
#! girilen notlar ondalıklı olabilir

passedExams = 0
failedExams = 0
for i in range(lessonCount):
    lessonExam1 = float(input(f"{i+1}. ders için vize notunuzu giriniz."))
    lessonExam2 = float(input(f"{i+1}. ders için final notunu giriniz."))
    totalExamNote = (lessonExam1 * 0.4) + (lessonExam2 * 0.6)
    if totalExamNote >= 50:
        passedExams += 1
    else:
        failedExams += 1
print(f"{passedExams} adet dersten geçtiniz. {failedExams} adet dersten kaldınız.")