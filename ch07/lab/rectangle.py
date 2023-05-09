class Rectangle:
    def __init__(self, x, y, h, w):
        self.x = abs(x)
        self.y = abs(y)
        self.height = abs(h)
        self.width = abs(w)
        
    def __str__(self):
        return "(x={}, y={}) and height={}, width={}".format(self.x, self.y, self.height, self.width)
  