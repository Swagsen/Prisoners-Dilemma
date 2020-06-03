from population import Population


numberOfGeneration = 50
populationSize = 20
matchTimes = 40

crossoverPropability = .5
mutationPropability = .05

strategyList = ['Defect', 'Cooperate', 'Switch', 'Random', 'Nice', 'Forgive', 'Pavlov']


def OneStrategy(strategy):
        population = Population(populationSize, matchTimes, crossoverPropability, mutationPropability)

        for x in range(numberOfGeneration):
            population.Generation(strategy)

        #print('best chromosome: ', population.bestChromosome)
        print('strategy: ', strategy, ' Years in prison: ', population.bestFitness,' opponent:', population.opponentFitness)

def AllStrategies():
    for strategy in strategyList:
        OneStrategy(strategy)



if __name__ == '__main__':
    AllStrategies()

    # for i in range(40):
    #     OneStrategy(strategyList[6])
