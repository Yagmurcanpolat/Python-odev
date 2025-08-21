urun1 = float(input("1. ürün fiyatını giriniz: "))
urun2 = float(input("2. ürün fiyatını giriniz: "))
urun3 = float(input("3. ürün fiyatını giriniz: "))

toplam = urun1 + urun2 + urun3

if toplam > 200:
    toplam = toplam - (toplam * 0.10)

print("Ödenecek toplam tutar:", toplam, "TL")
