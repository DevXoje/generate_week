from functions import getNextLetter


class Row:
    def __init__(self, letter: str, n_row: int):
        self.INITIAL_LETTER = letter
        self.INITAL_ROW = n_row
        self.letter = letter
        self.INITIAL_CELL = letter+str(n_row)
        self.n_row = n_row

    def get_position(self) -> str:
        return self.letter+str(self.n_row)

    def next_row(self, steps=1) -> None:
        self.letter = self.INITIAL_LETTER
        self.n_row = self.n_row+steps

    def get_formula_total(self):
        init1 = getNextLetter(self.letter, 1)+str(self.n_row+1)
        final1 = getNextLetter(self.letter, 2)+str(self.n_row+1)
        init2 = getNextLetter(self.letter, 3)+str(self.n_row+1)
        final2 = getNextLetter(self.letter, 4)+str(self.n_row+1)
        formula = '({}-{})+({}-{})'.format(init1, final1, init2, final2)
        return formula
