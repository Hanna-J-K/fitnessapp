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

    def remove_exercise(self):
        pass

    def create_exercise(self):
        pass
