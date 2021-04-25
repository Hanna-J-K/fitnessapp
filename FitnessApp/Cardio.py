from FitnessApp.ExerciseTimed import ExerciseTimed
from FitnessApp.Training import Training


class Cardio(Training):

    def __init__(self, name, exercise_list):
        super().__init__(name, exercise_list)

    def remove_exercise(self, exercise_name):
        self.exercise_list.remove(exercise_name)

    def add_exercise(self, exercise_name):
        self.exercise_list.append(exercise_name)

    def create_exercise(self, exercise_name, exercise_type, sets, time, distance):
        exercise = None
        if exercise_type == "hiit":
            exercise = ExerciseTimed(exercise_name, exercise_type, sets, 0, time, 0)
        elif exercise_type == "cardio":
            exercise = ExerciseTimed(exercise_name, exercise_type, 0, 0, time, distance)
        self.add_exercise(exercise)
