import abc

class View:
    def __init__(self, solution_length, max_tries) -> None:
        self.solution_length = solution_length
        self.max_tries = max_tries

    @abc.abstractclassmethod
    def display_state(self, state):
        raise NotImplementedError

    @abc.abstractclassmethod
    def display_end(self, solution):
        raise NotImplementedError

    @abc.abstractclassmethod
    def display_error(self, error):
        raise NotImplementedError


class ViewTerminal(View):
    def __init__(self, *args, **kargs) -> None:
        super().__init__(*args, **kargs)

    def display_grid(self, state):
        print("+" + "---" * self.solution_length + "+")
        for i in range(self.max_tries-1, -1, -1):
            a = [" "]*self.solution_length if i >= len(state) else state[i]["guess"]

            line = "|"
            for e in a:
                line += f'[{e}]'
            line += '|'
            line += f'({state[i]["check"]["well_placed"]}, {state[i]["check"]["not_well_placed"]})' if i < len(state) else ''
            print(line)
        print("+" + "---" * self.solution_length +"+")


    def display_state(self, state):
        print("\n"*2)
        print("|" + "[?]" * self.solution_length + "|")
        self.display_grid(state)
        

    def display_error(self, error):
        print(error)

    def display_end(self, state, solution, game_state):
        print("\n"*2)
        line = "|"
        for a in solution:
            line += f"[{a}]"
        line += "| THE SOLUTION"
        print(line)
        self.display_grid(state)
        print(game_state[1])


