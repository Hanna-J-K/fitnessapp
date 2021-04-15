from abc import ABC, abstractmethod


class Training(ABC):

    def __init__(self, name):
        self.name = name
        super().__init__()

    @abstractmethod
    def addExercise(self):
        pass

    @abstractmethod
    def removeExercise(self):
        pass

    @abstractmethod
    def createExercise(self):
        pass

