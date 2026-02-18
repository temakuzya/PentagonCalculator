# Pentagon Calculator

## English version

### 🧮 Description
A console application for calculating the **perimeter** and **area** of a regular pentagon.

This program calculates geometric parameters of a regular pentagon based on the side length entered by the user.  
It supports two input modes: manual input from the keyboard and reading data from a text file.

---

### ⚙️ Features

- Calculate perimeter of a regular pentagon:  
  **P = 5 · a**
- Calculate area of a regular pentagon:  
  **S = (5 · a²) / (4 · tan(π / 5))**
- Two input modes:
  - Console input (keyboard)
  - File input (via `input.txt`)
- Automatic file creation and opening
- Input validation and error handling
- Results rounded to 2 decimal places

---

### 💻 Requirements

- Python **3.8** or higher  
- Windows OS (for automatic file opening)

---

### 🚀 Installation & Running

1. Clone or download this repository  
2. Make sure Python is installed:

```bash
python --version
```

3. Run the program:

```bash
python PentagonCalculator.py
```

---

### 📖 Usage Guide

#### Main Menu

```
Finding the area and perimeter of a regular pentagon
1 - Input via console
2 - Input via file
0 - EXIT
Select input method:
```

#### Console Input Mode (Option 1)

- Enter **1** and press Enter  
- Enter the side length (use a dot for decimals, e.g., `5.5`)  
- The program will display the results:

```
Results:
Perimeter = 27.50
Area = 52.04
```

#### File Input Mode (Option 2)

- Enter **2** and press Enter  
- The file `input.txt` will be created and opened automatically  
- Enter a number in the file and save it (**Ctrl+S**)  
- Close Notepad, return to the console and press Enter  
- The program will read the file and display results

#### Exit

Enter **0** in the main menu to exit the program.

---

### ⚠️ Error Messages

| Message | Meaning |
|----------|----------|
| Input error! | Non-numeric value entered |
| The side must be a positive number! | Value ≤ 0 entered |
| The file must contain a number | File contains non-numeric data |
| The file must contain a number | `input.txt` is empty |
| Invalid choice :( | Invalid menu option selected |

---

### 🧪 Examples

#### Console Input

```
Select input method: 1
Enter the side length: 3

Results:
Perimeter = 15.00
Area = 15.48
```

#### File Input

```
Select input method: 2

File input.txt created.
Press Enter after you have filled the file...

Results:
Perimeter = 25.00
Area = 43.01
```

---

### Project Structure

```
.
├── PentagonCalculator.py  # Main program file
├── input.txt              # Input data file (created automatically)
└── README.md              # Documentation file
```

---

### 🧹 Code Style

The code follows **PEP 8** standards and is formatted using **Black**.

---

### 👤 Author

**A.A. Kuzmin**  
Year: 2026  
Institution: KGB POU HPET
Contaсts: temakuzya.khv27@gmail.com
---

---

# Калькулятор пентагона

## Русская версия

### 🧮 Описание

Консольное приложение для вычисления **периметра** и **площади** правильного пятиугольника.

Программа рассчитывает геометрические параметры правильного пятиугольника по заданной длине стороны.  
Поддерживает два режима ввода: с клавиатуры и из файла.

---

### ⚙️ Возможности

- Вычисление периметра:  
  **P = 5 · a**
- Вычисление площади:  
  **S = (5 · a²) / (4 · tan(π / 5))**
- Два режима ввода:
  - Ввод с консоли (клавиатуры)
  - Ввод из файла (`input.txt`)
- Автоматическое создание и открытие файла
- Проверка корректности ввода и обработка ошибок
- Округление результатов до 2 знаков

---

### 💻 Требования

- Python **3.8** или выше  
- ОС Windows (для автоматического открытия файла)

---

### 🚀 Установка и запуск

1. Скачайте репозиторий  
2. Проверьте установку Python:

```bash
python --version
```

3. Запустите программу:

```bash
python PentagonCalculator.py
```

---

### 📖 Как пользоваться

#### Главное меню

```
Нахождение площади и периметра правильного пятиугольника
1 - Ввод через консоль
2 - Ввод через файл
0 - ВЫХОД
Выберите способ ввода:
```

#### Ввод с консоли (пункт 1)

- Введите **1** и нажмите Enter  
- Введите длину стороны (например, `5.5`)  
- Программа выведет результаты:

```
Результаты:
Периметр = 27.50
Площадь = 52.04
```

#### Ввод через файл (пункт 2)

- Введите **2** и нажмите Enter  
- Файл `input.txt` создастся и откроется автоматически  
- Введите число в файл и сохраните (**Ctrl+S**)  
- Закройте Блокнот, вернитесь в консоль и нажмите Enter  
- Программа прочитает файл и выведет результаты

#### Выход

Введите **0** в главном меню.

---

### ⚠️ Сообщения об ошибках

| Сообщение | Значение |
|------------|-----------|
| Ошибка ввода! | Введено не число |
| Сторона должна быть положительным числом! | Число ≤ 0 |
| В файле должно быть число | В файле не число |
| В файле должно быть число | Файл `input.txt` пуст |
| Неверный выбор :( | Неверный пункт меню |

---

### 🧪 Примеры

#### Консольный ввод

```
Выберите способ ввода: 1
Введите длину стороны: 3

Результаты:
Периметр = 15.00
Площадь = 15.48
```

#### Файловый ввод

```
Выберите способ ввода: 2

Файл input.txt создан.
Нажмите Enter после того как заполните файл...

Результаты:
Периметр = 25.00
Площадь = 43.01
```

---

###  Структура проекта

```
.
├── PentogonCalculator.py  # Основной файл программы
├── input.txt              # Файл для ввода данных
└── README.md              # Документация
```

---

### 🧹 Стиль кода

Код соответствует стандарту **PEP 8** и отформатирован с помощью **Black**.

---

### 👤 Автор

**А.А. Кузьмин**  
Год: 2026  
Учреждение: КГБ ПОУ ХПЭТ
Контакты: temakuzya.khv27@gmail.com
