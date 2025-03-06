# Sistem çalışırken belirli aralıklarla log kaydı oluşturur ve görüntüler

import time

dosya_adi = "log.txt"
def loglari_goruntule():
    with open(dosya_adi, "r") as dosya:
        print(dosya.read())
        
while True:
    with open(dosya_adi, "a") as dosya:
        zaman = time.strftime("%Y-%m-%d %H:%M:%S")
        dosya.write(f"Sistem çalışıyor: {zaman}\n")
    time.sleep(10)
    komut = input("Komut girin (logları görüntüle): ")
    if komut == "logları görüntüle":
        loglari_goruntule()
    else:
        break

