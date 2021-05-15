from numpy.random import randint
from numpy.random import rand


def one_max(bitstring: list):
    return -sum(bitstring)

def selection(pop: list, scores: list, k=3) -> str:
    ''' Takes a list of parents and randomly selects
        two of them, if the fitness score of the second
        is greater than the initial, then that parent
        is selected and returned. '''
    selection_x = randint(len(pop))
    #selection_x = randint(0, len(pop), k-1)
    for i in randint(0, len(pop), k-1):
        if scores[i] < scores[selection_x]:
            selection_x = i
    return pop[selection_x]


def crossover(parent_a: list, parent_b: list, r_crossover: float) -> list:
    ''' Takes two selected parents, if the rate of crossover is
        greater than a random generated number between 0-1, then a
        random crossing point within len(string) is selected and
        two childs formed from recombination. '''
    child_a, child_b = parent_a.copy(), parent_b.copy()
    if rand() < r_crossover:
        parent_cp = randint(1, len(parent_a)-2)  # cp can not be end of string
        child_a = parent_a[:parent_cp] + parent_b[parent_cp:]  # crossover
        child_b = parent_b[:parent_cp] + parent_a[parent_cp:]
    return [child_a, child_b]


def mutation(bitstring: list, r_mutation: float):
    ''' Mutates bitstring by changing 1 -> 0 if thresh reached. '''
    for i in range(len(bitstring)):
        if rand() < r_mutation:
            bitstring[i] = 1 - bitstring[i]


def ga(objective_func, n_bits, n_iter, n_pop, r_crossover, r_mutation):
    # init n_pop bitstrings of length n_bits
    pop = [randint(0, 2, n_bits).tolist() for i in range(n_pop)]
    # take init best bitstring and score to be the first
    best, best_eval = 0, objective_func(pop[0])
    for gen in range(n_iter): # start generation loop
        # get scores of every bitstring in population
        scores = [objective_func(candidate) for candidate in pop]
        for n, i in enumerate(range(n_pop)): # iterate over bitstring population
            if scores[i] < best_eval:  # if ith bitstring has a better score than prev
                best, best_eval = pop[i], scores[i] # update best string and score
                print(">%d, new best f(%s) = %.3f" % (gen,  pop[i], scores[i]))
                if best_eval == float(-1*n_bits):
                    print('FOUND MIN: n_iter = %s, n_pop = %s' % (gen, n))
                    return [best, best_eval]
            # call selection func and return the best of every selection pair
        selected = [selection(pop, scores) for i in range(n_pop)]
        children = []
        for i in range(0, n_pop, 2):  # group parents into twos
            parent_a, parent_b = selected[i], selected[i+1]
            for c in crossover(parent_a, parent_b, r_crossover):
                mutation(c, r_mutation)
                children.append(c)
        pop = children
        print(gen)
    return [best, best_eval]


if __name__ =='__main__':
    n_iter = 100
    n_bits = 20
    n_pop = 1000
    r_crossover = 0.9
    r_mutation = 1.0/float(n_bits)
    best, score = ga(one_max, n_bits, n_iter, n_pop, r_crossover, r_mutation)
    print("Finished!")
    print("f(%s) = %f" % (best, score))
