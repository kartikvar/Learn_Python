from OOPS.Learning_Inheritence.Animal import Animal


class Dog(Animal):
    animal_type = "Dog"

    def sound(self):
        super().sound()
        print("This is sound of Dog")


dog = Dog()
print(dog.animal_type)
dog.sound()
dog.class_type()
