#bangun datar
import bangun_datar_modul

from bangun_datar_modul import luas_lingkaran

jari_jari = 6
luas= luas_lingkaran(jari_jari)
print(f"luas lingkaran dengan jari-jari {jari_jari} adalah {luas}")

from bangun_datar_modul import luas_persegi
sisi=5
luas= sisi*sisi
print(f"luas persegi adalah {luas}")

from bangun_datar_modul import luas_persegi_panjang
panjang = 5
lebar = 3
luas= panjang*lebar
print(f"luas dari persegi panjang adalah {luas}")

from bangun_datar_modul import luas_segitiga
alas=6
tinggi=3
luas= 1/2 * alas * tinggi
print(f"luas segitiga adalah {luas}")

from bangun_datar_modul import luas_jajargenjang
alas=4
tinggi=8
luas= alas * tinggi
print(f"luas dari jajargenjang adalah {luas}")

#operator
import operator_modul

from operator_modul import tambah
tambah(5,3)
from operator_modul import kurang
kurang(7,2)
from operator_modul import kali
kali(6,6)
from operator_modul import bagi
bagi(8,2)
from operator_modul import pangkat
pangkat(5,2)

#bangun ruang 
import bangun_ruang_modul

from bangun_ruang_modul import luas_kubus
sisi=2
luas= 6 * sisi * sisi
print(f"luas kubus adalah {luas}")

from bangun_ruang_modul import luas_balok
p=2
l=3
t=3
luas= 2 *p*l + 2*p*t + 2*l*t
print(f"luas balok adalah {luas}")

from bangun_ruang_modul import luas_tabung
phi=3.14
r=5
t=6
luas= 2 *phi *r *(r+t)
print(f"luas tabung adalah {luas}")

from bangun_ruang_modul import luas_limas
luas_alas=5
luas_sisi_tegak=10
luas= luas_alas + luas_sisi_tegak
print(f"luas limas adalah {luas}")

from bangun_ruang_modul import luas_prisma
luas_alas=5
keliling=8
tinggi=10
luas= (2* luas_alas) + (keliling*tinggi)
print(f"luas prisma adalah {luas}")