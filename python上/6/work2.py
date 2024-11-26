import math

class SolveEquation:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def getDiscriminant(self):
        return self._b ** 2 - 4 * self._a * self._c

    def getRoot1(self):
        discriminant = self.getDiscriminant()
        if discriminant < 0:
            return None  # 无实根
        return (-self._b + math.sqrt(discriminant)) / (2 * self._a)

    def getRoot2(self):
        discriminant = self.getDiscriminant()
        if discriminant < 0:
            return None  # 无实根
        return (-self._b - math.sqrt(discriminant)) / (2 * self._a)

######### 542313460109 胡华吉  ###############
equation = SolveEquation(1, -3, 2)
print("根1:", equation.getRoot1())
print("根2:", equation.getRoot2())
