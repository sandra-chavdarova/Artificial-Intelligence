"""
Да се дефинира класа за Агент кој ја чува својата позиција (координати x и y) во некој простор.
Да се дефинира метод кој го означува движењето на агентот во просторот.
Потоа да се дефинираат агенти кои имплементираат специфично движење (лево, десно, горе, долу).
Извршете 5 движења за секој од агентите и испечатете ја позицијата на агентот во секој чекор.
"""


class Agent:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Position: ({self.x}, {self.y})'

    def move(self):
        pass


class LeftAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.x -= 1


class RightAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.x += 1


class UpAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.y += 1


class DownAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.y -= 1


if __name__ == '__main__':
    left = LeftAgent(3, 4)
    print(left)
    for i in range(5):
        left.move()
        print(f'Step: {i}, {left}')

    right = RightAgent(-2, 3)
    print(right)
    for i in range(5):
        right.move()
        print(f'Step: {i}, {right}')

    up = UpAgent(-2, -3)
    print(up)
    for i in range(5):
        up.move()
        print(f'Step: {i}, {up}')

    down = DownAgent(2, 3)
    print(down)
    for i in range(5):
        down.move()
        print(f'Step: {i}, {down}')
