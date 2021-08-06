import abc


class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def say(self):
        pass


class Dog(Animal):
    def say(self):
        print(f"{self.__class__.__name__} say Woof!")

class Cat(Animal):
    def say(self):
        print(f"{self.__class__.__name__} say Meow!")

class Fish(Animal):
    pass

if __name__ == "__main__":
    Dog().say()
    Cat().say()
    Fish().say()