from FitnessApp.Exercise import Exercise


class ExerciseTimed(Exercise):
    def __init__(self, name, exercise_type, sets, reps, time, distance):
        super().__init__(name, exercise_type, sets, reps, time, distance)

    def print_information(self):
        print("Exercise name: " + self.name)
        print("Type: " + self.exercise_type)
        print("Time: " + str(self.time))
        print("Distance: " + str(self.distance))

