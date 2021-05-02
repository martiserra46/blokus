from board import Board

class Game():
    def play(self, players):
        board = Board()
        turn = 0
        finished = False
        players_cannot_move = set()
        print('\n',end='')
        print("-----BLOCKUS-----\n\n",end='')
        while not finished:
            board.print()
            print()
            player = players[turn % 4]
            if player not in players_cannot_move and player.can_move(board):
                print(f"-----{player.letter} MOVES-----\n")
                player.make_move(board)
                print()
            else:
                print(f"-----{player.letter} CAN'T MOVE-----\n")
                players_cannot_move.add(player)
            if len(players_cannot_move) > 2 and (turn + 1) % 4 == 0:
                finished = True
            turn += 1
        max_points = 0        
        for player in players:
            points = player.get_points()
            if points > max_points:
                max_points = points
        winners = []
        for player in players:
            if player.get_points() == max_points:
                winners.append(player)
        if len(winners) == 1:
            print(f"-----WINNER IS {winners[0].letter}-----\n")
        else:
            letters = [player.letter for player in winners]
            print("-----IT IS A TIE BETWEEN " + ", ".join(letters) + "-----\n")
        print("-----SCORE-----")
        for player in players:
            print(f"{player.letter}: {player.get_points()}")
        print()
        board.print()
        print()
