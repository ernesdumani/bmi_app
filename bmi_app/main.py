from adult import Adult
from child import Child

class BMIApp:
    def init(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def collect_user_data(self):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        weight = float(input("Enter weight (kg): "))
        height = float(input("Enter height (m): "))

        if age >= 18:
            return Adult(name, age, weight, height)
        else:
            return Child(name, age, weight, height)

    def print_results(self):
        print("\n=== Results ===")
        for person in self.people:
            person.print_info()

    def run(self):
        while True:
            person = self.collect_user_data()
            self.add_person(person)

            cont = input("Add another person? (y/n): ").lower()
            if cont != "y":
                break

        self.print_results()


if name == "main":
    app = BMIApp()
    app.run()