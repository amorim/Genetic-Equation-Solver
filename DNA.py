from random import randint, random


class DNA:


    def __init__(self, max):
        self.values = []
        self.max = 0
        self.fitnesss = 0
        self.max = max
        for i in range(4):
            self.values.append(randint(0, max))

    def fitness(self, target, coefs):
        score = 0
        for i in range(4):
            score += coefs[i] * self.values[i]
        score -= target
        if score < 0:
            score *= -1
        self.fitnesss = score

    def crossover(self, partner):
        child = DNA(self.max)
        midpoint = randint(0, len(self.values))
        for i in range(4):
            if i > midpoint:
                child.values[i] = self.values[i]
            else:
                child.values[i] = partner.values[i]
        return child

    def mutate(self, mutation_rate):
        for i in range(4):
            if random() < mutation_rate:
                self.values[i] = randint(0, self.max)
