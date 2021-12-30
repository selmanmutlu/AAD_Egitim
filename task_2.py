"""
1.
Create a deck of cards class. Internally, the deck of cards should use another class, a card class. Your requirements are:

-The Deck class should have a deal method to deal a single card from the deck
After a card is dealt, it is removed from the deck.
-There should be a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
-The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
"""


"""
*2.
basit bir drone classı yaratın her dronun sahip olması gerek standart özellikler:

*id,
*x,y,z kordinatları
*hızı,
*taşıyabiliceği yük,
*batarya,
her dronun sahip olması gereken fonksiyonlar(Bu fonksiyonlar hayali bir drone için calışmalı mesela takeoff komutunu verdiğinizde ucağın kalkmasını değil sadece y değerinin takeoff komutunda verdiğiniz yüksekliğe eşitlenmesini istiyorum, aynı şekilde (10,5,20) noktasına git dediğinizde gercekten oraya giden bir drone deil xyz si bu birimlere eşitlenmesini istiyorum),

*takeoff
*return to launch
*move
*yük al
*yük bırak,
*kalkış noktasına uzaklık,
"""
import time
class Drone():

    def __init__(self,id,koordinat,hız,taşıyabiliceği_yük,batarya):
        self.id = id
        self.koordinat = koordinat
        self.hız = hız
        self.taşıyabiliceği_yük = taşıyabiliceği_yük
        self.batarya = batarya

    def __str__(self):
        return "Drone ID: {}\nKoordinatları: {}\nHızı: {}\nTaşıyabiliceği Yük: {}\nBatarya: {}".format(self.id,self.koordinat,self.hız,self.taşıyabiliceği_yük,self.batarya)

    def takeoff(self):
        a = input("Drone'u havalandırmak istediğiniz y koordinatını giriniz:")
        b = int(input("Seyahat hızını giriniz:"))
        print("Drone havalanıyor...")
        time.sleep(2)
        self.koordinat["y"] = a
        self.hız = b
        print("Yeni koordinatlar {}\nHızı: {}".format(self.koordinat,self.hız))

    def return_to_launch(self):
        if self.koordinat["x"] == 0 and self.koordinat["y"] == 0 and self.koordinat["z"] == 0:
            print("Drone zaten başlangıç noktasında!...")
        else:
            print("Başlangıç noktasına dönülüyor...")
            time.sleep(2)
            self.koordinat["x"] = 0
            self.koordinat["y"] = 0
            self.koordinat["z"] = 0
            print("Drone başlangıç noktasına geri dönüş yaptı.\nKoordinatları = {}".format(self.koordinat))

    def move(self,x,y,z,v):
        print("Drone istediğiniz koordinatlara ilerliyor...")
        time.sleep(2)
        self.koordinat["x"] = x
        self.koordinat["y"] = y
        self.koordinat["z"] = z
        self.hız = v
        print("Drone ' un son konumu {}\nHızı: {}".format(self.koordinat,self.hız))

    def uzaklık(self):
        a = (x**2 + y**2 + z**2) ** 0.5
        a = int(a)
        print("Drone'un başlangıç noktasına olan uzaklığı {} birim".format(a))

    def yük_al(self):
        koordinat = input("Alıcağınız yükün koordinatlarını virgün(,) koyarak giriniz:")
        yük = int(input("Almak istediğiniz ağırlığı giriniz:"))
        if yük > self.taşıyabiliceği_yük:
            print("Drone bu ağırlığı kaldıracak kapasitede değil!...")
        else:
            print("Drone koordinatlara yönlendiriliyor...")
            time.sleep(3)
            liste = koordinat.split(",")
            self.koordinat["x"] = liste[0]
            self.koordinat["y"] = liste[1]
            self.koordinat["z"] = liste[2]
            print("Drone varış noktasına ulaştı\nDrone konumu: {}\nYük alınıyor..".format(self.koordinat))
            time.sleep(3)
            print("Yük başarıyla alındı.")

    def yük_bırak(self):
        koordinat = input("Yükü bırakmak istediğiniz koordinatları virgün(,) koyarak giriniz:")
        print("Drone koordinatlara yönlendiriliyor...")
        time.sleep(3)
        liste = koordinat.split(",")
        self.koordinat["x"] = liste[0]
        self.koordinat["y"] = liste[1]
        self.koordinat["z"] = liste[2]
        print("Drone varış noktasına ulaştı\nDrone konumu: {}\nYük bırakılıyor...".format(self.koordinat))
        time.sleep(3)
        print("Yük başarıyla bırakıldı.")

