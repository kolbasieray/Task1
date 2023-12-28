

#sayı al

sayi_listesi = input("Lütfen sayıları boşluk bırakarak girin: ")
sayilar = [int(sayi) for sayi in sayi_listesi.split()]


# Bubble Sort
n = len(sayilar)
for i in range(n):
    for j in range(0, n-i-1):
        if sayilar[j] > sayilar[j+1]:
            # Swap işlemi
            sayilar[j], sayilar[j+1] = sayilar[j+1], sayilar[j]

# Sıralanmış sayıları ekrana yazdır
print("Bubble Sort İle Sıralanmış Sayılar:", sayilar)
