import abc

class Player:
    def __init__(self, nom) -> None:
        self.nom = nom
    
    @abc.abstractclassmethod
    def play(self, game_state):
        raise NotImplementedError

class HumanPlayer(Player):
    def __init__(self, nom) -> None:
        super().__init__(nom)

    def play(self, game_state):
        user_input = input("Votre essaie : ")
        return list(map(int, user_input.split()))

import random
class IdiotPlayer(Player):
    def __init__(self, nom) -> None:
        super().__init__(nom)

    def play(self, game_state):
        return [random.randint(0, 7) for _ in range(4)]


