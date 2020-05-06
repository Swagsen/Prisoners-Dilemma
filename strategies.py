import numpy
import random

# '0' is cooperate, '1' is defect

class Strategy:

    #constructor
    def __init__(self, size, strategy):
        self.size = size
        self.strategy = strategy
        self.fitness = numpy.zeros(self.size)
        self.fitness_sum = 0
        self.history = ''
        self.opponentHistory = ''

    #select the strategy
    def Selection(self):
        if self.strategy == 'Defect':
            return self.AlwaysDefect()            
        elif self.strategy == 'Cooperate':
            return self.AlwaysCooperate()
        elif self.strategy == 'Switch':
            return self.Switching()
        elif self.strategy == 'Random':
            return self.Random()
        elif self.strategy == 'Nice':
            return self.Nice()
        elif self.strategy == 'Forgive':
            return self.Forgiving()
        elif self.strategy == "Pavlov":
            return self.Pavlov()
        
    #always defect
    def AlwaysDefect(self):
        return '1'

    #always cooperate
    def AlwaysCooperate(self):
        return '0'

    #cooperate -> defect -> cooperate -> defect
    def Switching(self):
        if len(self.history) == 0:
            return '0'
        if len(self.history) % 2 == 0:
            return '0'
        else:
            return '1'

    #action is random 
    def Random(self):
        return str(Random.randint(0,1))

    #cooperate as long as the opponent does so
    def Nice(self):
        if len(self.history) == 0:
            return '0'
        if '1' in self.opponentHistory:
            return '1'
        else:
            return '0'

    #do as the opponent did last time
    def Forgiving(self):
        if len(self.history) == 0:
            return '0'
        else:
            return self.opponentHistory[-1]

    #if players did the same action cooperate, else defect
    def Pavlov(self):
        if len(self.history) == 0:
            return '0'
        elif self.opponentHistory[-1] == self.history[-1]:
            return '0'
        else:
            return '1'
            
    #clean fitness(?)
    def CleanFitness(self):
        self.history = []
        self.opponentHistory = []
        self.fitness = numpy.zeros(self.size)
        self.fitness_sum = 0

strategy = Strategy(2, "Pavlov")
print(strategy.strategy + ":  " + strategy.Selection())
print(strategy.strategy + ":  " + strategy.Selection())
print(strategy.strategy + ":  " + strategy.Selection())