from FitnessApp.Training import Training


class Cardio(Training):

    def __init__(self, time, distance, name):
        super().__init__(name, exercise_list=0)
        self.time = time
        self.distance = distance

    def remove_exercise(self):
        pass

    def create_exercise(self):
        pass
