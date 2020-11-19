import pygame
from pygame.locals import *
import numpy as np
import math

BACKGROUND_COLOR = (0, 0, 0)
GRID_COLOR = (200, 200, 200)
WINDOWS_WIDTH = 600
WINDOWS_HEIGHT = 600

#Segunda aproximación por clases
class Board():
    def __init__(self, screen):
        self.screen = screen
        self.BlosckSize = 200

    def drawGrid(self):
        for x in range(WINDOWS_WIDTH):
            for y in range(WINDOWS_HEIGHT):
                rect = pygame.Rect(x * self.BlosckSize, y * self.BlosckSize, self.BlosckSize, self.BlosckSize)
                pygame.draw.rect(self.screen, GRID_COLOR, rect, 1)

    def drawBoard(self, table):
        for x in range(3):
            for y in range(3):
                if table[y][x] == 1:
                    pygame.draw.line(self.screen, (200, 0, 0), (50 + 200 * x, 50 + 200 * y),(150 + 200 * x, 150 + 200 * y), 5)
                    pygame.draw.line(self.screen, (200, 0, 0), (150 + 200 * x, 50 + 200 * y),(50 + 200 * x, 150 + 200 * y), 5)
                if table[y][x] == 2:
                    pygame.draw.circle(self.screen, (0, 0, 200), (100 + 200 * x, 100 + 200 * y), 50, 5)

class Player():
    def movePlayer(self, table, turn, key):
        if turn%2 == 0:
            table[int((key - 1)/3)][int((key -1)%3)] = 1
        else:
            table[int((key - 1)/3)][int((key -1)%3)] = 2
        return table

class Game():
    def __init__(self):
        pygame.init()
        self.table_0 = [[0, 0, 0]] * 3
        self.table = np.array(self.table_0)
        self.screen = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HEIGHT))
        self.draw()
        self.board = Board(self.screen)
        self.player = Player()

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        pygame.display.flip()

    def emptyCells(self, table):
        empty = []
        for x in range(3):
            for y in range(3):
                if table[x][y] == 0:
                    empty.append(x * 3 + y + 1)
        return empty

    def minimax(self, table, depth, isMaximizer):
        winner = self.checkGameisOver(table)
        if  winner != 3:
            if winner == 1: #jugador 1
                return -10 + depth
            elif winner == 2: #jugador2
                return 10 - depth
            else:
                return 0

        if isMaximizer:
            maxEval = -math.inf
            for i in self.emptyCells(table):
                tableCopy = np.copy(table)
                self.player.movePlayer(tableCopy, 1, i)
                index = i
                value = self.minimax(tableCopy, depth + 1, False)
                if (value > maxEval):
                    maxEval = value
                    bestIndex = index
            if depth == 0:
                return bestIndex
            return maxEval
        else:
            minEval = math.inf
            for i in self.emptyCells(table):
                tableCopy = np.copy(table)
                self.player.movePlayer(tableCopy, 0, i)
                index = i
                value = self.minimax(tableCopy, depth + 1, True)
                if (value < minEval):
                    minEval = value
                    bestIndex = index
            if depth == 0:
                return bestIndex
            return minEval

    def isBoardFull(self, table):
        if (table[0][0] == 0 or table[0][1] == 0 or table[0][2] == 0 or table[1][0] == 0 or table[1][1] == 0 or table[1][2] == 0 or table[2][0] == 0 or table[2][1] == 0 or table[2][2] == 0):
            return False
        else:
            return True
    
    def checkGameisOver(self, table):
        for x in range(3):
            if(table[x][0] == table[x][1] == table[x][2] != 0):
                return table[x][0]

        for y in range(3):
            if(table[0][y] == table[1][y] == table[2][y] != 0):
                return table[0][y]

        if (table[0][0] == table[1][1] == table[2][2] != 0):
            return table[1][1]

        if (table[0][2] == table[1][1] == table[2][0] != 0):
            return table[1][1]
        
        if self.isBoardFull(table):
            return 0

        return 3

    def run(self):
        run = True
        turn = 0
        finished_game = False

        self.board.drawGrid()

        while run:
            self.board.drawBoard(self.table)

            for event in pygame.event.get():
                if event.type == KEYDOWN:

                    if turn % 2 == 0:
                        if event.key == K_1 and self.table[0][0] == 0:
                            self.table = self.player.movePlayer(self.table, turn, 1)
                            turn += 1
                        elif event.key == K_1 and self.table[0][0] != 0:
                            print('Esta casilla esta ocupada, prueba con otra')

                        if event.key == K_2 and self.table[0][1] == 0:
                            self.table = self.player.movePlayer(self.table, turn, 2)
                            turn += 1
                        elif event.key == K_2 and self.table[0][1] != 0:
                            print('Esta casilla esta ocupada, prueba con otra')

                        if event.key == K_3 and self.table[0][2] == 0:
                            self.table = self.player.movePlayer(self.table, turn, 3)
                            turn += 1
                        elif event.key == K_3 and self.table[0][2] != 0:
                            print('Esta casilla esta ocupada, prueba con otra')

                        if event.key == K_4 and self.table[1][0] == 0:
                            self.table = self.player.movePlayer(self.table, turn, 4)
                            turn += 1
                        elif event.key == K_4 and self.table[1][0] != 0:
                            print('Esta casilla esta ocupada, prueba con otra')

                        if event.key == K_5 and self.table[1][1] == 0:
                            self.table = self.player.movePlayer(self.table, turn, 5)
                            turn += 1
                        elif event.key == K_5 and self.table[1][1] != 0:
                            print('Esta casilla esta ocupada, prueba con otra')

                        if event.key == K_6 and self.table[1][2] == 0:
                            self.table = self.player.movePlayer(self.table, turn, 6)
                            turn += 1
                        elif event.key == K_6 and self.table[1][2] != 0:
                            print('Esta casilla esta ocupada, prueba con otra')

                        if event.key == K_7 and self.table[2][0] == 0:
                            self.table = self.player.movePlayer(self.table, turn, 7)
                            turn += 1
                        elif event.key == K_7 and self.table[2][0] != 0:
                            print('Esta casilla esta ocupada, prueba con otra')

                        if event.key == K_8 and self.table[2][1] == 0:
                            self.table = self.player.movePlayer(self.table, turn, 8)
                            turn += 1
                        elif event.key == K_8 and self.table[2][1] != 0:
                            print('Esta casilla esta ocupada, prueba con otra')
                            
                        if event.key == K_9 and self.table[2][2] == 0:
                            self.table = self.player.movePlayer(self.table, turn, 9)
                            turn += 1
                        elif event.key == K_9 and self.table[2][2] != 0:
                            print('Esta casilla esta ocupada, prueba con otra')

                    if event.key == K_ESCAPE:
                        run = False

                if event.type == QUIT:
                    run = False

            if turn % 2 == 1 and len(self.emptyCells(self.table)) != 0:
                        index = self.minimax(self.table, 0, True)
                        self.table = self.player.movePlayer(self.table, turn, index)
                        turn += 1

            if finished_game == False:
                if self.checkGameisOver(self.table) == 1 or self.checkGameisOver(self.table) == 2:
                    print(f'Ha ganado el jugador {self.checkGameisOver(self.table)}')
                    finished_game = True
                elif self.checkGameisOver(self.table) == 0:
                    print('Empate')
                    finished_game = True

            pygame.display.flip()

game = Game()
game.run()

