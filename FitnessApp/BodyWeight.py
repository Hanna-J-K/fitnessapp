from FitnessApp.ExerciseRepetitive import ExerciseRepetitive
from FitnessApp.Training import Training


class BodyWeight(Training):

    def __init__(self, name, exercise_list):
        super().__init__(name, exercise_list)

    def remove_exercise(self, index_of_exercise):
        del self.exercise_list[index_of_exercise]

    def add_exercise(self, exercise):
        self.exercise_list.append(exercise)

    def create_exercise(self, exercise_name, exercise_type, sets, reps, time):
        exercise = None
        if exercise_type == "bw":
            exercise = ExerciseRepetitive(exercise_name, exercise_type, sets, reps, 0, 0)
        elif exercise_type == "yoga":
            exercise = ExerciseRepetitive(exercise_name, exercise_type, 0, 0, time, 0)
        self.add_exercise(exercise)


