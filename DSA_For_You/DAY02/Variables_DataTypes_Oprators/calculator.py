class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    
    def sub(self):
        if self.a > self.b:
            return self.a - self.b
        elif self.b > self.a:
            return self.b - self.a
        else:
            return 0
        
    def mul(self):
        return self.a * self.b
    
    def div(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Division by zero error!"
        
calc = Calculator(5, 10)

addition = calc.add()
subtraction = calc.sub()
multiplication = calc.mul()
division = calc.div()

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
