from person import Person

class Adult(Person):
    def calculate_bmi(self):
        return self.weight / (self.height ** 2)w