def singleton(cls):
    instances = {}
    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance

@singleton
class SingletonClass:
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

    
