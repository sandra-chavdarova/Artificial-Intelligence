"""

"""

from searching_framework import *


class Football(Problem):
    def __init__(self, initial, opponents, goal):
        super().__init__(initial, goal)
        self.opponents = opponents

    def successor(self, state):
        # state = ((player_x, player_y), (ball_x, ball_y))
        successors = dict()
        player_x, player_y = state[0]
        ball_x, ball_y = state[1]

        new_state = ((player_x, player_y + 1), (ball_x, ball_y))
        if self.check_valid(new_state, self.opponents):
            successors["Pomesti coveche gore"] = new_state
        new_state = ((player_x, player_y - 1), (ball_x, ball_y))
        if self.check_valid(new_state, self.opponents):
            successors["Pomesti coveche dolu"] = new_state
        new_state = ((player_x + 1, player_y), (ball_x, ball_y))
        if self.check_valid(new_state, self.opponents):
            successors["Pomesti coveche desno"] = new_state
        new_state = ((player_x + 1, player_y + 1), (ball_x, ball_y))
        if self.check_valid(new_state, self.opponents):
            successors["Pomesti coveche gore-desno"] = new_state
        new_state = ((player_x + 1, player_y - 1), (ball_x, ball_y))
        if self.check_valid(new_state, self.opponents):
            successors["Pomesti coveche dolu-desno"] = new_state

        new_state = ((player_x, player_y + 1), (ball_x, ball_y + 1))
        if self.check_valid(new_state, self.opponents) and player_x == ball_x and player_y == ball_y - 1:
            successors["Turni topka gore"] = new_state
        new_state = ((player_x, player_y - 1), (ball_x, ball_y - 1))
        if self.check_valid(new_state, self.opponents) and player_x == ball_x and player_y - 1 == ball_y:
            successors["Turni topka dolu"] = new_state
        new_state = ((player_x + 1, player_y), (ball_x + 1, ball_y))
        if self.check_valid(new_state, self.opponents) and player_x == ball_x - 1 and player_y == ball_y:
            successors["Turni topka desno"] = new_state
        new_state = ((player_x + 1, player_y + 1), (ball_x + 1, ball_y + 1))
        if self.check_valid(new_state, self.opponents) and player_x == ball_x - 1 and player_y == ball_y - 1:
            successors["Turni topka gore-desno"] = new_state
        new_state = ((player_x + 1, player_y - 1), (ball_x + 1, ball_y - 1))
        if self.check_valid(new_state, self.opponents) and player_x == ball_x - 1 and player_y - 1 == ball_y:
            successors["Turni topka dolu-desno"] = new_state

        return successors

    @staticmethod
    def check_valid(state, opponents):
        player_x, player_y = state[0]
        ball_x, ball_y = state[1]
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
        invalid = []
        for d in directions:
            for opponent in opponents:
                invalid.append((opponent[0] + d[0], opponent[1] + d[1]))
        invalid.append(opponents[0])
        invalid.append(opponents[1])
        invalid = tuple(invalid)
        return (0 <= player_x < 8 and 0 <= player_y < 6 and 0 <= ball_x < 8 and 0 <= ball_y < 6) and \
            (ball_x, ball_y) not in invalid \
            and (player_x, player_y) != (ball_x, ball_y) and \
            (player_x, player_y) not in opponents

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        position = state[1]
        return position in self.goal


if __name__ == '__main__':
    info = input().split(",")
    player = (int(info[0]), int(info[1]))
    info = input().split(",")
    ball = (int(info[0]), int(info[1]))
    goal = ((7, 2), (7, 3))
    opponents = ((3, 3), (5, 4))
    initial_state = (player, ball)
    game = Football(initial_state, opponents, goal)
    result = breadth_first_graph_search(game)
    if result is not None:
        print(result.solution())
    else:
        print("No Solution!")
