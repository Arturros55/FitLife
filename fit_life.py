# КОНСТАНТЫ
LINE = '=' * 56          # Длина разделителей
THIN = '-' * 56          # Длина тонких разделителей
WATER_PER_KG = 30        # Норма воды: мл на 1 кг веса

print(LINE)
print('ДОБРО ПОЖАЛОВАТЬ В FITLIFE!'.center(56))
print(LINE)
print()

# Знакомство
user_name = input('Введите ваше имя: ').strip().title()
if not user_name:
    user_name = 'Гость'
print(f'Приятно познакомиться, {user_name}!\n')
print(THIN)

# Возраст
while True:
    try:
        user_age = int(input('Введите ваш возраст (от 1 до 120): ').strip())
    except ValueError:
        print('Ошибка: нужно ввести целое число.')
        continue

    if not (1 <= user_age <= 120):
        print('Ошибка: возраст должен быть в диапазоне от 1 до 120.')
        continue

    break

# Вес
while True:
    try:
        user_weight = float(
            input('Введите ваш вес (в кг, от 5 до 400): ').strip())
    except ValueError:
        print('Ошибка: нужно ввести число.')
        continue

    if not (5 <= user_weight <= 400):
        print('Ошибка: вес должен быть в диапазоне от 5 до 400 кг.')
        continue

    break

# Рост
while True:
    try:
        user_height = float(
            input('Введите ваш рост (в метрах, от 0.5 до 2.5): ').strip())
    except ValueError:
        print('Ошибка: нужно ввести число.')
        continue

    if not (0.5 <= user_height <= 2.5):
        print('Ошибка: рост должен быть в диапазоне от 0.5 до 2.5 м.')
        continue

    break

# Рассчётные формулы для индекса массы тела и ежедневной нормы воды
bmi = round(user_weight / user_height ** 2, 1)
water_needed = user_weight * WATER_PER_KG / 1000

# Слово «год/года/лет» в правильной форме
if user_age % 100 in (11, 12, 13, 14):
    age_word = 'лет'
elif user_age % 10 == 1:
    age_word = 'год'
elif user_age % 10 in (2, 3, 4):
    age_word = 'года'
else:
    age_word = 'лет'

# Интерпретация ИМТ
if bmi < 18.5:
    bmi_category = 'недостаточный вес'
elif bmi < 25:
    bmi_category = 'норма'
elif bmi < 30:
    bmi_category = 'избыточный вес'
else:
    bmi_category = 'ожирение'

print()
print(LINE)
print('ВАШ ПРОФИЛЬ FITLIFE'.center(56))
print(LINE)
print(f'Имя:       {user_name}')
print(f'Возраст:   {user_age} {age_word}')
print(f'Вес:       {user_weight} кг')
print(f'Рост:      {user_height} м')
print(THIN)
print(f'ИМТ:        {bmi} ({bmi_category})')
print(f'Норма воды: {water_needed} л в день')
print(LINE)
print('Расчет окончен. Будьте здоровы!\n')
