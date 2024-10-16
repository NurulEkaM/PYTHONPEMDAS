buah = str(input("masukan buah:"))
if buah == "mangga":
    harga = 12000
elif buah == "jeruk":
    harga = 15000
else:
    harga=10000
        
k = int(input("masukan jumlah kg:"))
if k >= 5 and buah == "mangga" :
    diskon = 5/100
elif k>=5 and buah == "jeruk":
    diskon = 5/100
else:
    diskon = 0
    
total = k * harga
total_dis = total - diskon
print ("total:Rp",total)   
print("diskon:",diskon)
print ("total bayar:Rp", total_dis)