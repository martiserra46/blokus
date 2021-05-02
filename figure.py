import math

class Figure():
    def __init__(self, letter):
        self.letter = letter
        self.positions = None
        self.width, self.height = None, None
        self.matrix_to_draw = None

        self.setup_positions()
        self.setup_width_height()
        self.setup_matrix_to_draw()

    def setup_positions(self):
        pass

    def setup_width_height(self):
        min_x, min_y = math.inf, math.inf
        max_x, max_y = -math.inf, -math.inf
        for (x, y) in self.positions:
            if x < min_x:
                min_x = x
            if y < min_y:
                min_y = y
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
        self.width, self.height = max_x - min_x + 1, max_y - min_y + 1

    def setup_matrix_to_draw(self):
        matrix = [[' ' for j in range(self.width)] for i in range(self.height)]
        for (x, y) in self.positions:
            matrix[y][x] = self.letter
        self.matrix_to_draw = matrix
    
    def print(self):
        for row in self.matrix_to_draw:
            print('| ' + ' | '.join(row) + ' |')
    
    def rotate(self):
        new_positions = set()
        for (x, y) in self.positions:
            new_positions.add((self.height - 1 - y, x))
        self.positions = new_positions
        self.setup_width_height()
        self.setup_matrix_to_draw()
    
    def flip(self):
        new_positions = set()
        for (x, y) in self.positions:
            new_positions.add((self.width - 1 - x, y))
        self.positions = new_positions
        self.setup_width_height()
        self.setup_matrix_to_draw()

class FigureOneSquare_01(Figure):
    def setup_positions(self):
        self.positions = {(0,0)}

class FigureTwoSquares_01(Figure):
    def setup_positions(self):
        self.positions = {(0,0),(1,0)}

class FigureThreeSquares_01(Figure):
    def setup_positions(self):
        self.positions = {(0,0),(1,0),(2,0)}

class FigureThreeSquares_02(Figure):
    def setup_positions(self):
        self.positions = {(0,0),(1,0),(1,1)}

class FigureFourSquares_01(Figure):
    def setup_positions(self):
        self.positions = {(0,0),(1,0),(2,0),(3,0)}

class FigureFourSquares_02(Figure):
    def setup_positions(self):
        self.positions = {(0,0),(1,0),(0,1),(1,1)}

class FigureFourSquares_03(Figure):
    def setup_positions(self):
        self.positions = {(0,0),(1,0),(1,1),(2,1)}

class FigureFourSquares_04(Figure):
    def setup_positions(self):
        self.positions = {(0,1),(1,0),(1,1),(2,1)}

class FigureFourSquares_05(Figure):
    def setup_positions(self):
        self.positions = {(0,0),(1,0),(2,0),(2,1)}

class FigureFiveSquares_01(Figure):
    def setup_positions(self):
        self.positions = {(0,0),(1,0),(2,0),(3,0),(4,0)}

class FigureFiveSquares_02(Figure):
    def setup_positions(self):
        self.positions = {(0,0),(1,0),(2,0),(3,0),(3,1)}

class FigureFiveSquares_03(Figure):
    def setup_positions(self):
        self.positions = {(0,0),(1,0),(2,0),(2,1),(3,1)}

class FigureFiveSquares_04(Figure):
    def setup_positions(self):
        self.positions = {(0,0),(1,0),(2,0),(2,1),(2,2)}

class FigureFiveSquares_05(Figure):
    def setup_positions(self):
        self.positions = {(0,0),(1,0),(0,1),(1,1),(2,0)}

class FigureFiveSquares_06(Figure):
    def setup_positions(self):
        self.positions = {(0,0),(0,1),(1,1),(2,1),(2,0)}

class FigureFiveSquares_07(Figure):
    def setup_positions(self):
        self.positions = {(0,1),(0,2),(1,1),(2,1),(2,0)}

class FigureFiveSquares_08(Figure):
    def setup_positions(self):
        self.positions = {(0,0),(0,1),(1,1),(1,2),(2,2)}

class FigureFiveSquares_09(Figure):
    def setup_positions(self):
        self.positions = {(0,1),(1,1),(1,0),(2,1),(1,2)}

class FigureFiveSquares_10(Figure):
    def setup_positions(self):
        self.positions = {(1,0),(1,1),(1,2),(0,2),(2,2)}

class FigureFiveSquares_11(Figure):
    def setup_positions(self):
        self.positions = {(0,1),(1,0),(1,1),(2,1),(2,2)}

class FigureFiveSquares_12(Figure):
    def setup_positions(self):
        self.positions = {(0,0),(1,0),(2,0),(2,1),(3,0)}