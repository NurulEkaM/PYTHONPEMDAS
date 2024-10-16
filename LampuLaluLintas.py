# warna = str(input("masukan warna:"))
# if warna == "kuning":
#     print("hati hati")
# elif warna == "hijau":
#     print("maju")
# elif warna == "merah":
#     print("berhenti")
# else :
#     print ("warna salah")

while True:
    warna = str(input('masukan warna:'))

    match warna:
        case 'merah':
            print('berhenti')
            tanya =str(input('apakah kamu mau mengulangi?ya/tidak:'))
            if tanya == 'tidak':
                break
        case 'hijau':
            print('maju')
            tanya =str(input('apakah kamu mau mengulangi?ya/tidak:'))
            if tanya == 'tidak':
                break
        case 'kuning':
            print('hati hati')
            tanya =str(input('apakah kamu mau mengulangi?ya/tidak:'))
            if tanya == 'tidak':
                break
        case _:
            print('warna salah')
print('program selesai')