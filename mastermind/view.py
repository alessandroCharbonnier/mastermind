import abc

class View:
    def __init__(self) -> None:
        pass

    @abc.abstractclassmethod
    def display_state(self, state):
        raise NotImplementedError

    @abc.abstractclassmethod
    def display_end(self):
        raise NotImplementedError


class ViewTerminal(View):
    def __init__(self) -> None:
        super().__init__()

    def display_state(self, state):
        print()
"""
+------------+
|[ ][ ][ ][ ]|
|[ ][ ][ ][ ]|
|[ ][ ][ ][ ]|
|[ ][ ][ ][ ]|
|[ ][ ][ ][ ]|
|[ ][ ][ ][ ]|
"""
