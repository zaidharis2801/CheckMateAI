import copy
import numpy as np
import random
from collections import Counter


class Checkerboard:
    board = [["0"] * 6 for i in range(6)]
    currentPlayer = "red"

    def making_board(self):
        self.board= [["0"] * 6 for i in range(6)]
        for i in range(len(self.board)):

            if i == 0 or i == 1:

                for j in range(len(self.board)):
                    if i % 2 == 0 and j % 2 == 0:
                        self.board[i][j] = "B"
                    elif i % 2 == 1 and j % 2 == 1:
                        self.board[i][j] = "B"
            if i == 4 or i == 5:

                for j in range(len(self.board[i])):
                    if i % 2 == 0 and j % 2 == 0:
                        self.board[i][j] = "R"
                    elif i % 2 == 1 and j % 2 == 1:
                        self.board[i][j] = "R"

        for place in self.board:
            print(place, end='')
            print('')

    def switchCurrentPlayer(self):
        if self.currentPlayer == "red":
            self.currentPlayer = "black"
        elif self.currentPlayer == "black":
            self.currentPlayer = "red"

    def get_Color(self, row, col):
        return self.board[row][col]

    def is_valid_position(self, row, col):
        if (row < 0 or row > 5):
            return False
        else:
            if (col < 0 or col > 5):
                return False
            else:
                return True

    def all_possible_moves(self,board,player):
        all_moves = []

        if player == "red":
            for i in range(6):
                for j in range(6):
                    new_board = copy.deepcopy(board)
                    if new_board[i][j] == "R":
                        if self.is_valid_position(i - 1, j - 1):
                            if self.get_Color(i - 1, j - 1) == "B":
                                if self.is_valid_position(i - 2, j - 2):
                                    if new_board[i - 2][ j - 2]=="0":
                                        new_board[i - 2][j - 2] = 'R'
                                        new_board[i - 1][j - 1] = '0'
                                        new_board[i][j] = "0"
                                        all_moves.append(new_board)
                                        new_board = copy.deepcopy(board)
                            if self.get_Color(i - 1, j - 1) == "0":
                                if new_board[i - 1][j - 1] =="0":
                                    new_board[i - 1][j - 1] = 'R'
                                    new_board[i][j] = "0"
                                    all_moves.append(new_board)
                                    new_board = copy.deepcopy(board)


                        if self.is_valid_position(i - 1, j + 1):
                            if self.get_Color(i - 1, j + 1) == "B":
                                if self.is_valid_position(i - 2, j + 2):
                                    if new_board[i - 2][j + 2] == "0":
                                        new_board[i - 2][j + 2] = 'R'
                                        new_board[i - 1][j + 1] = '0'
                                        new_board[i][j] = "0"
                                        all_moves.append(new_board)
                                        new_board = copy.deepcopy(board)
                            if self.get_Color(i - 1, j + 1) == "0":
                                if new_board[i - 1][j + 1] == "0":
                                    new_board[i - 1][j + 1] = 'R'
                                    new_board[i][j] = "0"
                                    all_moves.append(new_board)


        if player == "black":
            for i in range(6):
                for j in range(6):
                    new_board = copy.deepcopy(board)
                    if self.board[i][j] == "B":
                        if self.is_valid_position(i + 1, j + 1):
                            if self.get_Color(i + 1, j + 1) == "R":
                                if self.is_valid_position(i + 2, j + 2):
                                    if new_board[i + 2][j + 2] == "0":
                                        new_board[i + 2][j + 2] = 'B'
                                        new_board[i + 1][j + 1] = '0'
                                        new_board[i][j] = "0"
                                        all_moves.append(new_board)
                                        new_board = copy.deepcopy(board)
                            if self.get_Color(i + 1, j + 1) == "0":
                                if new_board[i + 1][j + 1] == "0":
                                    new_board[i + 1][j + 1] = 'B'
                                    new_board[i][j] = "0"
                                    all_moves.append(new_board)
                                    new_board = copy.deepcopy(board)



                        if self.is_valid_position(i + 1, j - 1):
                            if self.get_Color(i + 1, j - 1) == "R":
                                if self.is_valid_position(i +2, j - 2):
                                    if new_board[i + 2][j - 2] == "0":
                                        new_board[i + 2][j - 2] = 'B'
                                        new_board[i + 1][j - 1] = '0'
                                        new_board[i][j] = "0"
                                        all_moves.append(new_board)
                                        new_board = copy.deepcopy(board)
                            if self.get_Color(i + 1, j - 1) == "0":
                                if new_board[i + 1][j - 1] == "0":
                                    new_board[i + 1][j - 1] = 'B'
                                    new_board[i][j] = "0"
                                    all_moves.append(new_board)

        return all_moves



    def one_move(self):
        self.making_board()
        self.board[0][2] = "R"


    def eval1(self,board):
        r_count = 0
        b_count = 0
        r_queen_count = 0
        b_queen_count = 0
        for row in range(len(board)):
            if row == 0:
                r_queen_count += board[row].count("R")
                b_count += board[row].count("B")
            elif row == 5:
                b_queen_count += board[row].count("B")
                r_count += board[row].count("R")
            else:
                r_count += board[row].count("R")
                b_count += board[row].count("B")
        red_points = r_count + 3 * r_queen_count
        black_points = b_count + b_queen_count * 3
        return red_points - black_points

    def eval2(self,board):
        red_points = 0
        black_points = 0
        for row in range(len(board)):
            r_count = board[row].count("R")
            b_count = board[row].count("B")
            black_points = black_points + b_count * (1 + (row * 0.1))
            red_points = red_points + r_count * (1 + ((5 - row) * 0.1))
        return red_points - black_points

    def terminal(self,board):

        return not bool(self.all_possible_moves(board,self.currentPlayer))

    def play_game(self,depth,depth2):
        self.making_board()
        possible_moves = self.all_possible_moves(self.board, "red")
        count = 0

        while self.terminal(self.board) is False:
            count += 1
            if self.currentPlayer == "red":
                val, b2 = self.minimax(True, self.board, depth, -999, 999)
            else:

                val, b2 = self.minimax(False, self.board, depth2, -999, 999)
            print(b2)
            self.board = copy.deepcopy(b2)

            print("*************")
            self.switchCurrentPlayer()
        print(self.currentPlayer)

        print(self.eval1(self.board))
        print("count {0}".format(count))
        return self.eval1(self.board),self.currentPlayer

    def play_game2(self,depth1,depth2):
        self.making_board()
        possible_moves = self.all_possible_moves(self.board, "red")
        count = 0

        while self.terminal(self.board) is False:
            count += 1
            if self.currentPlayer == "red":
                val, b2 = self.minimax2(True, self.board, depth1, -999, 999)
            else:

                val, b2 = self.minimax2(False, self.board, depth2, -999, 999)
            print(b2)
            self.board = copy.deepcopy(b2)

            print("*************")
            self.switchCurrentPlayer()
        print(self.currentPlayer)

        print(self.eval1(self.board))
        print("count {0}".format(count))
        return self.eval1(self.board),self.currentPlayer
    def play_game3(self,depth):
        self.making_board()
        possible_moves = self.all_possible_moves(self.board,"red")
        count = 0

        while self.terminal(self.board) is False :
            count += 1
            if self.currentPlayer=="red":
                val, b2 = self.minimax(True,self.board, depth,-999,999)
            else:

                val, b2 = self.minimax2(False,self.board,depth,-999,999)
            print(b2)
            self.board = copy.deepcopy(b2)
            # for myl in b2:
            #     for idx, item in enumerate(myl):
            #         if item == "0":
            #             myl[idx] = " "
            # print("*************")
            # print("Count: {0}".format(count))
            # for place in b2:
            #     print(place, end='')
            #     print('')
            print("*************")
            self.switchCurrentPlayer()
        print(self.currentPlayer)

        print(self.eval1(self.board))
        print("count {0}".format(count))
        return self.eval1(self.board),self.currentPlayer
    def play_game4(self,depth):
        self.making_board()
        possible_moves = self.all_possible_moves(self.board,"red")
        count = 0

        while self.terminal(self.board) is False :
            count += 1
            if self.currentPlayer=="red":
                val, b2 = self.minimax2(True,self.board, depth,-999,999)
            else:
                temp_board= copy.deepcopy(self.board)
                all_moves=self.all_possible_moves(temp_board, "black")
                b2=all_moves[random.randint(0,len(all_moves)-1)]
            print(b2)
            self.board = copy.deepcopy(b2)
            # for myl in b2:
            #     for idx, item in enumerate(myl):
            #         if item == "0":
            #             myl[idx] = " "
            # print("*************")
            # print("Count: {0}".format(count))
            # for place in b2:
            #     print(place, end='')
            #     print('')
            print("*************")
            self.switchCurrentPlayer()
        print(self.currentPlayer)

        print(self.eval1(self.board))
        print("count {0}".format(count))
        return self.eval1(self.board),self.currentPlayer


    def minimax(self, max_player, board, depth,min,max):

            if self.terminal(board) or depth == 0:
                return self.eval1(board), board

            if max_player:
                best_eval = min
                best_move = None
                for move in self.all_possible_moves(board, "red"):
                    evaluation = self.minimax(False, board, depth - 1, best_eval, max)[0]
                    if evaluation > best_eval:
                        best_eval = evaluation
                        best_move = move
                    if evaluation == best_eval:
                        ran = random.randint(1, 2)
                        if ran == 1:
                            best_move = move
                    if best_eval >= max:
                        print("Computation saved due to pruning.")
                        return max, move

                return best_eval, best_move
            else:
                best_eval = max
                best_move = None
                for move in self.all_possible_moves(board, "black"):
                    evaluation = self.minimax(True, board, depth - 1, min, best_eval)[0]
                    if evaluation < best_eval:
                        best_eval = evaluation
                        best_move = move
                    if best_eval == best_eval:
                        ran = random.randint(1, 2)
                        if ran == 1:
                            best_move = move
                    if best_eval <= min:
                        print("Computation saved due to pruning.")
                        return min, move

                return best_eval, best_move


    def minimax2(self, max_player, board, depth,min,max):
        if self.terminal(board) or depth == 0:
            return self.eval2(board), board

        if max_player:
            best_eval = min
            best_move = None
            for move in self.all_possible_moves(board, "red"):
                evaluation = self.minimax2(False, board, depth - 1,best_eval,max)[0]
                if evaluation > best_eval:
                    best_eval = evaluation
                    best_move = move
                if evaluation == best_eval:
                    ran = random.randint(1, 2)
                    if ran == 1:
                        best_move = move
                if evaluation>=max:
                    print("Computation saved due to pruning.")
                    return max,move

            return best_eval, best_move
        else:
            best_eval = max
            best_move = None
            for move in self.all_possible_moves(board, "black"):
                evaluation = self.minimax2(True, board, depth - 1, min, best_eval)[0]
                if evaluation < best_eval:
                    best_eval = evaluation
                    best_move = move
                if evaluation == best_eval:
                    ran = random.randint(1, 2)
                    if ran == 1:
                        best_move = move
                if evaluation<=min:
                    print("Computation saved due to pruning.")
                    return min, move

            return best_eval, best_move



game =Checkerboard()
game_list1=[]


res=game.play_game4(2)
if res[0]>0:
        game_list1.append("red")
elif res[0]<0:
        game_list1.append("black")
else:
        game_list1.append(res[1] + "d")
game_list2=[]

print(Counter(game_list1))

