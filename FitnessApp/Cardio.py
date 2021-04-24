from FitnessApp.Training import Training


class Cardio(Training):

    def __init__(self, time, distance, name):
        super().__init__(name)
        self.time = time
        self.distance = distance

    def add_exercise(self):
        pass

    def remove_exercise(self):
        pass

    def create_exercise(self):
        pass
