from FitnessApp.Training import Training


class WeightLifting(Training):

    def __init__(self, reps, sets, name):
        super().__init__(name)
        self.reps = reps
        self.sets = sets

    def add_exercise(self):
        pass

    def remove_exercise(self):
        pass

    def create_exercise(self):
        pass
