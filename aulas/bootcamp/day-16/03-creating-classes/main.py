class Dog:
    species = "Canis Familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

    def __str__(self):
        return f"my name is: {self.name}, hello! :)"

dog_a = Dog("Totó", 5)

print(dog_a.name)
print(dog_a.species)
print(dog_a.description())
print(dog_a.speak("au au"))
print(dog_a)


#Herança

class JackRussellTerrier(Dog):
    pass


miles = JackRussellTerrier("Miles", 4)

# Extends Funcionality of a Parent

class Bulldog(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)


matias = Bulldog('Matias', 6)

print(matias.speak())



