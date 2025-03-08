import time
import sys

def yazi_yaz(yazi, hiz=0.05):
    """
    Yazıyı klavye ile yazılıyormuş gibi yavaşça yazdırır.
    yazi: Yazılacak metin
    hiz: Harfler arasındaki bekleme süresi (varsayılan: 0.05 saniye)
    """
    for karakter in yazi:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(hiz)
    print()  # Satır sonu için


def main():
    #Güzel bir Karşılama ve bilgi verme
    yazi_yaz("Quize Hoşgeldiniz Şimdi size 5 soru sorucağız. Her bir soru 20 puandır.")
    puan = 0
    yazi_yaz("Başlayalım mı? evet/hayır ")
    start = input().lower()
    if start == "evet":
        #soru 1
        yazi_yaz("10 + 3 = ?")
        yazi_yaz("A - 10 \nB - 13 \nC - 7 \nD - 14 \nSadece şıkkı yazmanız yeterlidir. \n")
        cevap = input().capitalize()
        if cevap == "B":
            yazi_yaz("Tebrikler Doğru cevap ")
            puan += 20
        else:
            yazi_yaz("Yanlış Cevap")
        time.sleep(2)

        #soru 2
        yazi_yaz("145 + 3 = ?")
        yazi_yaz("A - 148 \nB - 13 \nC - 7 \nD - 14 \nSadece şıkkı yazmanız yeterlidir. \n")
        cevap = input().capitalize()
        if cevap == "A":
            yazi_yaz("Tebrikler Doğru cevap ")
            puan += 20
        else:
            yazi_yaz("Yanlış Cevap")
        time.sleep(2)

        #soru 3
        yazi_yaz("1 + 14 = ?")
        yazi_yaz("A - 14 \nB - 25 \nC - 15 \nD - 1 \nSadece şıkkı yazmanız yeterlidir. \n")
        cevap = input().capitalize()
        if cevap == "C":
            yazi_yaz("Tebrikler Doğru cevap ")
            puan += 20
        else:
            yazi_yaz("Yanlış Cevap")
        time.sleep(2)

        #soru 4
        yazi_yaz("100 + 3 = ?")
        yazi_yaz("A - 103 \nB - 1314 \nC - 4 \nD - 14 \nSadece şıkkı yazmanız yeterlidir. \n")
        cevap = input().capitalize()
        if cevap == "B":
            yazi_yaz("Tebrikler Doğru cevap ")
            puan += 20
        else:
            yazi_yaz("Yanlış Cevap")
        time.sleep(2)

        #soru 5
        yazi_yaz("10 + 311 = ?")
        yazi_yaz("A - 321 \nB - 1 \nC - 410 \nD - 41 \nSadece şıkkı yazmanız yeterlidir. \n")
        cevap = input().capitalize()
        if cevap == "A":
            yazi_yaz("Tebrikler Doğru cevap ")
            puan += 20
        else:
            yazi_yaz("Yanlış Cevap")
        time.sleep(2)

        yazi_yaz(f"Tebrikler Quizi Bitirdiniz. Puanınız: {puan}")
    else:
        yazi_yaz("Quiz iptal edildi. İyi günler")
        
main()