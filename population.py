from random import randint

from DNA import DNA


def map(n, start1, stop1, start2, stop2):
    return ((n - start1) / (stop1 - start1)) * (stop2 - start2) + start2


class Population:


    def __init__(self, mutation_rate, target, coefs, num):
        self.mutation_rate = 0
        self.population = []
        self.mating_pool = []
        self.coefs = []
        self.target = 0
        self.generations = 0
        self.finished = False
        self.perfect_score = 0
        self.target = target
        self.mutation_rate = mutation_rate
        self.coefs = coefs
        for i in range(num):
            self.population.append(DNA(target))
        self.calc_fitness()

    def calc_fitness(self):
        for i in range(len(self.population)):
            self.population[i].fitness(self.target, self.coefs)

    def natural_selection(self):
         self.mating_pool = []
         max_fitness = float('inf')
         for i in range(len(self.population)):
             if self.population[i].fitnesss < max_fitness:
                 max_fitness = self.population[i].fitnesss
         for i in range(len(self.population)):
             fitness = map(self.population[i].fitnesss, 0, max_fitness + 0.01, 0, 1)
             n = 2000 - int(fitness * 100)
             for j in range(n):
                 self.mating_pool.append(self.population[i])

    def generate(self):
        for i in range(len(self.population)):
            a = randint(0, len(self.mating_pool) - 1)
            b = randint(0, len(self.mating_pool) - 1)
            partnerA = self.mating_pool[a]
            partnerB = self.mating_pool[b]
            child = partnerA.crossover(partnerB)
            child.mutate(self.mutation_rate)
            self.population[i] = child
        self.generations += 1

    def get_best(self):
        world_record = float('inf')
        index = 0
        for i in range(len(self.population)):
            if self.population[i].fitnesss < world_record:
                index = i
                world_record = self.population[i].fitnesss
        if world_record == self.perfect_score:
            self.finished = True
        return self.population[index]

    def is_finished(self):
        return self.finished

    def get_generations(self):
        return self.generations



