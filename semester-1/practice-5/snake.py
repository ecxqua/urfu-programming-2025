from random import choice, randint

import pygame

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Цвет яблока
APPLE_COLOR = (255, 0, 0)

# Цвет змейки
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки:
SPEED = 20

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption('Змейка')

# Настройка времени:
clock = pygame.time.Clock()


def handle_keys(game_object):
    """Обработка нажатий клавиш и событий выхода из игры.

    Args:
        game_object: Объект змейки для изменения направления движения.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
            elif event.key == pygame.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT


class GameObject:
    """Базовый класс для игровых объектов.

    Attributes:
        position: Текущая позиция объекта на экране.
        body_color: Цвет объекта (кортеж RGB).
    """

    def __init__(self, position=(0, 0), body_color=(255, 255, 255)):
        """Инициализация игрового объекта.

        Args:
            position: Кортеж (x, y) начальной позиции объекта.
            body_color: Кортеж (R, G, B) цвета объекта.
        """
        self.position = position
        self.body_color = body_color

    def draw(self):
        """Отрисовка объекта на экране."""
        pass


class Apple(GameObject):
    """Класс, представляющий яблоко в игре.

    Яблоко появляется в случайной позиции сетки и может быть съедено змейкой.
    """

    def __init__(self, body_color=APPLE_COLOR):
        """Инициализация яблока с случайной позицией.

        Args:
            body_color: Цвет яблока (по умолчанию APPLE_COLOR).
        """
        position = self.randomize_position()
        super().__init__(position, body_color)

    def randomize_position(self):
        """Установить яблоко в случайную позицию на сетке.

        Returns:
            Кортеж (x, y) новой позиции яблока.
        """
        self.position = (randint(0, GRID_WIDTH - 1) * GRID_SIZE,
                         randint(0, GRID_HEIGHT - 1) * GRID_SIZE)
        return self.position

    def draw(self):
        """Отрисовать яблоко на экране."""
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Snake(GameObject):
    """Класс, представляющий змейку в игре.

    Змейка может двигаться в четыре направления, расти при поедании яблок
    и сбрасываться при столкновении с собой.

    Attributes:
        center_position: Начальная позиция центра змейки.
        length: Текущая длина змейки.
        positions: Список позиций всех сегментов змейки.
        direction: Текущее направление движения.
        next_direction: Следующее направление (установлено клавишей).
        last: Позиция последнего сегмента (для затирания).
    """

    def __init__(self, body_color=SNAKE_COLOR):
        """Инициализация змейки в центре экрана.

        Args:
            body_color: Цвет змейки (по умолчанию SNAKE_COLOR).
        """
        self.center_position = ((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))
        super().__init__(self.center_position, body_color)
        self.length = 1
        self.positions = [self.center_position]
        self.direction = RIGHT
        self.next_direction = None
        self.last = None

    def move(self, apple=None):
        """Переместить змейку на один шаг в текущем направлении.

        Проверяет столкновение с самой собой, поедание яблока и
        управляет длиной.

        Args:
            apple: Объект яблока для проверки столкновения (опционально).
        """
        head = self.get_head_position()
        current_head_position = (
            (head[0] + self.direction[0] * GRID_SIZE) % SCREEN_WIDTH,
            (head[1] + self.direction[1] * GRID_SIZE) % SCREEN_HEIGHT)

        if current_head_position in self.positions[1:]:
            self.reset()
        else:
            self.positions.insert(0, current_head_position)

            # ПРОВЕРКА ЯБЛОКА ДО УДАЛЕНИЯ ХВОСТА
            if apple and current_head_position == apple.position:
                self.length += 1
                apple.randomize_position()

            # УДАЛЕНИЕ ХВОСТА ПОСЛЕ ПРОВЕРКИ ЯБЛОКА
            if len(self.positions) > self.length:
                self.last = self.positions.pop()  # сохраняем для затирания
            else:
                self.last = None

    def reset(self):
        """Сбросить змейку в начальное состояние.

        Вызывается при столкновении со своим телом.
        Змейка возвращается в центр с длиной 1 и случайным направлением.
        """
        self.length = 1
        self.positions = [self.center_position]
        self.direction = choice([UP, DOWN, LEFT, RIGHT])

    def get_head_position(self):
        """Получить текущую позицию головы змейки.

        Returns:
            Кортеж (x, y) позиции головы.
        """
        return self.positions[0]

    def update_direction(self):
        """Обновить текущее направление на основе нажатой клавиши.

        Применяет next_direction к текущему направлению движения
        змейки.
        """
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def draw(self):
        """Отрисовать змейку и затереть последний сегмент."""
        for position in self.positions[:-1]:
            rect = (pygame.Rect(position, (GRID_SIZE, GRID_SIZE)))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

        # Отрисовка головы змейки
        head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, head_rect)
        pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)

        # Затирание последнего сегмента
        if self.last:
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)


def main():
    """Главная функция игры.

    Инициализирует PyGame, создает объекты игры (змейку и яблоко),
    запускает основной игровой цикл с обработкой событий и отрисовкой.
    """
    # Инициализация PyGame:
    pygame.init()
    # Тут нужно создать экземпляры классов.
    apple = Apple()
    snake = Snake()

    while True:
        clock.tick(SPEED)

        # Тут опишите основную логику игры.
        handle_keys(snake)
        snake.update_direction()
        snake.move(apple)
        # Отрисовка
        screen.fill(BOARD_BACKGROUND_COLOR)  # очистка экрана
        apple.draw()
        snake.draw()
        pygame.display.update()  # обновление экрана


if __name__ == '__main__':
    main()
