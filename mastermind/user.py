import abc
import random

class Player:
    def __init__(self, solution_length) -> None:
        self.solution_length = solution_length
    
    @abc.abstractclassmethod
    def play(self, game_state):
        raise NotImplementedError

    def set_name(self, name):
        self.name = name

    @abc.abstractclassmethod
    def pick_name(self):
        raise NotImplementedError

    @abc.abstractclassmethod
    def reset(self):
        raise NotImplementedError

class HumanPlayer(Player):
    def __init__(self, solution_length) -> None:
        super().__init__(solution_length)

    def play(self, game_state):
        user_input = input("Votre essaie : ")
        try:
            return list(map(int, user_input.split()))
        except ValueError:
            return -1
            

    def pick_name(self):
        return input("What's your name ? ")

class IdiotPlayer(Player):
    def __init__(self, solution_length) -> None:
        super().__init__(solution_length)

    def play(self, game_state):
        import random
        return random.sample([i for i in range(8)], self.solution_length)

    def pick_name(self):
        return "I'm retarded"

class AIPlayer(Player):
    def __init__(self, solution_length) -> None:
        super().__init__(solution_length)
        self.possibilities = self.create_all_possibilities()

    def pick_name(self):
        return "I'm smart"


    def reset(self):
        self.possibilities = self.create_all_possibilities()

    def play(self, game_state):
        if game_state:
            self.possibilities = self.delete_well_placed(game_state[-1]['guess'], game_state[-1]['check']['well_placed'])
            self.possibilities = self.delete_not_well_placed(game_state[-1]['guess'], game_state[-1]['check']['not_well_placed'] + game_state[-1]['check']['well_placed'])
            
            if not sum([v for v in game_state[-1]['check'].values()]):
                self.possibilities = self.delete_not_in(game_state[-1])
            
            tries = [t['guess'] for t in game_state]
            guess = random.choices(self.possibilities)[0]
            while guess in tries:
                guess = random.choices(self.possibilities)[0]
        else:
            guess = random.choices(self.possibilities)[0]
        return guess

    def create_all_possibilities(self):
        solutions = []
        for number in range(10**self.solution_length):
            num_str=str(number).zfill(self.solution_length)
            l = [int(i) for i in num_str]
            if not ('8' in num_str or '9' in num_str) and len(set(l)) == self.solution_length:
                solutions.append(l)

        [str(number).zfill(self.solution_length) for number in range(10**self.solution_length)]
        return solutions

    def nb_well_placed(self, guess, solution):
        return len([e for i, e in enumerate(guess) if e == solution[i]])

    def nb_not_well_placed(self, guess, solution):
        return len(set(guess) & set(solution))

    def delete_well_placed(self, guess, number):
        # TODO: prendre en compte l'historique des parties
        temp = []
        if number == 0:
            return [p for p in self.possibilities if p[0] != guess[0] and p[1] != guess[1] and p[2] != guess[2] and p[3] != guess[3]]
        else:
            for p in self.possibilities:
                count = 0
                for i, e in enumerate(p):
                    if e == guess[i]:
                        count += 1
                if count >= number:
                    temp.append(p)
        return temp

    def delete_not_well_placed(self, guess, number):
        temp = []
        for p in self.possibilities:
            if self.nb_not_well_placed(p, guess) == number:
                temp.append(p)
        return temp

    def delete_not_in(self, guess):
        guess = set(guess)
        temp = []
        for p in self.possibilities:
            if not (set(p) & guess):
                temp.append(p)
        return temp