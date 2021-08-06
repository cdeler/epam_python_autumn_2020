class SingletonBorg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class SingletonClass(SingletonBorg):
    def __init__(self, state=None):
        super().__init__()
        if state:
            self.state = state
        else:
            if not hasattr(self, "state"):
                self.state = "Init"

    def __str__(self):
        return self.state


if __name__ == "__main__":
    sc_1 = SingletonClass()
    sc_2 = SingletonClass()

    print(sc_1)

    sc_1.state = "I'm for SC1"
    sc_2.state = "I'm for SC2"

    print("sc_1", "ID:", id(sc_1), "State:", sc_1.state)
    print("sc_2", "ID:", id(sc_2), "State:", sc_2.state)
    print(sc_1.state==sc_2.state)

