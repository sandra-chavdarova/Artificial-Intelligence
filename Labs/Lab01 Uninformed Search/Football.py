"""
Дадена е табла 8x6, каде што се поставени човече и топка.
Потребно е човечето со туркање на топката да ја доведе до голот кој е обележан со сива боја.
На таблата дополнително има противници кои се обележани со сина боја.
Противниците се статични и не се движат.

Човечето може да се движи во пет насоки: горе, долу, десно, горе-десно и долу-десно за една позиција.
При движењето, доколку пред него се наоѓа топката, може да ја турне топката во насоката во која се движи.
Човечето не може да се наоѓа на истото поле како топката или некој од противниците.
Топката исто така не може да се наоѓа на поле кое е соседно со некој од противниците
(хоризнотално, вертикално или дијагонално) или на исто поле со некој од противниците.

На сликата е покажана една можна почетна состојба на таблата.

За сите тест примери големината на таблата е иста, а позицијата на човечето и топката се менуваат
и се читаат од стандарден влез. Позицијата на противниците и голот е иста за сите тест примери.
Ваша задача е да го имплементирате поместувањето на човечето (со тоа и туркањето на топката) во successor функцијата.
Акциите се именуваат како „Pomesti coveche gore/dolu/desno/gore-desno/dolu-desno“ ако се поместува човечето,
или како „Turni topka gore/dolu/desno/gore-desno/dolu-desno“ ако при поместувањето на чoвечето се турнува и топката.
Дополнително, потребно е да проверите дали сте стигнале до целта, односно да ја имплементирате функцијата goal_test
и да проверите дали состојбата е валидна, односно да ја дополните функцијата check_valid.
Треба да примените неинформирано пребарување за да најдете решение со најмал број на чекори.

Input:
0,1
1,2

Result:
['Pomesti coveche gore', 'Pomesti coveche gore', 'Turni topka dolu-desno', 'Pomesti coveche dolu', 'Turni topka desno', 'Turni topka desno', 'Turni topka desno', 'Pomesti coveche dolu', 'Turni topka gore-desno', 'Turni topka gore-desno']
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
