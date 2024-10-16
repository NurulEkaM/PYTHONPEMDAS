apple = 10000
diskon = int
total_dikon = int
jml = int
jml = int(input("masukan jumlah kg:"))
if jml >= 5:
    total = jml * apple
    print("total:Rp", total,"anda mendapat diskon!")
    diskon = jml * 0.05
    print("diskon:",diskon)
    total_dikon = total - diskon
    print("total diskon:Rp",total_dikon)
else:
    total = jml * apple
    print("total:",total)
    