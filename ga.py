from population import Population

target = 185
coefs = [5, 2, 1, 3]
popmax = 100
mutation_rate = 0.01

population = Population(mutation_rate, target, coefs, popmax)

while True:
    population.natural_selection()
    population.generate()
    population.calc_fitness()
    if population.is_finished():
        print("Finish:", population.get_best().values)
        break
    print(population.get_best().fitnesss)
