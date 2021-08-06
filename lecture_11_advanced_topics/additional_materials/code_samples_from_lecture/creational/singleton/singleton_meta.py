class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonClass(metaclass=Singleton):
    pass


class NonSingletonClass:
    pass

if __name__ == "__main__":
    sc_1 = SingletonClass()
    sc_2 = SingletonClass()

    res = sc_1 == sc_2
    print("sc_1 == sc_2 is {}".format(res))
    
    non_sc_1 = NonSingletonClass()
    non_sc_2 = NonSingletonClass()

    res = non_sc_1 == non_sc_2
    print("non_sc_1 == non_sc_2 is {}".format(res))

    
