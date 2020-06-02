import random, copy
import numpy as np
from chromosome import Chromosome
from strategies import Strategy

class Population:
    def __init__(self, populationSize, matchTimes, crossoverPropability, mutationPropability):
        self.chromosomeList = list()

        for _ in range(populationSize):
            self.chromosomeList.append(Chromosome())

        self.geneSize = 64
        self.populationSize = populationSize
        self.nextGenChromosomeList = list()
        
        self.crossoverPropability = crossoverPropability
        self.mutationPropability = mutationPropability
        self.matchTimes = matchTimes
        
        self.bestFitness = 0
        self.opponentFitness = 0

        self.bestChromosome = ''

    def Crossover(self):
        indexList = np.arange(self.populationSize)
        np.random.shuffle(indexList)

        halfPopultaionSize = int(self.populationSize/2)
        firstIndex = indexList[0:halfPopultaionSize]
        secondIndex = indexList[halfPopultaionSize::]
        
        for i in range(halfPopultaionSize):
            if random.random() < self.crossoverPropability:
                randomIndex = random.randint(0, self.geneSize-1)

                newChromosome1 = Chromosome()
                newChromosome2 = Chromosome()
                newChromosome1.genes = self.chromosomeList[firstIndex[i]].genes[0:randomIndex] + self.chromosomeList[secondIndex[i]].genes[randomIndex::]
                newChromosome2.genes = self.chromosomeList[secondIndex[i]].genes[0:randomIndex] + self.chromosomeList[firstIndex[i]].genes[randomIndex::]

                self.nextGenChromosomeList.append(newChromosome1)
                self.nextGenChromosomeList.append(newChromosome2)

    def Mutation(self):
        for i in range(self.populationSize):
            if random.random() < self.mutationPropability:
                randomIndex = random.randint(0, self.geneSize-1)
                newGenes = ''

                #kopiowanie stringa jest uposledzone XD
                for x, gene in enumerate(self.chromosomeList[i].genes):          
                    if x == randomIndex:
                        if gene == '1':
                            newGenes = newGenes + '0'
                        else:
                            newGenes = newGenes + '1'
                    else:
                        newGenes = newGenes + gene

                newChromosome = Chromosome()
                newChromosome.genes = newGenes
                self.nextGenChromosomeList.append(newChromosome)

    def Evaluate(self, strategyType):
        self.nextGenChromosomeList += self.chromosomeList
        population = self.nextGenChromosomeList

        self.strategy = Strategy(len(population), strategyType)

        for i, chromosome in enumerate(population):
            for x in range(self.matchTimes):
                self.strategy.AddToHistory(chromosome.Match(self.strategy.Selection()))

        self.chromosomeList = copy.deepcopy(sorted(population, key=lambda x: x.fitness, reverse=False))[0:self.populationSize]

        self.bestFitness = self.chromosomeList[0].fitness
        self.opponentFitness = self.chromosomeList[0].opponentFitness
        self.bestChromosome = self.chromosomeList[0].genes
        self.nextGenChromosomeList = list()

    def Generation(self, types):
        self.Crossover()
        self.Mutation()
        self.Evaluate(types)        
        self.Clean()
    
    def Clean(self):
        self.strategy.CleanHistory()
        for chromosome in self.chromosomeList:
            chromosome.CleanFitness()
    