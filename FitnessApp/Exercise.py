
class Exercise:
    def __init__(self, name, exercise_type, sets, reps, time, distance, has_equipment=False):
        self.name = name
        self.has_equipment = has_equipment
        self.exercise_type = exercise_type
        self.sets = sets
        self.reps = reps
        self.time = time
        self.distance = distance
