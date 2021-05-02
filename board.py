class Board():
    def __init__(self):
        self.rows = 20
        self.cols = 20
        self.matrix = None

        self.setup_matrix()
    
    def setup_matrix(self):
        self.matrix = [[' ' for j in range(self.cols)] for i in range(self.rows)]
    
    def is_valid(self, x_pos, y_pos, figure):
        for (x, y) in figure.positions:
            x += x_pos
            y += y_pos
            if x < 0 or x >= self.cols or y < 0 or y >= self.rows:
                return False
            if self.matrix[y][x] != ' ':
                return False
            if (x > 0 and self.matrix[y][x - 1] == figure.letter) or (x < self.cols - 1 and self.matrix[y][x + 1] == figure.letter):
                return False
            if (y > 0 and self.matrix[y - 1][x] == figure.letter) or (y < self.rows - 1 and self.matrix[y + 1][x] == figure.letter):
                return False
        for (x, y) in figure.positions:
            x += x_pos
            y += y_pos
            if x > 0 and y > 0:
                if self.matrix[y - 1][x - 1] == figure.letter:
                    return True
            if x > 0 and y < self.rows - 1:
                if self.matrix[y + 1][x - 1] == figure.letter:
                    return True
            if x < self.cols - 1 and y > 0:
                if self.matrix[y - 1][x + 1] == figure.letter:
                    return True
            if x < self.cols - 1 and y < self.rows - 1:
                if self.matrix[y + 1][x + 1] == figure.letter:
                    return True
            if ((x == 0 and y == 0) or (x == 0 and y == self.rows - 1) or
                (x == self.cols - 1 and y == 0) or 
                (x == self.cols - 1 and y == self.rows - 1)):
                return True
        return False

    def insert_figure(self, x_pos, y_pos, figure):
        if not self.is_valid(x_pos, y_pos, figure):
            return False
        for (x, y) in figure.positions:
            x += x_pos
            y += y_pos
            self.matrix[y][x] = figure.letter
        return True
    
    def get_available_positions(self, figure):
        available_positions = []
        for y in range(self.rows):
            for x in range(self.cols):
                if self.is_valid(x, y, figure):
                    available_positions.append((x, y))
        return available_positions
    
    def can_insert_figure(self, figure):
        for i in range(4):
            figure.rotate()
            for j in range(2):
                figure.flip()
                if len(self.get_available_positions(figure)) > 0:
                    return True
        return False

    def print(self):
        print('{:>9}'.format(''), end='')
        for col_ind in range(self.cols):
            print('{pos:^5} '.format(pos=col_ind), end='')
        print('\n')
        for row_ind in range(self.rows):
            print('{pos:>5}   |'.format(pos=row_ind), end='')
            for col_ind in range(self.cols):
                print('{letter:^5}|'.format(letter=self.matrix[row_ind][col_ind]), end='')
            print('\n')