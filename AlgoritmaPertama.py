kodebrg = str(input("masukan kode barang:"))
if kodebrg == 'PK01':
    namabrg = 'pakaian'
    harga = 10000
    print("harga ",namabrg ,"Rp",harga)
elif kodebrg == 'TS02':
    namabrg = 'Tas'
    harga = 70000
    print("Harga ",namabrg ,"Rp",harga)
elif kodebrg == 'CL03':
    namabrg = 'Celana'
    harga = 90000
    print("Harga ",namabrg ,"Rp",harga)
else:
    print("Barang tidak ditemukan")