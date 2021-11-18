if __name__ == "__main__":
    from mastermind.view import ViewTerminal
    from mastermind.user import HumanPlayer, IdiotPlayer, AIPlayer
    from mastermind.game import Game
    Game(AIPlayer, ViewTerminal).play()
