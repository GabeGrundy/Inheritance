class Number:
    def __init__(self,value):
        self.value = value
    def __repr__(self):
        return f'Number({self.value})' 
    def add(self,other):
        return self.value + other.value
    def sub(self,other):
        return self.value - other.value

class ComplexNumber(Number):
    def __init__(self, real, imaginary):
        super().__init__(real)
        self.imaginary = imaginary
    def __repr__(self):
        return f'ComplexNumber({self.value}, {self.imaginary})'
    def add(self,other):
        real_part = super().add(other)
        return ComplexNumber(real_part, self.imaginary + other.imaginary)
    def sub(self,other):
        real_part = super().sub(other)
        return ComplexNumber(real_part, self.imaginary - other.imaginary)

if __name__ == "__main__":
    num1 = Number(5)
    num2 = Number(3)
    print(num1)
    print(num2)
    print(num1.add(num2))
    print(num1.sub(num2))
    complex_num1 = ComplexNumber(2,4)
    complex_num2 = ComplexNumber(1,2)
    print(complex_num1)
    print(complex_num2)
    print(complex_num1.add(complex_num2))
    print(complex_num1.sub(complex_num2))

