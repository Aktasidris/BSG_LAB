# Şifrelemek için kullanılan anahtar
anahtar = 3
def kelimeyi_sifrele(kelime):
    sifreli_kelime = ""
    for harf in kelime:
        if harf.isalpha():
            # Harfi kaydır ve sifreli_kelime'ye ekle
            sifreli_kelime += chr(((ord(harf) - 97 + anahtar) % 26) + 97)
        else:
            # Harf değilse doğrudan ekleyin
            sifreli_kelime += harf
    return sifreli_kelime
def sifreyi_coz(sifreli_kelime):
    orijinal_kelime = ""
    for harf in sifreli_kelime:
        if harf.isalpha():
            # Harfi kaydır ve orijinal_kelime'ye ekle
            orijinal_kelime += chr(((ord(harf) - 97 - anahtar) % 26) + 97)
        else:
            # Harf değilse doğrudan ekleyin
            orijinal_kelime += harf
    return orijinal_kelime
kelime = input("Şifrelemek istediğiniz kelimeyi girin: ")

sifreli_kelime = kelimeyi_sifrele(kelime)
print("Şifrelenmiş kelime: " + sifreli_kelime)

# Şifreyi çözün
cozulmus_kelime = sifreyi_coz(sifreli_kelime)
print("Çözülmüş kelime: " + cozulmus_kelime)