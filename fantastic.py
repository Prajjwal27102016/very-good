class Rectangle(object):
    def __init__(self, l,w ):
        self.width = w
        self.lenght = l
    def rectangle_area(self):
        return self.lenght*self.width

newRectangle = Rectangle(12, 10)
print("dimesions of rectangle- length: %d, width: %d" % (newRectangle.lenght, newRectangle.width))
print("area of rectangle is: %d" % (newRectangle.rectangle_area()))
