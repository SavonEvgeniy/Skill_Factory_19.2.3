from app.calculator import Calculator

class TestCalc: 
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):   #тестируем умножение
        assert self.calc.multiply(self, 2, 2) == 4
    def test_multiply_calculate_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5
        
    def test_division_calculate_correctly(self):   #тестируем деление
        assert self.calc.division(self, 4, 2) == 2
    def test_division_calculate_failed(self):
        assert self.calc.division(self, 6, 2) == 2
        
    def test_subtraction_calculate_correctly(self):  #тестируем вычитание
        assert self.calc.subtraction(self, 4, 2) == 2
    def test_subtraction_calculate_failed(self):
        assert self.calc.subtraction(self, 6, 2) == 2
        
    def test_adding_calculate_correctly(self):   #тестируем сложение
        assert self.calc.adding(self, 4, 2) == 6
    def test_adding_calculate_failed(self):
        assert self.calc.adding(self, 6, 2) == 6
