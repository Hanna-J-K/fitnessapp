from FitnessApp.Training import Training


class Cardio(Training):

    def __init__(self, time, distance, name):
        super().__init__(name)
        self.time = time
        self.distance = distance

    def add_exercise(self):
        pass

    def removeExercise(self):
        pass

    def createExercise(self):
        pass
