from FitnessApp.Training import Training


class WeightLifting(Training):

    def __init__(self, reps, sets, name):
        super().__init__(name)
        self.reps = reps
        self.sets = sets

    def addExercise(self):
        pass

    def removeExercise(self):
        pass

    def createExercise(self):
        pass