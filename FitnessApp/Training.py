from abc import ABC, abstractmethod


class Training(ABC):

    def __init__(self, name, exercise_list):
        self.name = name
        self.exercise_list = exercise_list
        super().__init__()

    @abstractmethod
    def remove_exercise(self, exercise_name):
        pass

    @abstractmethod
    def add_exercise(self, exercise):
        pass

    @abstractmethod
    def create_exercise(self):
        pass

