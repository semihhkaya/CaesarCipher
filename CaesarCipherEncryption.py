while True:
    print("Çıkmak için 0'a basın")
    def sezar(metin):
        sifre = ""
        alfabe=['a','b' ,'c' , 'd', 'e', 'f', 'g' ,'h' ,'i' ,'j','k' ,'l' ,'m' ,'n' ,'o' ,'p' ,'q' ,'r' ,'s' ,'t' ,'u' ,'v','w','x','y' ,'z']
        for i in metin:
            sifre+=alfabe[(alfabe.index(i)+k)%26]
        print("sifre :",sifre)
        return metin

    isim = input("metini giriniz : ")
    if isim=="0":
        break
    k = int(input("Anahtar değerini giriniz: "))
    sezar(isim)
