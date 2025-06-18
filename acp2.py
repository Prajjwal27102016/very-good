class Triangle(object):
    def __init__(self, l ,w):
        self.width = w
        self.length = l
    def triangle_area(self):
        return (self.length * self.width)
newTriangle = Triangle(12, 10)
print("dimesions of triangle- length: %d, width: %d" % (newTriangle.length, newTriangle.width))
print("area of triangle is: %d" % (newTriangle.triangle_area()))
    
 