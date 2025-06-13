class Coordinate(object):
    """
    A point in 2D space
    """
    #To initialize
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #To print
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"
    
    def distance(self, other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return(x_diff_sq + y_diff_sq)**0.5
    
c = Coordinate(3,4)
zero = Coordinate(0,0)
print(c.distance(zero))
print(Coordinate.distance(c, zero))
print(c)

class Fractions(object):
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    
    def __add__(self, other):
        result = Fractions(0,0)
        result.num = self.num * other.den + self.den * other.num
        result.den = self.den * other.den

        minimum = min(result.num, result.den)
        x = 2
        while x <= minimum**0.5:
            while result.num % x == 0 and result.den % x == 0:
                result.num = int(result.num/x)
                result.den = int(result.den/x)
            
            minimum = min(result.num, result.den)
            x = x + 1

        return result
    
    def __subtract__(self, other):
        result = Fractions(0,0)
        result.num = self.num * other.den - self.den * other.num
        result.den = self.den * other.den

        minimum = max(result.num, result.den)
        x = 2
        while x <= minimum:
            while result.num % x == 0 and result.den % x == 0:
                result.num = int(result.num/x)
                result.den = int(result.den/x)
      
            x = x + 1

        return result
    
    def __sub__(self, other):
        result = Fractions(0,0)
        result.num = self.num * other.den - self.den * other.num
        result.den = self.den * other.den

        minimum = max(result.num, result.den)
        x = 2
        while x <= minimum:
            while result.num % x == 0 and result.den % x == 0:
                result.num = int(result.num/x)
                result.den = int(result.den/x)
        
            x = x + 1

        return result
    
    def __mul__(self,other):
        result = Fractions(0,0)
        result.num = self.num * other.num
        result.den = self.den * other.den

        minimum = max(result.num, result.den)
        x = 2
        while x <= minimum:
            while result.num % x == 0 and result.den % x == 0:
                result.num = int(result.num/x)
                result.den = int(result.den/x)
            
            x = x + 1

        return result
    
    def __truediv__(self,other):
        result = Fractions(0,0)
        result.num = self.num * other.den
        result.den = self.den * other.num

        minimum = max(result.num, result.den)
        x = 2
        while x <= minimum:
            while result.num % x == 0 and result.den % x == 0:
                result.num = int(result.num/x)
                result.den = int(result.den/x)
            x = x + 1

        return result
    
    def __float__(self):
        return self.num/self.den
    
    def inverse(self):
        return Fractions(self.den, self.num)
    
a = Fractions(1,3)
b = Fractions(1,6)
print(b - a)
print(a/b + b/a)

print(a/b + Fractions.inverse(a/b))

def Polynomial(object):
    pass