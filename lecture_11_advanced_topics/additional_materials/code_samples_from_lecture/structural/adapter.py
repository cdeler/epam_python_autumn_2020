from typing import Callable, TypeVar


T = TypeVar("T")


class Dog:
    def __init__(self):
        self.name = "dog"

    def woof(self) -> None:
        print("Dog say Woof!")

class Cat:
    def __init__(self):
        self.name = "cat"
    
    def meow(self) -> None:
        print("Cat say Meow!")

class UnknownAlienComputer:
    def __init__(self):
        self.name = "aaaalieeen"

    def undefined(self) -> None:
        print("na!lv... Bleep Bloop Bleep Bloop ...o0o0o0")


class Adapter:
    def __init__(self, obj: T, **adapted_methods: Callable):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)

    def original_dict(self):
        return self.obj.__dict__

if __name__ == "__main__":
    dog = Dog()
    print(dog.__dict__)
    
    dog = Adapter(dog, say=dog.woof)
    print(dog.__dict__)

    cat = Cat()
    cat = Adapter(cat, say=cat.meow)

    alien = UnknownAlienComputer()
    alien = Adapter(alien, say=alien.undefined)

    print(alien.__dict__)

    for item in (dog, cat, alien):
        item.say()