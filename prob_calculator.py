import copy
import random
from collections import Counter

# Consider using the modules imported above.

class Hat(object):
    def __init__(self, **kwargs):
        hat = []
        for key, val in kwargs.items():
            for x in range(val):
                hat.append(key)
        # print(f'hat is {hat}')
        self.contents = hat

    def draw(self, draws):
        x = len(self.contents)
        chosen = []
        if draws >= x:
            chosen = self.contents
            return chosen
        for i in range(draws):
            pick = random.randrange(0, x)
            chosen.append(self.contents[pick])
            self.contents.pop(pick)
            x -= 1
        return chosen         
    
              
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    results = []
    for i in range(num_experiments):
        pot = copy.deepcopy(hat)
        results.append(pot.draw(num_balls_drawn))
    expected_balls = dict(sorted(expected_balls.items()))
    matches = 0

    for item in results:
        drawn = dict(sorted(Counter(item).items()))
        tester = 0
        for eb in expected_balls.items():
            if eb[0] in drawn and eb[1] <= drawn[eb[0]]:
                    tester += 1
        if tester == len(expected_balls):
            matches += 1

    probability =matches/num_experiments
    return probability
    
   