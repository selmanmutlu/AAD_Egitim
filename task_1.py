##Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini format metoduyla yapmaya çalışın
a = int(input("ilk sayıyı giriniz:"))
b = int(input("ikinci sayıyı giriniz:"))
c = int(input("üçüncü sayıyı giriniz:"))

print("ÇÖZÜM: {} x {} x {} = {}".format(a,b,c,a*b*c))

#1) Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.
ad = input("İsminizi Giriniz:")
soyad = input("Soyisminizi Giriniz:")
numara = input("Numaranızı Giriniz:")
print("\n----KULLANICI BİLGİLERİ---- \n İsim: {} \n Soyisim: {} \n Numara: {} ".format(ad,soyad,numara))

#2) Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın. Hipotenüs Formülü: a^2 + b^2 = c^2
kenar1 = int(input("Birinci dik kenar değerini giriniz:"))
kenar2 = int(input("İkinci dik kenar değerini giriniz:"))
print("Hipotenüs'ün uzunluğu: {} ".format((kenar1**2+kenar2**2)**0.5))


"""
3) Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.
#Beden Kitle İndeksi: Kilo / Boy(m) * Boy(m)

#BKİ 18.5'un altındaysa -------> Zayıf

#BKİ 18.5 ile 25 arasındaysa ------> Normal

#BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

#BKİ 30'un üstündeyse -------------> Obez"""
boy = float(input("Boyunuzu giriniz:"))
kilo = float(input("Kilonuzu giriniz:"))
kitle_endeksi = kilo/(boy*boy)

if kitle_endeksi > 30:
    print("Obez")
elif kitle_endeksi < 30 and kitle_endeksi > 25:
    print("Fazla Kilolu")
elif kitle_endeksi > 18.5 and kitle_endeksi < 25:
    print("Normal")
elif kitle_endeksi < 18.5:
    print("Zayıf")


"""
4) Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.
Vize1 toplam notun %30'una etki edecek.

Vize2 toplam notun %30'una etki edecek.

Final toplam notun %40'ına etki edecek.


Toplam Not >=  90 -----> AA

Toplam Not >=  85 -----> BA

Toplam Not >=  80 -----> BB

Toplam Not >=  75 -----> CB

Toplam Not >=  70 -----> CC

Toplam Not >=  65 -----> DC

Toplam Not >=  60 -----> DD

Toplam Not >=  55 -----> FD

Toplam Not <  55 -----> FF


"""
print("""
********************************************

HARF NOTU UYGULAMASI

********************************************
""")
vize1 = int(input("1. Vize Notunu Giriniz:"))
vize2 = int(input("2. Vize Notunu Giriniz:"))
final = int(input("Final Notunu Giriniz:"))
harf_notu = vize1*(3/10) + vize2*(3/10) + final*(4/10)

if harf_notu >= 90:
    print("AA")
elif harf_notu >= 85:
    print("BA")
elif harf_notu >= 80:
    print("BB")
elif harf_notu >= 75:
    print("CB")
elif harf_notu >= 70:
    print("CC")
elif harf_notu >= 65:
    print("DC")
elif harf_notu >= 60:
    print("DD")
elif harf_notu >= 55:
    print("FD")
else:
    print("FF")


"""
5)
1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.
İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin.
"""
for i in range(1,10):
    for j in  range(1,10):
        print("{} x {} = {}".format(i,j,i*j))




"""
6)
Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin. Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.
İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın.

"""
toplam = 0

while True:
    sayı = input("Sayıyı Giriniz:")

    if sayı == "q":
        break
    sayı = int(sayı)

    toplam += sayı
print("Toplam:",toplam)

"""
7) 
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.
Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
"""
sayı = int(input("sayı:"))

list = []
x = 1
toplam = 0

while x < sayı:
    if sayı % x == 0:
        list.append(x)
    x += 1

for i in list:
    toplam += i
if toplam == sayı:
    print("girdiğiniz sayı bir mükemmel sayıdır")
else:
    print("girdiğiniz sayı bir mükemmel sayı değildir")

"""
8) 
Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.

"""
def ebobbulma(sayı1,sayı2):
    i = 1
    list = []
    while i <= sayı1 and i <= sayı2:
        if sayı1 % i == 0 and sayı2 % i == 0:
            list.append(i)
        i += 1

    return max(list)

