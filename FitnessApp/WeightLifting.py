from FitnessApp.ExerciseRepetitive import ExerciseRepetitive
from FitnessApp.Training import Training


class WeightLifting(Training):

    def __init__(self, name, exercise_list):
        super().__init__(name, exercise_list)

    def remove_exercise(self, index_of_exercise):
        del self.exercise_list[index_of_exercise]

    def add_exercise(self, exercise):
        self.exercise_list.append(exercise)

    def create_exercise(self, exercise_name, exercise_type, sets, reps):
        exercise = ExerciseRepetitive(exercise_name, exercise_type, sets, reps, 0, 0)
        self.add_exercise(exercise)
