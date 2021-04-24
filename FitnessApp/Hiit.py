from FitnessApp.Cardio import Cardio


class Hiit(Cardio):
    def __init__(self, time, sets, distance=0):
        super().__init__(time, sets, distance)
