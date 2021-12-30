class Rectangle:
  def __init__(self,width,height):
    self.width = width
    self.height = height
  
  def __str__(self):
    return "Rectangle(width={0}, height={1})".format(self.width,self.height)

  def set_width(self,width):
    self.width = width

  def set_height(self,height):
    self.height = height

  def get_area(self):
    return (self.width * self.height)  

  def get_perimeter(self):
    return ((2*self.width)+(2*self.height))
  
  def get_diagonal(self):
    return (((self.width**2)+(self.height**2)) ** .5)
  
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    pic = ''
    for i in range(self.height):
      pic += '*' * self.width
      pic += '\n'
    return pic
  
  def get_amount_inside(self,obj):
    currArea = self.width * self.height
    objArea = obj.width * obj.height
    return (currArea//objArea)

class Square(Rectangle):
  def __init__(self,side):
    self.side = side
    super().__init__(side,side)

  def set_side(self,side):
    self.side = side
    super().set_width(side)
    super().set_height(side)

  def __str__(self):
    return "Square(side={0})".format(self.width)

  
