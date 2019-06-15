

print("""
#######################
Sinav Sonuc Sistemi
#######################
""")
i=0
dersi_gecenler=list()
dersten_kalanlar=list()

while (i<4):
    isim=input("Isminizi Girin:")
    vize1=int(input("Vize Notunuz Giriniz:"))
    vize2=int(input("Vize2 Notunuz Giriniz:"))
    Final=int(input("Final Notunuz Giriniz:"))
   

    not_ortalama=(vize1*0.3)+(vize2*0.3)+(Final*0.4)
    if not_ortalama>=80:
        print("Tebrikler {}, Not Ortalamaniz {} , dersi A ile gectiniz!".format(isim,not_ortalama))
        dersi_gecenler.append(isim)
    elif not_ortalama>=60 and not_ortalama <80:
        print("Tebrikler {}, Not Ortalamaniz {} , dersi B ile gectiniz!".format(isim,not_ortalama))
        dersi_gecenler.append(isim)
    elif not_ortalama>50 and not_ortalama <60:
        print("Tebrikler {}, Not Ortalamaniz {} , dersi C ile gectiniz!".format(isim,not_ortalama))
        dersi_gecenler.append(isim)
    else:
        print("Dersi Gecemediniz!")
        dersten_kalanlar.append(isim)
    i+=1

print("Dersi Gecen Ogrenciler:",dersi_gecenler)
print("Dersi Gecemeyen Ogrenciler:",dersten_kalanlar)

liste=[]
i=0
while i<3:
    isim=input("isim girin:")
    liste.append(isim)
    i+=1
print(liste)















