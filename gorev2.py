# Kullanıcının not almasını, notları görüntülemesini ve silmesini sağlar

import os

dosya_adi = "gunluk.txt"
while True:
    komut = input("Komut girin (not, goruntule, sil, cikis): ")
    if komut == "not":
        not_girisi = input("Notunuzu girin: ")
        with open(dosya_adi, "a") as dosya:
            dosya.write(not_girisi + "\n")
    elif komut == "goruntule":
        with open(dosya_adi, "r") as dosya:
            print(dosya.read())
    elif komut == "sil":
        os.remove(dosya_adi)
        print("Günlük silindi.")
    elif komut == "cikis":
        break