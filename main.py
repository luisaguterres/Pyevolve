from pyevolve import G1DList
from pyevolve import GSimpleGA


def eval_func(chromosome):
    score = 0.0

    for value in chromosome:
        if value==0:
            score +=1.0

    return score


genome = G1DList.G1DList(20)

genome.evaluator.set(eval_func)
genome.setParams(rangemin=0, rangemax=10)

ga = GSimpleGA.GSimpleGA(genome)

ga.evolve(freq_stats=10)

print ga.bestIndividual()