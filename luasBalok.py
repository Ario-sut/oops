class luasPersegi:
    def __init__(self,panjang,lebar):
        self.panjang=10
        self.lebar=5

Balok=luasPersegi(10,5)

print('-- Mencari Luas Balok --')
print('Panjang Balok :',Balok.panjang)
print('Lebar Balok   :',Balok.lebar)
print('Luas Balok    :',Balok.panjang*Balok.lebar)
print()
class luasLingkaran:
    def __init__(self,radius):
        self.radius=7

Luas = luasLingkaran(7)
print('-- Mencari Luas Lingkaran --')
print('Luas Lingkaran :',Luas.radius*22/7)
