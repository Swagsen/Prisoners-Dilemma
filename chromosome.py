import random
from strategies import Strategy

#chromosome class contains genes, history and the fitness
class Chromosome:
    def __init__(self):
        self.genes = "{0:064b}".format(random.randint(0, 2**64-1))
        self.history = "{0:06b}".format(0, 2**6-1)
        #self.history = "{0:06b}".format(0)
        self.fitness = 0
        self.opponentFitness = 0

    def Result(self, myChoice, opponentChoice):
        if myChoice == '0' and opponentChoice == '0':
            return 1
        elif myChoice == '0' and opponentChoice == '1':
            return 3
        elif myChoice == '1' and opponentChoice == '0':
            return 0
        elif myChoice == '1' and opponentChoice == '1':
            return 2
        return 420

    def Match(self, opponentChoice):
        selection = self.genes[int(self.history, 2)]
        self.fitness += self.Result(selection, opponentChoice)
        self.opponentFitness += self.Result(opponentChoice, selection)
        self.history = self.history[2::] + selection + opponentChoice
        return selection + opponentChoice
    
    def CleanFitness(self):
        self.fitness = 0
        self.opponentFitness = 0