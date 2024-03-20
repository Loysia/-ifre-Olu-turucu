import random

karakterler  ="+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"



def sifre_olustur(uzunluk):
    sifre = ""

    for i in range (cevap):
        sifre += random.choice(karakterler)

    print(sifre)
    return sifre



while True:
    hesap = input("Hangi hesabın için şifre istiyorsun?\n") 
    cevap = int(input("Kaç karakterli bi şifre istiyorsun?\n"))
    if cevap <= 0:
        break
    with open("sifreler.txt" , "a") as doc:
        doc.write(f"{hesap} : {sifre_olustur(cevap)}\n")