sayı1 = int(input("İlk Sayınızı Giriniz:"))
sayı2 = int(input("ikinci Sayınızı Giriniz:"))

print("EBOB:",ebobbulma(sayı1,sayı2))


"""
9)
Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.

"""
def ekokbulma(sayı1,sayı2):
    i = 1
    ekok = 1
    while True:
        if sayı1*i % sayı2 == 0:
            ekok = sayı1*i
            return ekok
        i += 1

a = int(input("İLK SAYIYI GİRİNİZ:"))
b = int(input("İKİNCİ SAYIYI GİRİNİZ:"))
print("EKOK:",ekokbulma(a,b))

"""
10)

Bu projede ise 4 tane sınıfı oluşturun.
Hayvan Sınıfı ------> Bütün hayvanların ortak özelliklerinin toplandığı sınıf olacak.

Köpek Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa köpeklere ait ek özellikler ve metodlar ekleyin.

Kuş Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa kuşlara ait ek özellikler ve metodlar ekleyin.

At Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa atlara ait ek özellikler ve metodlar ekleyin.

"""
import  time

class Hayvanlar():
    def __init__(self,grup="Omurgalılar ve Omurgasızlar",yaşam_alanı="Hava,Kara,Deniz",beslenme_çeşidi="etçil,otçul,hem etçil hem otçul"):
        self.grup = grup
        self.yaşam_alanı = yaşam_alanı
        self.beslenme_çeşidi = beslenme_çeşidi
    def __str__(self):
        return ("Hayvanların Ortak Özellikleri \n1)Grup = {}\n2)Yaşam Alanı = {}\n3)Beslenme Çeşidi = {}".format(self.grup,self.yaşam_alanı,self.beslenme_çeşidi))

class Köpekler(Hayvanlar):
    def __init__(self,grup="Memeliler",yaşam_alanı="Kara",beslenme_çeşidi="Etçil",cins=["Buldog","Golden","Pitbull","Rottweiler"],genel_özellikleri=["Keskin koku alma ve işitme kabiliyetleri vardır.","Ömürleri 15-20 yıl arasıdır.","Sahiplerine bağlıdırlar."]):
        super().__init__(grup,yaşam_alanı,beslenme_çeşidi)
        self.cins = cins
        self.genel_özellikleri = genel_özellikleri
    def __str__(self):
        return ("KÖPEKLERİN GENEL ÖZELLİKLERİ \n1)Tür = {}\n2)Yaşam Alanı = {}\n3)Beslenme Çeşidi = {}\n4)Cinsleri = {}\n5)Genel Özellikleri = {}".format(self.grup,self.yaşam_alanı,self.beslenme_çeşidi,self.cins,self.genel_özellikleri))
    def cins_ekle(self,):
        a = input("Eklemek istediğiniz cinsi giriniz:")
        print("Ekleniyor...")
        time.sleep(2)
        self.cins.append(a)
    def özellik_ekleme(self):
        b = input("Eklemek istediğiniz özelliği giriniz:")
        print("Ekleniyor...")
        time.sleep(2)
        self.genel_özellikleri.append(b)

class Kuşlar(Hayvanlar):
    def __init__(self,grup="Kuşlar",yaşam_alanı="Hava ve Kara",beslenme_çeşidi="Etçil",cins=["Amazon Papağanı","Muhabbet Kuşu","Hint Bülbülü"],genel_özellikleri=["Vücutları tüylerle kaplıdır.","Yavrularını sütle beslemezler."]):
        super().__init__(grup,yaşam_alanı,beslenme_çeşidi)
        self.cins = cins
        self.genel_özellikleri = genel_özellikleri
    def __str__(self):
        return ("KUŞLARIN GENEL ÖZELLİKLERİ \n1)Tür = {}\n2)Yaşam Alanı = {}\n3)Beslenme Çeşidi = {}\n4)Cinsleri = {}\n5)Genel Özellikleri = {}".format(self.grup,self.yaşam_alanı,self.beslenme_çeşidi,self.cins,self.genel_özellikleri))
    def cins_ekle(self,):
        a = input("Eklemek istediğiniz cinsi giriniz:")
        print("Ekleniyor...")
        time.sleep(2)
        self.cins.append(a)
    def özellik_ekleme(self):
        b = input("Eklemek istediğiniz özelliği giriniz:")
        print("Ekleniyor...")
        time.sleep(2)
        self.genel_özellikleri.append(b)

