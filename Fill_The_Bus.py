import itertools

groups = [3, 4, 6, 5, 7, 6, 2, 4, 9, 8, 2]


def combinations(data):
    for combo in itertools.combinations(groups, 3):
        if sum(combo) == 15:
            print(combo)


combinations(groups)
