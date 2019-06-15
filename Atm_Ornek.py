print(""""
**************************
Islemler:
1.Bakiye Ogren
2.Para Cek
3.Para Yatir
4.Cikis

**************************""")

bakiye=0

islem=input("Yapmak Istediginiz Islemi Secin:")

while True:
    if(islem=="1"):
        print("Bakiyeniz {} TLdir.".format(bakiye))
        islem = input("Yapmak Istediginiz Islemi Secin:")
    elif(islem=="2"):
        cekilecek_miktar=0
        cekilecek_miktar=int(input("Cekmek Istediginiz Miktari Girin:"))
        if(cekilecek_miktar>bakiye):
            print("Hesabinizda Yeterli Bakiye Bulunmamaktadir.Bakiyeniz : {}".format(bakiye))
            islem = input("Yapmak Istediginiz Islemi Secin:")
        else:
            bakiye=bakiye-cekilecek_miktar
            print("Kalan Bakiyeniz : {}".format(bakiye))
            islem = input("Yapmak Istediginiz Islemi Secin:")
    elif (islem == "3"):
        yatirilacak_miktar=input("Yatirmak Istediginiz Tutari Girin:")
        bakiye=bakiye+int(yatirilacak_miktar)
        print("Yeni Bakiyeniz : {}".format(bakiye))
        islem = input("Yapmak Istediginiz Islemi Secin:")
    elif (islem == "4"):
        print("Kartiniz Iade Ediliyor.. Tesekkurler..")
        break
    else:
        print("Lutfen Gecerli Bir Islem Secin!")
        islem = input("Yapmak Istediginiz Islemi Secin:")

