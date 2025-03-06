# Kullanıcı bilgilerini JSON dosyasında saklar ve listeler

import json
import os

dosya_adi = "kullanicilar.json"
if os.path.exists(dosya_adi):
    with open(dosya_adi, "r") as dosya:
        kullanicilar = json.load(dosya)
else:
    kullanicilar = []

while True:
    komut = input("Komut girin (ekle, listele, cikis): ")
    if komut == "ekle":
        ad = input("Ad: ")
        soyad = input("Soyad: ")
        yas = input("Yaş: ")
        kullanicilar.append({"ad": ad, "soyad": soyad, "yas": yas})
        with open(dosya_adi, "w") as dosya:
            json.dump(kullanicilar, dosya, indent=4)
    elif komut == "listele":
        with open(dosya_adi, "r") as dosya:
            for k in kullanicilar:
                print(f"{k['ad']} {k['soyad']} ({k['yas']})")
    elif komut == "cikis":
        break