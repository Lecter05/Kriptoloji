
def msc(metin):  # metni sayısa çevir(msc)
    harf_sayi_eslesmesi = {'a': 0, 'b': 1, 'c': 2, 'ç': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'ğ': 8, 'h': 9,
    'ı': 10, 'i': 11, 'j': 12, 'k': 13, 'l': 14, 'm': 15, 'n': 16, 'o': 17, 'ö': 18,
    'p': 19, 'r': 20, 's': 21, 'ş': 22, 't': 23, 'u': 24, 'ü': 25, 'v': 26, 'y': 27,
    'z': 28, '_': 29, 'w': 30, 'q': 31, 'x': 32, '0': 33, '1': 34, '2': 35, '3': 36,
    '4': 37, '5': 38, '6': 39, '7': 40, '8': 41, '9': 42, '!': 43, '@': 44, '#': 45,
    '$': 46, '%': 47, '^': 48, '&': 49, '*': 50, '(': 51, ')': 52, '-': 53, '+': 54,
    '=': 55, '[': 56, ']': 57, '{': 58, ':': 59, '}': 60, '|': 61, ';': 62, '"': 63,
    "'": 64, '<': 65, '>': 66, ',': 67, '.': 68, '?': 69, '/': 70, ' ': 71}

    sayisal_metin = [harf_sayi_eslesmesi[harf] for harf in metin if harf in harf_sayi_eslesmesi]
    return sayisal_metin


def smc(sayi):  # sayıyı metine çevir(smc)
    sayi_harf_eslesmesi = {0: 'a', 1: 'b', 2: 'c', 3: 'ç', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'ğ', 9: 'h',
    10: 'ı', 11: 'i', 12: 'j', 13: 'k', 14: 'l', 15: 'm', 16: 'n', 17: 'o', 18: 'ö',
    19: 'p', 20: 'r', 21: 's', 22: 'ş', 23: 't', 24: 'u', 25: 'ü', 26: 'v', 27: 'y',
    28: 'z', 29: '_', 30: 'w', 31: 'q', 32: 'x', 33: '0', 34: '1', 35: '2', 36: '3',
    37: '4', 38: '5', 39: '6', 40: '7', 41: '8', 42: '9', 43: '!', 44: '@', 45: '#',
    46: '$', 47: '%', 48: '^', 49: '&', 50: '*', 51: '(', 52: ')', 53: '-', 54: '+',
    55: '=', 56: '[', 57: ']', 58: '{', 59: ':', 60: '}', 61: '|', 62: ';', 63: '"',
    64: "'", 65: '<', 66: '>', 67: ',', 68: '.', 69: '?', 70: '/', 71: ' '}

    metine_cevir = [sayi_harf_eslesmesi[sayi] for sayi in sayi if sayi in sayi_harf_eslesmesi]
    return metine_cevir


import numpy as np
from sympy import Matrix
from prettytable import PrettyTable


