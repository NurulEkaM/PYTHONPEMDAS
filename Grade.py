# bil = int(input("masukan nilai:"))
# if bil >= 81:
#     print ("a")
# elif bil >= 71:
#     print ("b")
# elif bil >= 61:
#     print("c")
# elif bil >= 59:
#     print("d")
# else:
#     print ("e")

while True:
    bil = int(input('bil:'))
    
    match bil:
        case 1001:
            print('kamu melebihi nilai')
            if bil >= 81:
                print('a')
 