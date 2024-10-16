a = int (input('Lama detik:' ))

jam = a // 3600 #hitung jumlah jam
b = a % 3600   #sisa jam 
menit = b // 60 #hitung jumlah menit
detik = b % 60  #hitung jumlah detik
print ('Jam :', jam)
print ('Menit :', menit)
print ('Detik :', detik)