def çiftsayı(sayı):

    if(sayı % 2 == 0):
        return sayı
    else:
        raise ValueError
liste = [34,2,1,3,33,100,61,1800]

for i in liste:

    try:
        print(çiftsayı(i))
    except ValueError:
        print("Bu Sayı 2 ile tam bölünmüyor...") 