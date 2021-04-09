from FitnessApp.Cardio import Cardio


class Hiit(Cardio):
  def __init__(self, time, sets, distance=None):
    super().__init__(time, distance=None)
    self.sets = sets
