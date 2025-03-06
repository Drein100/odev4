# ogrenciler.txt dosyasına öğrenci isimleri ekler ve ardından okur

def ogrencileri_oku():     
    with open("ogrenciler.txt", "r") as dosya:         
        print(dosya.read())

with open("ogrenciler.txt", "a") as dosya:     
    while True:         
        isim = input("Öğrenci ismi girin (Çıkmak için 'bitti' yazın): ")         
        if isim.lower() == "bitti":  
            break         
        dosya.write(isim + "\n")  

ogrencileri_oku()           
