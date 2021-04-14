from FitnessApp.BodyWeight import BodyWeight


class Calisthenics(BodyWeight):
    pass

    def encode_calisthenics(self):
        return {'sets': self.sets, 'reps': self.reps}
