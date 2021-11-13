import abc

class Player:
    def __init__(self, nom) -> None:
        self.nom = nom
    
    @abc.abstractclassmethod
    def play(self, game_state):
        raise NotImplementedError

class HumanPlayer(Player):
    def __init__(self, nom) -> None:
        super().__init__(self, nom)

    def play(self, game_state):
        return input("Votre essaie : ")


