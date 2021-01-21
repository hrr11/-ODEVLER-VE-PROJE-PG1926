girdi = None
dizi = []
büyük = 0
#Çıkmak için 'x' veya 'X' yazınız.
while True:
    girdi = input("Sayı giriniz :")

    try:
        if girdi == "x" or girdi == "X":
            break
        else:
            dizi.append(int(girdi))
    except:
        print('lütfen sayı giriniz')


print(format(dizi))

for i in dizi :
    if i % 2==1 and i>=büyük :
        büyük=i

print('en büyük tek sayı: ', büyük)