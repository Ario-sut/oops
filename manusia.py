class person:
    def __init__(self, name, age, hobby, residence):
        self.name = name
        self.age = age
        self.hobby = hobby
        self.residence = residence

p1= person('Halip', 22,'Teaching', 'Makassar')
p2 = person('Fitraka', 19, 'Shogi', 'Bandung')

print('='*38)
print('Nama orang pertama        = ',p1.name)
print('Umur orang pertama        = ',p1.age)
print('Hobi orang pertama        = ',p1.hobby)
print('Asal orang pertama        = ',p1.residence)
print('='*38)
print('Nama orang Kedua          = ',p2.name)
print('Umur orang Kedua          = ',p2.age)
print('Hobi orang Kedua          = ',p2.hobby)
print('Asal orang Kedua          = ',p2.residence)
print('='*38)



