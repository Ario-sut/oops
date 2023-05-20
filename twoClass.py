class polygon:
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        perimeter = sum(self.sides)
        return perimeter
    
class quadrilateral(polygon):
    def info(self):
        print('This is Quadrilateral')

class pentagon(polygon):
    def info(self):
        print('This is Pentagon')

Quadobj = quadrilateral([3,6,7,9])
peri = Quadobj.perimeter()
print('The perimeter is',peri)

Pentaobj = pentagon([3,5,7,8,9])
peri = Pentaobj.perimeter()
print('The perimeter is',peri)
