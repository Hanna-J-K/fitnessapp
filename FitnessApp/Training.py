from abc import ABC, abstractmethod


class Training(ABC):

    def __init__(self, name):
        self.name = name
        super().__init__()

    @abstractmethod
    def add_exercise(self):
        pass

    @abstractmethod
    def remove_exercise(self):
        pass

    @abstractmethod
    def create_exercise(self):
        pass

