import random

def nb_well_placed(guess, solution):
    return len([e for i, e in enumerate(guess) if e == solution[i]])


def nb_not_well_placed(guess, solution):
    return len(set(guess) & set(solution))


def delete_not_well_placed(guess, number):
    temp = []
    for p in possibilities:
        if nb_not_well_placed(p, guess) >= number:
            temp.append(p)
    return temp

def delete_well_placed(guess, number):
    temp = []
    if number == 0:
        for p in possibilities:
            if p[0] != guess[0] and p[1] != guess[1] and p[2] != guess[2] and p[3] != guess[3]:
                temp.append(p)
    else:
        for p in possibilities:
            count = 0
            for i, e in enumerate(p):
                if e == guess[i]:
                    count += 1
            if count >= number:
                temp.append(p)
    return temp

solution = random.sample([i for i in range(8)], 4)

possibilities = [[i, j, k, l] for i in range(8) for j in range(8) for k in range(8) for l in range(8) if len(set([i, j, k, l])) == 4]

guess = None
tries = []
while guess != solution:
    guess = random.choices(possibilities)[0]
    while guess in tries:
        guess = random.choices(possibilities)[0]
    tries.append(guess)
    possibilities = delete_well_placed(guess, nb_well_placed(guess, solution))
    possibilities = delete_not_well_placed(guess, nb_not_well_placed(guess, solution))
    print(f"{len(possibilities)}")

print(len(tries), tries)
print(f"{solution in possibilities=}")
print(guess, solution)