class Atlar(Hayvanlar):
    def __init__(self,grup="Memeliler",yaşam_alanı="Kara",beslenme_çeşidi="Otçul",cins=["Arap Atı","Türkmen Atı"],genel_özellikleri=["Kulakları çok iyi işitir.","Bacak kasları çok kuvvetlidir."]):
        super().__init__(grup,yaşam_alanı,beslenme_çeşidi)
        self.cins = cins
        self.genel_özellikleri = genel_özellikleri
    def __str__(self):
        return  ("ATLARIN GENEL ÖZELLİKLERİ \n1)Tür = {}\n2)Yaşam Alanı = {}\n3)Beslenme Çeşidi = {}\n4)Cinsleri = {}\n5)Genel Özellikleri = {}".format(self.grup,self.yaşam_alanı,self.beslenme_çeşidi,self.cins,self.genel_özellikleri))
    def cins_ekle(self,):
        a = input("Eklemek istediğiniz cinsi giriniz:")
        print("Ekleniyor...")
        time.sleep(2)
        self.cins.append(a)
    def özellik_ekleme(self):
        b = input("Eklemek istediğiniz özelliği giriniz:")
        print("Ekleniyor...")
        time.sleep(2)
        self.genel_özellikleri.append(b)
print("""
*******************************************************************
HAYVANLAR ALEMİNİN ORTAK ÖZELLİKLERİ

1) Hayvanların Ortak Özellikleri
2) Köpeklerin Ortak Özellikleri
3) Kuşların Ortak Özellikleri
4) Atların Ortak Özellikleri

(Çıkış yapmak için 'q' ya basınız.)
********************************************************************
""")
while True:
    a = input("Lütfen göz atmak istediğiniz seçeneği yazınız:")
    if a == "1":
        hayvan=Hayvanlar()
        print(hayvan)
    elif a == "2":
       köpek = Köpekler()
       print(köpek)
       time.sleep(2)
       print("""
       ***************
       KÖPEKLER:
       1)Cins Ekle
       2)Özellik Ekle
       3)Çıkış
       ***************
       """)
       b = input("Lütfen işlem yapmak istediğiniz numarayı seçiniz:")
       if b == "1":
           köpek.cins_ekle()
       elif b == "2":
           köpek.özellik_ekleme()
       elif b == "3":
           print("Bu menüden çıkış yapılıyor...")
           time.sleep(1)
       else:
           print("Lütfen geçerli bir işlem seçiniz.\nAna menüye dönülüyor...")
           time.sleep(2)
    elif a == "3":
       kuş = Kuşlar()
       print(kuş)
       time.sleep(2)
       print("""
       ***************
       KUŞLAR:
       1)Cins Ekle
       2)Özellik Ekle
       3)Çıkış
       ***************
       """)
       b = input("Lütfen işlem yapmak istediğiniz numarayı seçiniz:")
       if b == "1":
           kuş.cins_ekle()
       elif b == "2":
           kuş.özellik_ekleme()
       elif b == "3":
           print("Bu menüden çıkış yapılıyor...")
           time.sleep(1)
       else:
           print("Lütfen geçerli bir işlem seçiniz.\nAna menüye dönülüyor...")
           time.sleep(2)
    elif a == "4":
       at = Atlar()
       print(at)
       time.sleep(2)
       print("""
       ***************
       ATLAR:
       1)Cins Ekle
       2)Özellik Ekle
       3)Çıkış
       ***************
       """)
       b = input("Lütfen işlem yapmak istediğiniz numarayı seçiniz:")
       if b == "1":
           at.cins_ekle()
       elif b == "2":
           at.özellik_ekleme()
       elif b == "3":
           print("Bu menüden çıkış yapılıyor...")
           time.sleep(1)
       else:
           print("Lütfen geçerli bir işlem seçiniz.\nAna menüye dönülüyor...")
           time.sleep(2)
    elif a == "q":
        print("Program kapatılıyor...")
        time.sleep(1)
        break
    else:
        print("Lütfen geçerli bir işlem seçiniz!...")