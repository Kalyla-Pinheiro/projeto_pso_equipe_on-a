import numpy as np
from src.predictor import ConcreteStrengthPredictor
from src.constraints import penalty

class ObjectiveFunction:

    def __init__(self, model_path='concrete_rf.pkl'):
        self.predictor = ConcreteStrengthPredictor(model_path=model_path)

    def evaluate(self, x: np.ndarray) -> float:
        resistance = self.predictor.predict(*x)
        return resistance - penalty(x)
