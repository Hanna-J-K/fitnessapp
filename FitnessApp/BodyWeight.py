from FitnessApp.Training import Training


class BodyWeight(Training):

    def __init__(self, name, exercise_list):
        super().__init__(name, exercise_list)

    def remove_exercise(self, exercise_name):
        self.exercise_list.remove(exercise_name)

    def create_exercise(self, exercise_name):
        pass


