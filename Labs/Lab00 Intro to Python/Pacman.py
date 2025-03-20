class Player:
    def __init__(self):
        self.pacman_x = 0
        self.pacman_y = 0

    def move(self, position):
        self.pacman_x = list(position)[0]
        self.pacman_x = list(position)[1]


class Game:
    def __init__(self, n, m, matrix):
        self.n = n
        self.m = m
        self.matrix = matrix


class Pacman:
    def __init__(self, n, m, matrix):
        self.player = Player()
        self.game = Game(n, m, matrix)

    def play_game(self):
        pass


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    matrix = [list(input()) for _ in range(n)]
    print(matrix)
