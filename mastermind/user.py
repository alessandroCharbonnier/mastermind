import abc

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

class HumanPlayer(Player):
    def __init__(self, solution_length) -> None:
        super().__init__(solution_length)

    def play(self, game_state):
        user_input = input("Votre essaie : ")
        return list(map(int, user_input.split()))

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

    def play(self, game_state, solution):
        import random
        print('solution', solution)
        print('before', set(solution) in self.possibilities)
        print("len", len(game_state))
        if len(game_state) == 0:
            print(a:=list(random.choice(self.possibilities)))
            return a
        self.nb_well_placed(game_state[-1]['check']['well_placed'], game_state[-1]['guess'])
        self.nb_not_well_placed(game_state[-1]['check']['not_well_placed'], game_state[-1]['guess'])
        print(a:=list(random.choice(self.possibilities)), len(self.possibilities))
        print('present ?', set(solution) in self.possibilities)
        return a

    def create_all_possibilities(self):
        temp = [set([i, j, k, l]) for i in range(8) for j in range(8) for k in range(8) for l in range(8)]
        return [t for t in temp if len(t) == self.solution_length]

    def nb_not_well_placed(self, number, array):
        array = set(array)
        self.possibilities = [p for p in self.possibilities if len(array & p) >= number]
        print(len(self.possibilities))

    def nb_well_placed(self, number, array):
        if number == 0:
            for i, p in reversed(list(enumerate(self.possibilities))):
                for l1, l2 in zip(set(array), p):
                    if l1 == l2:
                        del self.possibilities[i]
                        break
        #    self.possibilities = [p for p in self.possibilities if sum(l1 != l2 for l1, l2 in zip(set(array), p)) == 4]
        else:
            self.possibilities = [p for p in self.possibilities if sum(l1 == l2 for l1, l2 in zip(set(array), p)) == number]