def sifrele_desire(metin, anahtar):

    kucult = metin.lower()

    # matris ile uygun bir formatta çarpılabilmesi için sonuna eklemeler yapılır(random).
    if len(kucult) % 3 == 1:
        for harfler in smc(np.random.randint(1, 10, size=2)):
            kucult += harfler
            print(metin)
    elif len(kucult) % 3 == 2:
        for harfler in smc(np.random.randint(1, 10, size=1)):
            kucult += harfler
            print(metin)

    sayi_metin = msc(kucult)

    metin_array_yap = np.array(sayi_metin)

    # -1 ifadesi NumPy'nin otomatik olarak satır sayısını hesaplamasını sağlar.
    matris_metin = metin_array_yap.reshape(-1, 3)

    # Metinin transpozunu al
    matris_metin_transpoz = matris_metin.transpose()

    # anahtar tanımlanır + 3x3 Matris haline getir.
    array_yap = np.array(anahtar)
    anahtar_matris = array_yap.reshape(3, 3)

    # Anahtar ile Metin matris çarpımı
    anahtar_metin_carpimi = np.dot(anahtar_matris, matris_metin_transpoz)

    # Çarpılan Matrisin modu
    sifreli_metin_matrix = np.mod(anahtar_metin_carpimi, 29)

    # Şireli matrisin transpozu al
    sifreli_metin_transpozu = sifreli_metin_matrix.transpose()

    # matrisi düz listeye çevir
    sifreli_metin_duz_dizi = sifreli_metin_transpozu.flatten()

    # matris içerisindeki sayıları harfe çevir
    sifreli_metin = smc(sifreli_metin_duz_dizi)

    sifreli_tam_kelime = ""
    for harfler in sifreli_metin:
        sifreli_tam_kelime += harfler

    # matrisin determinantı al
    det = int(round(np.linalg.det(anahtar_matris)))

    # Determinantı hesapla ve modunu al
    mod_det = det % 29

    try:
        # Determinantın modüler tersini hesapla
        det_tersi = pow(mod_det, -1, 29)
    except ValueError:
        print("Geçersiz anahtar! Determinantın modüler tersi yok.")
        return

    # Anahtar matrisin minör ve kofaktörünü al
    cofactor_matrix = [[Matrix(anahtar_matris).cofactor(i, j) for j in range(len(Matrix(anahtar_matris).row(0)))] for i in range(len(Matrix(anahtar_matris).col(0)))]

    # kofaktör matrisi değişkene atar
    kofaktor_dizi = [row for row in cofactor_matrix]

    # kofaktörü array'e çevirmeye yarar
    kofaktor_array = np.array(kofaktor_dizi)
    Matris_kofaktor = kofaktor_array.reshape(3, 3)

    Matris_kofaktor_Transpoz = Matris_kofaktor.transpose()

    # derterminantın tersi ile transpoz çarp
    det_ters_carpim_transpoz = Matris_kofaktor_Transpoz * det_tersi

    # derterminantın tersi ile transpoz çarpımının modu
    mod_carpim = np.mod(det_ters_carpim_transpoz, 29)

    # Matris tersi ile şifreli metinin çarp
    matris_tersi_carpi_sifreli_metin = np.dot(mod_carpim, sifreli_metin_matrix)

    # Matris tersi ile şifreli metinin çarpımının modu
    carpim_mod = np.mod(matris_tersi_carpi_sifreli_metin, 29)

    # modu alınan matrisin transpozu
    modun_transpozu = carpim_mod.transpose()

    # matris çarpımını düz yap
    duz_yap = modun_transpozu.flatten()

    # sayıyı metine çevir
    yazi_haline_Getir = smc(duz_yap)

    tam_kelime = ""
    for harf in yazi_haline_Getir:
        tam_kelime += harf

    BOLD = "\033[1m"
    yazdir1 = PrettyTable()
    yazdir1.field_names = ["\033[97mŞifrelenicek metin", "\033[97mŞifrelenmiş metin", "\033[97mMetinin son hali (random karakter eklenmiş)"]
    yazdir1.add_row([BOLD + f"\033[94m{metin}\033[0m", BOLD + f"\033[93m{sifreli_tam_kelime}\033[0m", BOLD + f"\033[94m{kucult}\033[0m"])
    print("\n", yazdir1, "\n")

    yazdir2 = PrettyTable()
    yazdir2.field_names = ["\033[97mMetinin sayısal hali", "\033[97mMetinin Şifreli sayısal hali"]
    yazdir2.add_row([BOLD + f"\033[94m{sayi_metin}\033[0m", BOLD + f"\033[93m{sifreli_metin_duz_dizi}\033[0m"])
    print(yazdir2)


sifrele_desire("deneme 1 2 3 / *", np.random.randint(1, 10, size=9))  # veya [1, 1, 0, 1, 0, 3, 0, 2, 0]