AAD_Drone = Drone(id = "412639",koordinat = {"x": 0, "y": 0, "z": 0},hız=0,taşıyabiliceği_yük= 10 ,batarya="%100")

print("""
*****************************************************
DRONE KULLANICI PANELİ

1)Drone Bilgileri
2)Kalkış
3)Başlangıca Geri Dönüş
4)Hareket
5)Yük Al
6)Yük Bırak
7)Başlangıç Noktasına Olan Uzaklık

(Lütfen kapatmak için 'q' yu tuşlayın...)
*****************************************************
""")
while True:
    komut = input("Lütfen komut seçiniz:")
    if komut == "q":
        print("Panel kapatılıyor...")
        time.sleep(2)
        break
    elif komut == "1":
        print(AAD_Drone)
    elif komut == "2":
        AAD_Drone.takeoff()
    elif komut == "3":
        AAD_Drone.return_to_launch()
    elif komut == "4":
        x = int(input("Lütfen varış noktasının x koordinatını giriniz:"))
        y = int(input("Lütfen varış noktasının y koordinatını giriniz:"))
        z = int(input("Lütfen varış noktasının z koordinatını giriniz:"))
        v = int(input("Lütfen seyahat hızını giriniz:"))
        AAD_Drone.move(x,y,z,v)
    elif komut == "5":
        AAD_Drone.yük_al()
    elif komut == "6":
        AAD_Drone.yük_bırak()
    elif komut == "7":
        AAD_Drone.uzaklık()
    else:
        print("Lütfen geçerli bir komut giriniz!...")

"""
*3.
1000 int den oluşan random bir liste yaratın ve istediğiniz sorting algoritmasını kullanarak küçükten büyüğe sıralayan bir script yazınız.
"""
import random

liste1 = []
liste2 = []
for i in range(0,1000):
        liste1.append(random.randint(0,2000))

liste2 = sorted(liste1)
print(liste1)
print("******************")
print(liste2)
#tam anlayamadım ama sanırım ödev böyle

"""
*4.
n katlı bir gökdelende olduğunuzu farz edin, elinizde 2 adet yumurta var. amacınız yumurtanın kırılmadan atılabileceği en yüksek katı bulmak. yumurtayı atmak için k adet deneme yapabilirsiniz ve yumurta herhangi bir katta kırılabilir (evet herhangi bir kat)

n verilen k değerine göre en fazla kaç olabilir?
"""
"""
binary search algoritmasıyla yapmayı denedim.
örnek olarak 3 deneme hakkımız olduğunu varsayalım buna göre n değeri maksimum 8 olabiliyor, ilk denememizi de
en orta kattan 4. kattan yapıyoruz kırılmassa kalan üst yarının en ortasından yani 6. kattan 2. denemeyi gerçekleştiriyoruz
bu katta yumurtanın kırıldığını varsayalım bu seferde 4. kat ile 6. katın ortası yani 5. kattan 3. denememizi yapıyoruz,
yumurtanın kırılıp kırılmamasına göre 3. denememizde sonuca ulaşmış oluyoruz. 
"""
deneme_hakkı = int(input("Kaç adet deneme hakkınız olsun? :"))

en_yüksek_kat = 2 ** deneme_hakkı

print("Deneme sayınıza göre maksimum {} katlı bir gökdelende atış yapabilirsiniz.".format(en_yüksek_kat))


"""
*5.
bir sayının cift olup olmadığını hesaplayan en iyi fonksiyonu yazmaya calışın. (diyer katılımcılarla karşılaştırılacak)

"""
def çiftmi_tekmi(sayı):

    if sayı % 2 == 0:
        print("{}  çift sayıdır.".format(sayı))

    else:
        print("{}  tek sayıdır. ".format(sayı))


sayı = int(input("Lütfen sayınızı giriniz:"))
print(çiftmi_tekmi(sayı))