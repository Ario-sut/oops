class OpAritmatika:

    #-- deklrasi properti
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def bilangan1(self):
        return self.x
    
    def bilangan2(self):
        return self.y
    
    def tambah(self):
        return self.x + self.y

    def kurang(self):
        return self.x - self.y

    def kali(self):
        return self.x * self.y

    def bagi(self):
        return self.x / self.y
    
    def sisa(self):
        return self.x % self.y
    
    def pangkat(self):
        return self.x ** self.y
    
#-- program utama & pemnggilan
op = OpAritmatika(6,5)
bil1 = op.bilangan1()
bil2 = op.bilangan2()

opTambah = op.tambah()
opKurang = op.kurang()
opKali= op.kali()
opBagi = op.bagi()
opSisa = op.sisa()

print('-- Operasi Aritmatika Sederhana --')
print(' ..Dengan OOP Bahasa Python..')
print('='*34)
print('Bilangan Ke-1(x)          = ', bil1)
print('Bilangan Ke-2(y)          = ', bil2)
print('Penjumlahan 2 Bilangan    = ', opTambah)
print('Pengurangan 2 Bilangan    = ', opKurang)
print('Perkalian 2 Bilangan      = ', opKali)
print('Pembagian 2 Bilangan      = ', opBagi)
print('Sisa Pembagian 2 Bilangan = ', opSisa)
print('='*34)