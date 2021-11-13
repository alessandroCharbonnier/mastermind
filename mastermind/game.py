import random
import abc

class Game:
    def __init__(self, user, view) -> None:
        self.solution_length: int = 4 # à changer
        self.solution: list[int] = self.create_solution()
        self.tries: list[dict] = []
        self.max_tries = 8
        self.game_has_ended = False
        self.user = user
        self.view = view

    def create_solution(self):
        possibilities = [i for i in range(8)]

        solution = []
        for i in range(self.solution_length):
            index = random.randint(0, len(possibilities)-1)
            solution.append(possibilities[index])
            possibilities.pop(index)
        return solution


    def user_submition(self, user_input:list[int]):
        """
        ajoute a la fin de tries
        {
            'guess' : [1,3,5,8] => user_input,
            'check' : {well_placed: 2, not_well_placed:1}
        }
        """
        self.tries.append({"guess" : user_input,
                           "check" : self.check(user_input)
                          })
        
        if a:=self.has_user_won():
            self.game_has_ended = True
            return 1, "YOU WIN", a
        elif a:=self.has_user_lost():
            self.game_has_ended = True
            return -1, "YOU LOOSE", a
        else:
            return 0, self.tries[-1]['check']

    def check(self, user_input:list[int]) -> dict:
        '''
        compare user_input avec self.solution
        return un dict {well_placed: nb_vrai, not_well_placed: nb_faux}
        '''

        included = set(user_input) & set(self.solution)

        well_placed = []
        for i, e in enumerate(user_input):
            if e == self.solution[i]:
                well_placed.append(e)

        return {"well_placed": len(well_placed),
                "not_well_placed" : len(included ^ set(well_placed))}


    def has_user_won(self):
        '''
        check le dernier items de self.tries et regarde si check{well_placed} == self.solution_length
        '''
        return self.solution if self.tries[-1]["check"]["well_placed"] == 4 else False


    def has_user_lost(self):
        return self.solution if len(self.tries) == self.max_tries - 1 else False


    def validate_input(self, input):
        if not isinstance(input, list):
            return False

        if len(input) != self.solution_length:
            return False

        if not all(isinstance(x, int) for x in input):
            return False

        if not all(0 <= x <= 8 for x in input):
            return False

        # doublons
        if len(set(input)) != self.solution_length:
            return False

        return True

    def play(self):
        while not self.game_has_ended:
            user_input = None
            while not self.validate_input(user_input):
                user_input = self.user.play(self.tries)
                game_state = self.user_submition(user_input)
                self.view.display_state(self.tries)
                if game_state[0] != 0:
                    self.game_has_ended = True
                    self.view.display_end(self.solution)




        


if __name__ == "__main__":
    print(Game().create_solution())
