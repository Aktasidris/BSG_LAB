import random
import itertools
def Sifre_Uret(karakter, uzunluk, tekrar_onay):
    if not karakter:
        print("Geçerli bir giriş yapmadınız.")
        return
    karisik_giris = ''.join(random.sample(karakter, len(karakter)))

    if tekrar_onay:
        #kartezyen çarpımmı yapar
        kombinasyonlar = [''.join(x) for x in itertools.product(karisik_giris, repeat=uzunluk)]
    else:
        if uzunluk > len(karisik_giris):
            print("Karakterlerin tekrarı kullanılmadığı için şifre bu kadar uzun olamaz.")
            return
        #olasılıkların permutasyonlarını alır
        kombinasyonlar = [''.join(x) for x in itertools.permutations(karisik_giris, uzunluk)]

    with open("sifreler.txt", "w") as dosya:
        for kombinasyon in kombinasyonlar:
            dosya.write(kombinasyon + "\n")
    print("Üretilen şifre kombinasyonları 'sifreler.txt' dosyasına kaydedildi.")

kullanici_girisi = input("Şifreleri oluşturacak karakterleri girin örn:(1234567890): ")
uzunluk = int(input("Şifrenin uzunluğunu belirleyin: "))
izin_verilen_tekrar = input("Karakterler tekrar kullanılsın mı? (E/H): ").lower() == 'e'

Sifre_Uret(kullanici_girisi, uzunluk, izin_verilen_tekrar)
