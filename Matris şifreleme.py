# metni sayısa çevir(msc)
def msc(metin):
    harf_sayi_eslesmesi = {
        'a': 0, 'b': 1, 'c': 2, 'ç': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'ğ': 8,
        'h': 9, 'ı': 10, 'i': 11, 'j': 12, 'k': 13, 'l': 14, 'm': 15, 'n': 16,
        'o': 17, 'ö': 18, 'p': 19, 'r': 20, 's': 21, 'ş': 22, 't': 23, 'u': 24,
        'ü': 25, 'v': 26, 'y': 27, 'z': 28, '_': 29
    }
    sayisal_metin = [harf_sayi_eslesmesi[harf] for harf in metin if harf in harf_sayi_eslesmesi]
    return sayisal_metin

# sayıyı metine çevir(smc)
def smc(sayisal_dizge):
    sayi_harf_eslesmesi = {
        0: 'a', 1: 'b', 2: 'c', 3: 'ç', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'ğ',
        9: 'h', 10: 'ı', 11: 'i', 12: 'j', 13: 'k', 14: 'l', 15: 'm', 16: 'n',
        17: 'o', 18: 'ö', 19: 'p', 20: 'r', 21: 's', 22: 'ş', 23: 't', 24: 'u',
        25: 'ü', 26: 'v', 27: 'y', 28: 'z', 29: '_'
    }
    metine_cevir = [sayi_harf_eslesmesi[sayi] for sayi in sayisal_dizge if sayi in sayi_harf_eslesmesi]
    return metine_cevir

import numpy as np
from sympy import Matrix
from prettytable import PrettyTable

# Metin gir
metin = input("Metni giriniz(max 9): ")

kucult = metin.lower()

# Girilene metnin 3x3 matris olabilmesi için
metin = (kucult + "________")[:9]

# Girilen metni sayıya çevir
sayi_metin = msc(metin)

# Metni array'e çevirir
metin_array_yap = np.array(sayi_metin)
# Metini 3x3 matris haline getir
matris_metin = metin_array_yap.reshape(3, 3)

# Metinin transpozunu al
matris_metin_transpoz = matris_metin.transpose()
print("\ntranspozu alınan metin:\n", matris_metin_transpoz)

# anahtar tanımlanır + 3x3 Matris haline getir.
anahtar = np.array([1, 1, 0, 1, 0, 3, 0, 2, 0])  # anahtarı random üretmek için --> np.random.randint(1, 10, size=9)
anahtar_matris = anahtar.reshape(3, 3)
print("\nAnahtar matris:\n")

# Anahtar ile Metin matris çarpımı
anahtar_metin_carpimi = np.dot(anahtar_matris, matris_metin_transpoz)
print("\nMatris çarpımı:\n", anahtar_metin_carpimi)

# Çarpılan Matrisin modu
sifreli_metin_matrix = np.mod(anahtar_metin_carpimi, 29)
print("\nMatris modu:\n", sifreli_metin_matrix)

# Şireli matrisin transpozu al
sifreli_metin_transpozu = sifreli_metin_matrix.transpose()
print("\nsifreli metin transpozu:\n", sifreli_metin_transpozu)

# matrisi düz listeye çevir
sifreli_metin_duz_dizi = sifreli_metin_transpozu.flatten()

# matris içerisindeki sayıları harfe çevir
sifreli_metin = smc(sifreli_metin_duz_dizi)

sifreli_tam_kelime = ""
for harfler in sifreli_metin:
    sifreli_tam_kelime += harfler



# matrisin determinantı al
det = int(round(np.linalg.det(anahtar_matris)))
print("\nAnahtar matrisin determinantı:\n", det)

# Determinantı hesapla ve modunu al
mod_det = det % 29

# Determinantın modüler tersini de hesapla
det_tersi = pow(mod_det, -1, 29)
print("\nDeterminantın tersi (mod 29):\n", det_tersi)

# Anahtar matrisin minör ve kofaktörünü al
cofactor_matrix = [[Matrix(anahtar_matris).cofactor(i, j) for j in range(len(Matrix(anahtar_matris).row(0)))] for i in range(len(Matrix(anahtar_matris).col(0)))]

# kofaktör matrisi değişkene atar
kofaktor_dizi = [row for row in cofactor_matrix]
print("\ncofactor matrix: \n", kofaktor_dizi)

# kofaktörü array'e çevirmeye yarar
kofaktor_array = np.array(kofaktor_dizi)
Matris_kofaktor = kofaktor_array.reshape(3, 3)
print("\ncofactor matrix 3x3 formu:\n", Matris_kofaktor)

Matris_kofaktor_Transpoz = Matris_kofaktor.transpose()
print("\ncofactor matrix 3x3 formu ama transpozu alınmış:\n", Matris_kofaktor_Transpoz)

# derterminantın tersi ile transpoz çarp
det_ters_carpim_transpoz = Matris_kofaktor_Transpoz * det_tersi
print("\nDeterminantın tersinin çarpımı :\n", det_ters_carpim_transpoz)

# derterminantın tersi ile transpoz çarpımının modu
mod_carpim = np.mod(det_ters_carpim_transpoz, 29)
print("\nMatris modu:\n", mod_carpim)

# Matris tersi ile şifreli metinin çarp
matris_tersi_carpi_sifreli_metin = np.dot(mod_carpim, sifreli_metin_matrix)
print("\nAnahtar matris ile şifreli metin çarpımı:\n", matris_tersi_carpi_sifreli_metin)

# Matris tersi ile şifreli metinin çarpımının modu
carpim_mod = np.mod(matris_tersi_carpi_sifreli_metin, 29)
print("\nAnahtar matris ile şifreli metin çarpımının modu:\n", carpim_mod)

# modu alınan matrisin transpozu
modun_transpozu = carpim_mod.transpose()
print("\nModun transpozu:\n", matris_tersi_carpi_sifreli_metin)

# matris çarpımını düz yap
duz_yap = modun_transpozu.flatten()

# sayıyı metine çevir
yazi_haline_Getir = smc(duz_yap)

tam_kelime = ""
for harf in yazi_haline_Getir:
    tam_kelime += harf

BOLD = "\033[1m"
yazdir1 = PrettyTable()
yazdir1.field_names = ["\033[97mŞifrelenicek metin", "\033[97mŞifrelenmiş metin", "\033[97mDeşifre edilmiş metin"]
yazdir1.add_row([BOLD + f"\033[94m{metin}\033[0m", BOLD + f"\033[93m{sifreli_tam_kelime}\033[0m", BOLD + f"\033[94m{metin}\033[0m"])
print("\n", yazdir1, "\n")

yazdir2 = PrettyTable()
yazdir2.field_names = ["\033[97mMetinin sayısal hali", "\033[97mMetinin Şifreli sayısal hali"]
yazdir2.add_row([BOLD + f"\033[94m{sayi_metin}\033[0m", BOLD + f"\033[93m{sifreli_metin_duz_dizi}\033[0m"])
print(yazdir2)
