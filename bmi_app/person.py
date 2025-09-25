class Person:
    def __init__(selfself, name, age, weight, height):
        self.name = name
        self.age = age
        self._weight = weight
        self._height = height

    @property def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self._weight = value
        else:
            raise ValueError("weight must be positive")

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise ValueError("height must be positive")
        def calculate_bmi(self):
            raise NotImplementedError("Subclass must implement calculate_bmi")

        def get_bmi_category(self, bmi):
            if bmi < 18.5:
                return "Underweight"
            elif 18.5 <= bmi <= 24.9:
                return "healthy weight"
            elif 25 <= bmi <= 29.9:
                return "obese weight"
            else:
                return "obesity"

        def print_info(self):
            bmi =self.calculate_bmi()
            category = self.get_bmi_category(bmi)
            print(f"Name: {self.name}, Age: {self.age}, BMI: {bmi:,2f}, Category: {category}")
