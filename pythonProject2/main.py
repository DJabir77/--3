import random  # Импортируем модуль random для генерации случайных чисел.

class SuperNim:  # Определяем класс SuperNim для игры.
    def __init__(self, rows, cols):  # Конструктор класса, принимает количество строк и столбцов.
        self.rows = rows  # Сохраняем количество строк.
        self.cols = cols  # Сохраняем количество столбцов.
        self.board = self.generate_board()  # Генерируем игровое поле.
        self.current_player = 1  # Инициализируем первого игрока.

    def generate_board(self):  # Метод для создания игрового поля.
        # Генерация двумерного списка (матрицы) случайных чисел от 0 до 3.
        return [[random.randint(0, 3) for _ in range(self.cols)] for _ in range(self.rows)]

    def display_board(self):  # Метод для отображения текущего состояния игрового поля.
        print("Игровое поле:")  # Заголовок для поля.
        print("   " + " ".join(str(i) for i in range(self.cols)))  # Выводим горизонтальную нумерацию.
        for idx, row in enumerate(self.board):  # Итерируемся по каждой строке игрового поля.
            print(f"{idx} | " + " ".join(str(x) for x in row))  # Выводим индекс строки и ее содержимое.
        print()  # Пустая строка для читаемости.

    def is_game_over(self):  # Метод для проверки, закончилась ли игра.
        # Проверяем, есть ли хотя бы одна фишка на поле.
        return all(cell == 0 for row in self.board for cell in row)

    def count_tokens(self, row, col):  # Метод для подсчета фишек в выбранной строке и столбце.
        row_tokens = sum(self.board[row])  # Суммируем фишки в выбранной строке.
        col_tokens = sum(self.board[r][col] for r in range(self.rows))  # Суммируем фишки в выбранном столбце.
        return row_tokens, col_tokens  # Возвращаем количество фишек в строке и столбце.

    def make_move(self, row, col):  # Метод для выполнения хода.
        if self.board[row][col] > 0:  # Проверяем, есть ли фишки в выбранной клетке.
            # Убираем фишки из выбранной строки.
            for c in range(self.cols):
                self.board[row][c] = 0  # Устанавливаем значение 0 для каждой клетки в строке.
            # Убираем фишки из выбранного столбца.
            for r in range(self.rows):
                self.board[r][col] = 0  # Устанавливаем значение 0 для каждой клетки в столбце.
            return True  # Возвращаем True, если ход был успешным.
        else:
            print("Невозможно сделать ход! В этой клетке нет фишек.")  # Сообщаем, что ход невозможен.
            return False  # Возвращаем False, если ход не был выполнен.

    def switch_player(self):  # Метод для переключения между игроками.
        # Меняем текущего игрока: если 1, то 2, и наоборот.
        self.current_player = 1 if self.current_player == 2 else 2

    def play(self):  # Метод для управления игровым процессом.
        while not self.is_game_over():  # Цикл продолжается, пока игра не закончилась.
            self.display_board()  # Отображаем текущее состояние игрового поля.
            print(f"Игрок {self.current_player}, сделайте ход (введите строку и столбец): ")
            while True:  # Запускаем цикл для получения корректного ввода.
                try:
                    row, col = map(int, input().split())  # Пытаемся получить координаты от пользователя.
                    if 0 <= row < self.rows and 0 <= col < self.cols:  # Проверяем, находятся ли координаты в допустимом диапазоне.
                        row_tokens, col_tokens = self.count_tokens(row, col)  # Подсчитываем фишки в строке и столбце.
                        if row_tokens > 0 or col_tokens > 0:  # Проверяем, есть ли фишки в строке или столбце.
                            if self.make_move(row, col):  # Пытаемся сделать ход.
                                break  # Если ход успешен, выходим из цикла.
                        else:
                            print("В выбранной строке и столбце нет фишек. Попробуйте снова.")  # Если фишек нет, просим попробовать снова.
                    else:
                        print("Некорректные координаты. Попробуйте еще раз.")  # Если координаты некорректны, сообщаем об ошибке.
                except ValueError:  # Обрабатываем случай, если введены некорректные данные.
                    print("Пожалуйста, введите два целых числа (строка и столбец).")

            if self.is_game_over():  # Проверяем, закончилась ли игра после хода.
                print(f"Игрок {self.current_player} выиграл!")  # Объявляем победителя.
                self.display_board()  # Отображаем финальное состояние игрового поля.
                break  # Выходим из основного цикла.

if __name__ == "__main__":  # Проверяем, является ли этот файл основным.
    game = SuperNim(5, 5)  # Создаем объект игры с полем 5x5.
    game.play()  # Запускаем игру.
