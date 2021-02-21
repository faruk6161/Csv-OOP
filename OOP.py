'''
    Coded by FARUK OKSUZ
                        '''

import csv
import statistics
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
ogrencilerListesi=[]

class Ogrenci:
    def __init__(self , ogrNo,ad,soyad,vize1,vize2,final):
        self.ogrNo = ogrNo
        self.ad = ad
        self.soyad = soyad
        self.vize1 = vize1
        self.vize2 = vize2
        self.final = final
        
    def BasariNotuHesapla(self):
        self.durum="GEÇTİ"
        self.basariNotu= round(int(self.vize1)* 0.2+ int(self.vize2)*0.3+int(self.final)*0.5)
        
        if self.basariNotu >= 90 and self.basariNotu <= 100:
            self.harfNotu = "AA"
            self.durum="GEÇTİ"
        elif self.basariNotu >= 85 and self.basariNotu < 90:
            self.harfNotu = "BA"
            self.durum="GEÇTİ"
        elif self.basariNotu >= 80 and self.basariNotu < 85:
            self.harfNotu = "BB"
            self.durum="GEÇTİ"
        elif self.basariNotu >= 75 and self.basariNotu < 80:
            self.harfNotu = "CB"
            self.durum="GEÇTİ"
        elif self.basariNotu >= 70 and self.basariNotu < 75:
            self.harfNotu = "CC"
            self.durum="GEÇTİ"
        elif self.basariNotu >= 65 and self.basariNotu < 70:
            self.harfNotu = "DC"
            self.durum="GEÇTİ"
        elif self.basariNotu >= 60 and self.basariNotu < 65:
            self.harfNotu = "DD"
            self.durum="GEÇTİ"
        elif self.basariNotu >= 50 and self.basariNotu < 60:
            self.harfNotu = "FD"
            self.durum = "ŞARTLI GEÇTİ"
        elif self.basariNotu <= 49:
            self.harfNotu = "FF"
            self.durum = "KALDI"
               
def KayitListele():
    for ogrenci in ogrencilerListesi:
        print(ogrenci.ogrNo , ogrenci.ad , ogrenci.soyad , ogrenci.vize1 , ogrenci.vize2 , ogrenci.final , ogrenci.basariNotu , ogrenci.harfNotu , ogrenci.durum)
      
def IstatikselBilgiler():
    aa,ba,bb,cb,cc,dc,dd,fd,ff = 0, 0, 0, 0, 0, 0, 0, 0, 0
    sinifOrtalamasi = round(statistics.mean([ogrenci.basariNotu for ogrenci in ogrencilerListesi]))
    standartSapma=round(statistics.stdev([ogrenci.basariNotu for ogrenci in ogrencilerListesi]))
    maxNot=max([ogrenci.basariNotu for ogrenci in ogrencilerListesi])
    minNot=min([ogrenci.basariNotu for ogrenci in ogrencilerListesi])
    harfString = ['AA','BA','BB','CB','CC','DC','DD','FD','FF']
    
    for ogrenci in ogrencilerListesi:
        if ogrenci.harfNotu=="AA":
            aa+=1
        elif ogrenci.harfNotu=="BA":
            ba+=1
        elif ogrenci.harfNotu=="BB":
            bb+=1
        elif ogrenci.harfNotu=="CB":
            cb+=1
        elif ogrenci.harfNotu=="CC":
            cc+=1
        elif ogrenci.harfNotu=="DC":
            dc+=1
        elif ogrenci.harfNotu=="DD":
            dd+=1
        elif ogrenci.harfNotu=="FD":
            fd+=1
        elif ogrenci.harfNotu=="FF":
            ff+=1
            
    print("Sinif Ortalamasi : {}".format(sinifOrtalamasi))
    print("Sinif Standart Sapma : {}".format(standartSapma))
    print("Sinif Maksimum Not : {}".format(maxNot))
    print("Sinif Minimum Not : {}".format(minNot))
    
    harfNotlariSayisi=[aa,ba,bb,cb,cc,dc,dd,fd,ff]
    plt.bar(harfString , harfNotlariSayisi,)
    plt.xlabel("Harf Notlari")
    plt.ylabel("Sayısı")
    plt.show()
    
    xMin , xMax =0.0 , 100.0
    x = np.linspace(xMin, xMax, 100)
    y = scipy.stats.norm.pdf(x,sinifOrtalamasi,standartSapma)
    plt.plot(x,y, color='coral')
    plt.xlabel("Notlar")
    plt.title("ÇAN EĞRİSİ")
    plt.show()
    
