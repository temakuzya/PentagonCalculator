import math
import os


def calculate_perimeter(side):
    return 5 * side


# расчёт периметра пятиугольника


def calculate_area(side):
    return (5 * side**2) / (4 * math.tan(math.pi / 5))


# расчёт площади пятиугольника


def main():
    while True:
        print("Нахождение площади и периметра правильного пятиугольника")
        print("1 - Ввод через консоль")
        print("2 - Ввод через файл")
        print("0 - ВЫХОД")

        choice = input("Выберите способ ввода: ")

        if choice == "0":  # выход из программы
            print("Программа завершена")
            exit()

        elif choice == "1":  # консольный ввод данных
            try:
                side = float(input("Введите длину стороны: "))
                if side < 0:
                    print("Сторона должна быть положительным числом!")
                    continue
                else:
                    perimeter = calculate_perimeter(side)
                    area = calculate_area(side)

                    print("\nРезультаты: ")
                    print("Периметр = ", round(perimeter, 2))
                    print("Площадь = ", round(area, 2))
            except:
                print("Ошибка ввода!")

        elif choice == "2":  # ввод данных из файла
            filename = "input.txt"

            file = open(filename, "w")
            file.close()

            print("\nФайл input.txt создан.")
            print("Введите число и сохраните файл")
            print("После сохранения вернитесь в программу")

            os.startfile(filename)
            input("Нажмите Enter после того как заполните файл...")
            try:
                file = open(filename, "r")
                content = file.read().strip()
                file.close()

                side = float(content)

                if side <= 0:
                    print("Сторона должна быть положительным числом!")
                    return
                else:
                    perimeter = calculate_perimeter(side)
                    area = calculate_area(side)

                    print("\nРезультаты: ")
                    print("Периметр = ", round(perimeter, 2))
                    print("Площадь = ", round(area, 2))

            except:
                print("В файле должно быть число")

        else:
            print("Неверный выбор :( ")


main()
