import random


def len_iters_random(size):
    permutations = []
    lis = [i for i in range(1, size + 1)]
    for i in lis:
        for j in lis:
            for k in lis:
                for l in lis:
                    if i + j + k + l == size:
                        permutations.append([i, j, k, l])
    return random.choice(permutations)
