asci = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', ]


def dekripsi(hasil,kunci):
    kunci_2 = ""
    index_kunci = -1
    for i in range(len(hasil)):
        if hasil[i].lower() in asci:
            index_kunci += 1
            kunci_2 += kunci[index_kunci % len(kunci)].lower()
        else:
            kunci_2 += hasil[i].lower()
    kalimat = ""

    for i in range(len(hasil)):
        try:
            i_kata = (asci.index(hasil[i].lower()) - asci.index(kunci_2[i]))
            if hasil[i].isupper():
                kalimat += asci[i_kata].upper()
            else:
                kalimat += asci[i_kata]
        except ValueError:
            if hasil[i].isupper():
                kalimat += hasil[i].upper()
            else:
                kalimat += hasil[i]
    return kalimat


def enkripsi(kalimat, kunci):
    kunci_2 = ""
    index_kunci = -1
    for i in range(len(kalimat)):
        if kalimat[i].lower() in asci:
            index_kunci += 1
            kunci_2 += kunci[index_kunci % len(kunci)].lower()
        else:
            kunci_2 += kalimat[i].lower()
    hasil = ""

    for i in range(len(kalimat)):
        try:
            i_hasil = (asci.index(kalimat[i].lower()) + asci.index(kunci_2[i])) % 26
            if kalimat[i].isupper():
                hasil += asci[i_hasil].upper()
            else:
                hasil += asci[i_hasil]
        except ValueError:
            if kalimat[i].isupper():
                hasil += kalimat[i].upper()
            else:
                hasil += kalimat[i]
    
    hasil = hasil.replace(' ', '_')
    hasil = hasil.upper()
    
    return hasil


import os

while True:
    print('Pilih: \n1. Enkprisi Polyalphabetic\n2. Dekripsi Polyalphabetic')
    try:
        pilihan = int(input('\nMasukkan nomor pilihan: '))
    except:
        pilihan = 0
    if pilihan == 1:
        kalimat = input('\nMasukkan kalimat: ')
        kunci = input('Masukkan kunci: ')
        print("Hasil enkripsi:", enkripsi(kalimat, kunci))
    elif pilihan == 2:
        kalimat = input('\nMasukkan kalimat: ')
        kunci = input('Masukkan kunci: ')
        print("Hasil dekripsi:", dekripsi(kalimat, kunci))
    else:
        print('\nMasukkan pilihan yang benar!')

    replay = input('Ulangi program (y/t)?')
    if replay.lower() != 'y':
        break
