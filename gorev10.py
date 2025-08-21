dogum_yili = int(input("Doğum yılınızı giriniz: "))
guncel_yil = 2025

yas = guncel_yil - dogum_yili
print("Yaşınız:", yas)

if yas >= 0 and yas <= 12:
    print("Çocuksunuz")
elif yas >= 13 and yas <= 17:
    print("Ergensiniz")
else:
    print("Yetişkinsiniz")