def DosyadanOku():
    with open('Sinif.csv', 'r') as read_obj:
        csv_reader = csv.reader(read_obj)
        for kayit in csv_reader:
            ogr=Ogrenci(*kayit) # kayıt sayısı kadar nesne oluşturuldu .
            ogrencilerListesi.append(ogr)
    print("Dosyadan başarıyla okuma gerçekleşti ! \n")
  
def DosyayaYaz():
    with open("Output.csv", "w", newline="",encoding="utf-8") as dosya:
       yaz = csv.writer(dosya)
       for ogrenci in ogrencilerListesi:
           yaz.writerow([ogrenci.ogrNo , ogrenci.ad,ogrenci.soyad,ogrenci.basariNotu,ogrenci.harfNotu,ogrenci.durum])
   
    print("Dosyaya yazma işlemi başarıyla gerçekleşti ! \n")
    
    
def BasariNotunaGoreSirala(): 
    def BasariNotunaGore(ogrenci):
        return ogrenci.basariNotu
    
    ogrencilerListesi.sort(key=BasariNotunaGore , reverse=True)
    
    print("Öğrenciler başarı notuna göre sıralandı ! \n")
    
def KayitSil():
    ogrNo = int(input("Kayıtlı silinecek olan ögrenci numarasını giriniz : "))
    if ogrNo in [ int(kisi.ogrNo) for kisi in ogrencilerListesi]:
        ogrencilerListesi.pop(ogrNo)
        print("Öğrenci başarıyla silindi ! \n")
    else:
        raise Exception("Böyle bir öğrenci bulunmamaktadır ! \n")    
           
def KayitEkle():
    ogrNo = int(input("Yeni kayıt için Ogrenci numarasını giriniz : "))
    
    if ogrNo in [ int(kisi.ogrNo) for kisi in ogrencilerListesi]:
        raise Exception("Öğrenci numarası zaten var !")
    else:    
        ad = input("Ad giriniz :")
        soyad = input("Soyad giriniz :")
        vize1 = int(input("Vize1 giriniz :"))
        vize2 = int(input("Vize2 giriniz :"))
        final = int(input("Final giriniz :"))   
        ogr = Ogrenci(ogrNo , ad , soyad , vize1 , vize2 , final)
        ogrencilerListesi.append(ogr)
        print("Ogrenci eklendi ! \n")

    ogr.BasariNotuHesapla()
    



def KayitGuncelle():
    ogrNo = int(input("Kaydı güncellenecek olan ögrenci numarasını giriniz : "))
    if ogrNo in [ int(kisi.ogrNo) for kisi in ogrencilerListesi]:
            ogrencilerListesi[ogrNo].ad = input("Yeni ad gir :")
            ogrencilerListesi[ogrNo].soyad = input("Yeni soyad gir :")
            ogrencilerListesi[ogrNo].vize1 = int(input("Yeni vize1 gir :"))
            ogrencilerListesi[ogrNo].vize2 = int(input("Yeni vize2 gir :"))
            ogrencilerListesi[ogrNo].final = int(input("Yeni final gir :"))
            print("Öğrenci başarıyla güncellendi ! \n")
    else:
        raise Exception("Böyle bir öğrenci bulunamadı !")

    


def main():
    print("\n Lütfen önce 1 ve 2 numaralı işlemleri yapınız !")
    print("""
          1- Dosyadan Oku ( Csv ) 
          2- Basari Notuna Gore Sirala
          3- Kayit Ekle 
          4- Kayit Sil 
          5- Kayit Güncelle 
          6- Kayit Listele 
          7- İstatiksel Bilgiler
          8- Dosyaya Yaz
          9- Çıkış
          """)
    while True:
        secim=int(input("İşlem numarasını giriniz ? :"))
         
        if secim==1:
            DosyadanOku()   
            
        elif secim==2:
            for ogrenci in ogrencilerListesi:
                ogrenci.BasariNotuHesapla()
                
            BasariNotunaGoreSirala()
            
        elif secim==3:
            KayitEkle()
            
        elif secim==4:
            KayitSil()
            
        elif secim==5:
            KayitGuncelle()
            
        elif secim==6:
            KayitListele()
            
        elif secim==7:
            IstatikselBilgiler()
            
        elif secim==8:
            print(" Basariyla dosyaya yazildi \n")
            DosyayaYaz()
            
        elif secim==9:
            print(" Çıkış yaptınız \n ")
            break
                
if __name__ == "__main__":
    main()
