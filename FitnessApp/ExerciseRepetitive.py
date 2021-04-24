from FitnessApp.Exercise import Exercise


class ExerciseRepetitive(Exercise):
    def __init__(self, name, exercise_type, sets, reps, time, distance):
        super().__init__(name, exercise_type, sets, reps, time, distance)

    def print_information(self):
        print("Exercise name: " + self.name)
        print("Type: " + self.exercise_type)
        print("Sets: " + str(self.sets))
        print("Reps: " + str(self.reps))

