from figure import *
import random as rd

class Player():
    def __init__(self, letter):
        self.letter = letter
        self.figures_used = None
        self.figures_not_used = None

        self.setup_figures()
    
    def setup_figures(self):
        self.figures_used = []
        self.figures_not_used = [
            FigureOneSquare_01(self.letter),
            FigureTwoSquares_01(self.letter),
            FigureThreeSquares_01(self.letter),
            FigureThreeSquares_02(self.letter),
            FigureFourSquares_01(self.letter),
            FigureFourSquares_02(self.letter),
            FigureFourSquares_03(self.letter),
            FigureFourSquares_04(self.letter),
            FigureFourSquares_05(self.letter),
            FigureFiveSquares_01(self.letter),
            FigureFiveSquares_02(self.letter),
            FigureFiveSquares_03(self.letter),
            FigureFiveSquares_04(self.letter),
            FigureFiveSquares_05(self.letter),
            FigureFiveSquares_06(self.letter),
            FigureFiveSquares_07(self.letter),
            FigureFiveSquares_08(self.letter),
            FigureFiveSquares_09(self.letter),
            FigureFiveSquares_10(self.letter),
            FigureFiveSquares_11(self.letter),
            FigureFiveSquares_12(self.letter)
        ]
    
    def print_figures_not_used(self):
        i = 0
        for figure in self.figures_not_used:
            print(f'Figure {i}')
            figure.print()
            if i < len(self.figures_not_used) - 1:
                print('\n\n', end='')
                i += 1
    
    def make_move(self, board):
        pass

    def all_figures_used(self):
        return len(self.figures_not_used) == 0
    
    def can_move(self, board):
        for figure in self.figures_not_used:
            if board.can_insert_figure(figure):
                return True
        return False
    
    def get_points(self):
        num = 0
        for figure in self.figures_used:
            for position in figure.positions:
                num += 1
        return num

class HumanPlayer(Player):
    def make_move(self, board):
        print("---INSERT FIGURE---\n\n", end='')

        all_data_chosen = False
        while not all_data_chosen:
            # Choose figure
            figure = self.choose_figure(board)

            # Rotate/Flip figure
            result = self.rotate_flip_figure(board, figure)
            if (not result):
                continue
            figure = result

            # Select position
            result = self.choose_position(board, figure)
            if (not result):
                continue
            (x, y) = result

            all_data_chosen = True

        board.insert_figure(x, y, figure)
        self.figures_not_used.remove(figure)
        self.figures_used.append(figure)
    
    def choose_figure(self, board):
        valid = False
        while not valid:
            try:
                # Choose figure
                print("Choose one of these figures\n\n", end='')
                self.print_figures_not_used()
                print('\n',end='')
                board.print()
                print('\n', end='')
                out = int(input('Fig. number: '))
                if out < 0 or out >= len(self.figures_not_used):
                    raise ValueError
                figure = self.figures_not_used[out]
                print('\n', end='')
                figure.print()
                print('\n', end='')
                valid = True
            except ValueError:
                print("Invalid figure number\n\n", end='')
        return figure
    
    def rotate_flip_figure(self, board, figure):
        valid = False
        while not valid:
            try:
                # Rotate figure
                modify_figure = True
                while modify_figure:
                    out = input('Rotate (r)\nFlip (f)\nChange fig. (cf)\nContinue (c)\n - ')
                    if out == 'cf':
                        return False
                    if out == 'r':
                        figure.rotate()
                        print('\n',end='')
                        figure.print()
                    elif out == 'f':
                        figure.flip()
                        print('\n',end='')
                        figure.print()
                    elif out == 'c':
                        modify_figure = False
                    else:
                        raise ValueError
                    print('\n',end='')
                valid = True
            except ValueError:
                print("Invalid input\n\n", end='')
        return figure
    
    def choose_position(self, board, figure):
        valid = False
        while not valid:
            try:
                # Choose position
                print("Choose one position\n\n", end='')
                print('\n',end='')
                board.print()
                print('\n', end='')
                out = input('Position (x,y)\nChange fig. (cf)\n - ')
                if out == 'cf':
                    return False
                pos = out.split(',')
                x = int(pos[0])
                y = int(pos[1])
                if not board.is_valid(x, y, figure):
                    raise ValueError
                print('\n', end='')
                valid = True
            except:
                print("Invalid position\n\n")
        return (x, y)

class RandomComputerPlayer(Player):
    def make_move(self, board):
        found = False
        while not found:
            figure = self.figures_not_used[rd.randint(0, len(self.figures_not_used) - 1)]
            num_rotations = rd.randint(0, 3)
            for _ in range(num_rotations):
                figure.rotate()
            num_flips = rd.randint(0, 1)
            for _ in range(num_flips):
                figure.flip()
            available_positions = board.get_available_positions(figure)
            if len(available_positions) > 0:
                (x, y) = rd.choice(available_positions)
                found = True
        board.insert_figure(x, y, figure)
        self.figures_not_used.remove(figure)
        self.figures_used.append(figure)