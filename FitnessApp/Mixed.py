from FitnessApp.Training import Training


class Mixed(Training):
    def __init__(self, reps, sets, time, distance, name):
        super().__init__(name)
        self.reps = reps
        self.sets = sets
        self.time = time
        self.distance = distance

    def add_exercise(self):
        pass

    def removeExercise(self):
        pass

    def createExercise(self):
        pass
