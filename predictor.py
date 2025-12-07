import joblib
import numpy as np

class ConcreteStrengthPredictor:

    def __init__(self, model_path='concrete_rf.pkl', fixed_age=28.0):
        self.fixed_age = fixed_age
        self.model = joblib.load(model_path)

    def predict(self, cement, blastFurnaceSlag, flyAsh, water,
                superplasticizer, coarseAggregate, fineAggregate):
        x = np.array([
            cement, blastFurnaceSlag, flyAsh, water, superplasticizer,
            coarseAggregate, fineAggregate, self.fixed_age
        ]).reshape(1, -1)
        return float(self.model.predict(x)[0])
