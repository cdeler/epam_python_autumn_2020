import weakref


class Dog:
    _pool = weakref.WeakValueDictionary()

    def __new__(cls, breed, name):
        obj_key = f"{breed}_{name}"
        obj = cls._pool.get(obj_key)
        if obj is None:
            obj = object.__new__(Dog)
            cls._pool[obj_key] = obj
            obj.breed, obj.name = breed, name
        return obj

    def __repr__(self):
        return f"<{self.breed.capitalize()} : {self.name.capitalize()}>"


if __name__ == "__main__":
    alex_1 = Dog("Shepherd", "Alex")
    alex_2 = Dog("Shepherd", "Alex")
    print(alex_1, alex_2, "alex_1 == alex_2", alex_1 == alex_2)

    alex_1.say = "woof"
    alex_3 = Dog("Shepherd", "Alex")

    print("alex_1 say:", alex_1.say)
    print("alex_3 say:", alex_3.say)
    
    Dog._pool.clear()

    alex_4 = Dog("Shepherd", "Alex")
    
    print("alex_2 say:", alex_2.say)
    print("alex_4 say:", alex_4.say)
