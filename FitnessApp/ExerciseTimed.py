from FitnessApp.Exercise import Exercise


class ExerciseTimed(Exercise):
    def __init__(self, name, exercise_type, sets, reps, time, distance):
        super().__init__(name, exercise_type, sets, reps, time, distance)
        self.sets = 0
        self.reps = 0

