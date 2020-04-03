# rakamları farklı 4 (veya daha az) basamaklı bir sayı mı?
def kontrol(sayı):
    return str(sayı).isdigit() and len(set([harf for harf in str(sayı).rjust(4,"0")]))==4
    # eğer ilk basamakta sıfır olsun istemiyorsanız str(sayı)'nın sağındaki .rjust(4,"0") ifadesini silin

# olası bütün sayıları listele
def sıfırla():
    return [i for i in range(123,9877) if kontrol(i)]

# artı eksi hesabı
def hesapla(tutulan,tahmin):
    tutulan=str(tutulan).rjust(4,"0")
    tahmin=str(tahmin).rjust(4,"0")
    artı,eksi=0,0
    for i in range(0,4):
        for j in range(0,4):
            if tahmin[i]==tutulan[j]:
                if i==j:
                    artı+=1
                else:
                    eksi+=1
    return artı,eksi

# olası sayı listesini yeni tahmine göre küçültme işlemi
def küçült(liste,tahmin,artıeksi):
    return [sayı for sayı in liste if hesapla(sayı,tahmin)==artıeksi]

# bilgisayar bir sayı tutar, oyuncu tahmin eder
def bilgisayar():
    from random import choice
    liste=sıfırla()
    tutulan=choice(liste)
    print("Bir sayı tuttum. Bakalım bulabilecek misin?")
    while True:
        try:
            tahmin=input("Bir tahminde bulun: ")
            if tahmin==str(tutulan):
                print(f"TEBRİKLER! {tutulan} tutmuştum.")
                break
            else:
                if kontrol(tahmin):
                    artı,eksi=hesapla(tutulan,tahmin)
                    liste=küçült(liste,tahmin,(artı,eksi))
                    print(f"{tahmin.rjust(4,'0')} +{artı}-{eksi}")
                print(f"Listemizde {len(liste)} olasılık var.")
        except:
            print("Bir hata oldu. Baştan başlayalım.")
            bilgisayar()

# oyuncu bir sayı tutar, bilgisayar tahmin eder
def oyuncu(tutulan):
    from random import choice
    liste=sıfırla()
    print("Bakalım tuttuğun sayıyı bulabilecek miyim?")
    adet=0
    while True:
        try:
            adet+=1
            tahmin=choice(liste)
            artı,eksi=hesapla(tutulan,tahmin)
            print(f"{str(tahmin).rjust(4,'0')} +{artı}-{eksi}")
            if artı==4:
                print(f"{adet} tahminde buldum. Tebrik et beni.")
                break
            else:
                liste=küçült(liste,tahmin,(artı,eksi))
                print(f"Listemizde {len(liste)} olasılık var.")
        except:
            print("Bir hata oldu. Baştan başlayalım.")
            oyuncu(tutulan)
            break
