print("""
Carpim Tablosu Olusturma Programi
""")

x = int(input("Hangi sayi araliginda carpim tablosu olusturmak istersiniz\nBaslangic degeri(en az 1 olmali):"))
y = int(input("Bitis degeri:"))

for i in range(x,y+1):
    if x==0:
        print("Lutfen 0'dan farkli bir sayi giriniz ve tekrar deneyiniz.")
        break
    print("****************")
    for j in range(1,11):
        print("{}*{}={}".format(i,j,i*j))