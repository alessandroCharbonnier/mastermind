import signal

game = None
def handler(signum, frame):
    game.exit()

signal.signal(signal.SIGINT, handler)

if __name__ == "__main__":
    from mastermind.view import ViewTerminal, GView
    from mastermind.user import HumanPlayer, IdiotPlayer, AIPlayer
    from mastermind.game import Game
    game = Game(HumanPlayer, GView, solution_length=4)
    game.play()
