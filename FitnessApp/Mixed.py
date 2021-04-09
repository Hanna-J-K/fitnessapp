from FitnessApp.Training import Training


class Mixed(Training):
    def __init__(self, reps, sets, time, distance):
        self.reps = reps
        self.sets = sets
        self.time = time
        self.distance = distance

    def addExercise(self):
        pass

    def removeExercise(self):
        pass

    def createExercise(self):
        pass
