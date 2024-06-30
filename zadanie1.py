class Runner(object):

    def eval(self, string):

        start, goal, days = map(float, string.split())

        current_distance = start
        for day in range(int(days)):
            if current_distance >= goal:
                return True
            current_distance *= 1.1  # Увеличиваем текущую дистанцию на 10%

        return current_distance >= goal  # После завершения всех дней

    def loop(self):
        line = input()
        value = self.eval(line)
        print(value)

if __name__ == '__main__':
    # Для тестирования заменяем путь ввода
    calc = Runner()
    input_test = "4 15 30"  # Здесь вы можете изменить строку для тестирования
    result = calc.eval(input_test)
    print(result)