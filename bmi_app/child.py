from person import Person

class Child(Person):
    def calculate_bmi(self):
        return (self.weight / (self.height ** 2)) *1.3