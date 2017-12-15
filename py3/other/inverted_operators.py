class oo()
def __add__(self, other):
  if isinstance(other, Point2D):
    return Point2D(self.x + other.x, self.y + other.y)
  else:
    return Point2D(self.x + float(other), self.y +

def __radd__(self, other):
  if isinstance(other, Point2D):
    return Point2D(self.x + other.x, self.y + other.y)
  else:
    return Point2D(self.x + float(other), self.y +

