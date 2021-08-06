
from abc import ABC, abstractmethod
from typing import Optional, Tuple, TypeVar

T = TypeVar("T")


class Handler(ABC):
    def __init__(self, next_step: Optional[T] = None):
        self.next_step = next_step

    def handle(self, request: int) -> None:
        res = self.process(request)
        if not res and self.next_step:
            self.next_step.handle(request)

    @abstractmethod
    def process(self, request: int) -> Optional[bool]:
        pass


class EvenNumberHandler(Handler):
    @staticmethod
    def process(request: int) -> Optional[bool]:
        if request % 2 == 0:
            print(f"{request} success with handler EvenNumberHandler")
            return True

class DivideByThreeHandler(Handler):
    @staticmethod
    def process(request: int) -> Optional[bool]:
        if request % 3 == 0:
            print(f"{request} success with handler DivideByThreeHandler")
            return True

class FallbackHandler(Handler):
    @staticmethod
    def process(request: int) -> Optional[bool]:
        print(f"end of chain, no handler for {request}")
        return False


if __name__ == "__main__":
    h0 = EvenNumberHandler()
    h1 = DivideByThreeHandler(FallbackHandler())
    h0.next_step = h1
    
    h0.handle(2)
    h0.handle(3)
    h0.handle(7)
    
