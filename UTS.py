total =0
while True:
    print ('Silahkan Pilih')
    print('1.Ganti Oli(Rp 150.000)')
    print('2.Tune up(Rp 300.000)')
    print('3.Balancing(Rp 100.000)')
    
    service = str(input('Masukan service:'))
    member = str(input('Masukan Status member:'))
    match service:
        case '1':
            harga = 150000
            nama_service = 'Ganti oli'
        case '2':
           harga = 300000
           nama_service = 'tune up'
        case '3':
            harga = 100000
            nama_service = 'balancing'
        case _:
            print('service tidak ada')
            continue
    match member:
        case 'member':
           diskon1 = 1.0
           diskon2 = 2.0
        case 'non member':
            diskon1n = 0
            diskon2n = 0.05
        case _:
            print('member salah')
    total += harga
    if member == 'member' in enumerate (service, start=1) :
       diskon = total - diskon2
    elif member == 'member':
        diskon = total - diskon1
    elif member == 'non member'in enumerate (service, start=0):
        diskon = total - 0
    elif member == 'non member':
        diskon = total - diskon2n
    print('total:',total)
    print('member:',member)
    print ('harga:',harga)
    print('harga setelah di diskon:',diskon)
    print('nama service:',nama_service)
 
    nanya = str(input('igin membeli baru?ya/tidak:'))
    if nanya.lower() == 'tidak':
        break
print('Bengkel tutup')