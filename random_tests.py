import pickle

class Person:
    def __init__(self, age, weight, height) -> None:
        self.age = age
        self.weight = weight
        self.height = height

    def describe_self(self):
        print(f"The person is about {self.age} years old, weighing about {self.weight}"
            f"and was about {self.height} feet tall.")

# Deontay = Person(34, 150, 9)


# with open('person_data.pickle', 'wb') as file:
#     pickle.dump(Deontay, file)


with open('person_data.pickle', 'rb') as file:
    loaded_person = pickle.load(file)

loaded_person.describe_self()