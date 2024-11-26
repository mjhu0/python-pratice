class ApproximateRoot:
    def __init__(self, func, precision=1e-6, max_iterations=1000):
        self.func = func
        self.precision = precision
        self.max_iterations = max_iterations

    def bisection_method(self, a, b):
        if self.func(a) * self.func(b) >= 0:
            print("区间端点未包含根")
            return None

        iterations = 0
        while (b - a) / 2 > self.precision and iterations < self.max_iterations:
            midpoint = (a + b) / 2
            if self.func(midpoint) == 0:
                return midpoint  # 精确根
            elif self.func(a) * self.func(midpoint) < 0:
                b = midpoint
            else:
                a = midpoint
            iterations += 1

        return (a + b) / 2

# 定义函数 f(x) = x^3 + 3x^2 + x + 1
def func(x):
    return x**3 + 3*x**2 + x + 1
# 使用 ApproximateRoot 类进行计算
approximate_root_finder = ApproximateRoot(func)
root = approximate_root_finder.bisection_method(-4, -1)  
print("近似根:", root)
######### 542313460109 胡华吉  ###############