hak = 3
sifre = input("sifre: ")
hak = hak - 1

while sifre != "351247" and hak > 0:
    print("wrong, kalan hak:", hak)
    sifre = input("tekrar dene: ")
    hak = hak - 1

if sifre == "351247":
    print("giris basarili")
else:
    print("hakkin bitti")