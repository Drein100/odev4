# Kullanıcının telefon numaralarını kaydetmesini, aramasını ve listelemesini sağlar

dosya_adi = "rehber.txt"
while True:
    komut = input("Komut girin (ekle, ara, listele, cikis): ")
    if komut == "ekle":
        ad = input("Ad: ")
        numara = input("Telefon: ")
        with open(dosya_adi, "a") as dosya:
            dosya.write(f"{ad}: {numara}\n")
    elif komut == "ara":
        aranan = input("Aranacak isim: ")
        with open(dosya_adi, "r") as dosya:
            for satir in dosya:
                if aranan in satir:
                    print(satir.strip())
    elif komut == "listele":
        with open(dosya_adi, "r") as dosya:
            print(dosya.read())
    elif komut == "cikis":
        break