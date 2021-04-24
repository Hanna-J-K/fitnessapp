from FitnessApp.BodyWeight import BodyWeight


class Calisthenics(BodyWeight):
    pass

    def print_reps_and_sets(self):
        print(self.reps)
        print(self.sets)

    def encode_calisthenics(self):
        return {'sets': self.sets, 'reps': self.reps}
