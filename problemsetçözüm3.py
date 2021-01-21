girdi = None
dizi = []
#Çıkmak için 'x' veya 'X' yazınız.
while True:
    girdi = input("Sayı giriniz :")

    try:
        if girdi == "x" or girdi == "X":
            break
        elif girdi == "0":
            dizi.insert(0, int(girdi))
        else:
            dizi.append(int(girdi))
    except:
        print("Lütfen sayı yazın")

print("Dizi: ", dizi)