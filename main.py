if __name__ == "__main__":
    from mastermind.view import ViewTerminal
    from mastermind.user import HumanPlayer, IdiotPlayer
    from mastermind.game import Game
    Game(HumanPlayer("Alessandro"), ViewTerminal).play()
