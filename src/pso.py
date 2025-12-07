import numpy as np
from src.objective import FitnessFunction

class PSO:

    def __init__(self, fitness: FitnessFunction, n_particles=30, n_iterations=50,
                 w=0.7, c1=1.5, c2=1.5):
        self.fitness = fitness
        self.n_particles = n_particles
        self.n_iterations = n_iterations
        self.w = w      
        self.c1 = c1    
        self.c2 = c2   
        self.history = []

        self.dim = 7  
        self.lb = np.array([0, 0, 0, 0, 0, 800, 600])  
        self.ub = np.array([540, 360, 200, 250, 32, 1140, 1000])  

        self._initialize()

    def _initialize(self):
        self.positions = np.random.uniform(self.lb, self.ub, (self.n_particles, self.dim))
        self.velocities = np.random.uniform(-1, 1, (self.n_particles, self.dim))
        self.best_personal = np.copy(self.positions)
        self.fitness_personal = np.array([self.fitness.evaluate(p) for p in self.positions])

        best_idx = np.argmax(self.fitness_personal)
        self.best_global = np.copy(self.positions[best_idx])
        self.fitness_global = self.fitness_personal[best_idx]

    def optimize(self):
        for _ in range(self.n_iterations):
            r1, r2 = np.random.rand(), np.random.rand()

            self.velocities = (
                self.w * self.velocities +
                self.c1 * r1 * (self.best_personal - self.positions) +
                self.c2 * r2 * (self.best_global - self.positions)
            )

            self.positions += self.velocities
            self.positions = np.clip(self.positions, self.lb, self.ub)

            current_fitness = np.array([self.fitness.evaluate(p) for p in self.positions])
            self.history.append(current_fitness.max())

            for i in range(self.n_particles):
                if current_fitness[i] > self.fitness_personal[i]:
                    self.fitness_personal[i] = current_fitness[i]
                    self.best_personal[i] = self.positions[i]

            best_idx = np.argmax(current_fitness)
            if current_fitness[best_idx] > self.fitness_global:
                self.fitness_global = current_fitness[best_idx]
                self.best_global = self.positions[best_idx]

        return self.best_global, self.fitness_global, self.history
