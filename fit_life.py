# ============================================================
# КОНСТАНТЫ
# ============================================================

WATER_ML_PER_KG = 30       # Норма воды: мл на 1 кг веса
ML_PER_LITER = 1000        # Пересчёт мл -> литры

AGE_MIN, AGE_MAX = 18, 120
WEIGHT_MIN, WEIGHT_MAX = 30.0, 300.0
HEIGHT_MIN, HEIGHT_MAX = 0.5, 2.5

AGE_RANGE = f'от {AGE_MIN} до {AGE_MAX}'
WEIGHT_RANGE = f'от {WEIGHT_MIN:g} до {WEIGHT_MAX:g}'
HEIGHT_RANGE = f'от {HEIGHT_MIN:g} до {HEIGHT_MAX:g}'

BMI_CATEGORIES = (
    (16.0, 'выраженный дефицит массы тела'),
    (18.5, 'недостаточная масса тела'),
    (25.0, 'норма'),
    (30.0, 'избыточная масса тела (предожирение)'),
    (35.0, 'ожирение I степени'),
    (40.0, 'ожирение II степени'),
)
BMI_LAST_CATEGORY = 'ожирение III степени'


# ============================================================
# ОСНОВНОЙ СЦЕНАРИЙ
# ============================================================

print('\nДОБРО ПОЖАЛОВАТЬ В FITLIFE!\n')

# Имя
user_name = input('Введите ваше имя: ').strip().title()
if not user_name:
    user_name = 'Гость'
print(f'Приятно познакомиться, {user_name}!\n')

# Возраст
while True:
    try:
        user_age = int(input(f'Введите ваш возраст ({AGE_RANGE}): ').strip())
    except ValueError:
        print('Ошибка: нужно ввести целое число.')
        continue
    if not (AGE_MIN <= user_age <= AGE_MAX):
        print(f'Ошибка: возраст должен быть в диапазоне {AGE_RANGE}.')
        continue
    break

# Вес
while True:
    try:
        user_weight = float(
            input(f'Введите ваш вес (в кг, {WEIGHT_RANGE}): ').strip())
    except ValueError:
        print('Ошибка: нужно ввести число.')
        continue
    if not (WEIGHT_MIN <= user_weight <= WEIGHT_MAX):
        print(f'Ошибка: вес должен быть в диапазоне {WEIGHT_RANGE} кг.')
        continue
    break

# Рост
while True:
    try:
        user_height = float(
            input(f'Введите ваш рост (в метрах, {HEIGHT_RANGE}): ').strip())
    except ValueError:
        print('Ошибка: нужно ввести число.')
        continue
    if not (HEIGHT_MIN <= user_height <= HEIGHT_MAX):
        print(f'Ошибка: рост должен быть в диапазоне {HEIGHT_RANGE} м.')
        continue
    break

# Расчёты ИМТ и ежедневной нормы воды
bmi_raw = user_weight / user_height ** 2
bmi = round(bmi_raw, 1)
water_needed = round(user_weight * WATER_ML_PER_KG / ML_PER_LITER, 2)

# Определение категории ИМТ
bmi_category = BMI_LAST_CATEGORY
for threshold, category in BMI_CATEGORIES:
    if bmi_raw < threshold:
        bmi_category = category
        break

# Склонение «год/года/лет»
if user_age % 100 in (11, 12, 13, 14):
    age_word = 'лет'
elif user_age % 10 == 1:
    age_word = 'год'
elif user_age % 10 in (2, 3, 4):
    age_word = 'года'
else:
    age_word = 'лет'

# Вывод результатов
print('\nВАШ ПРОФИЛЬ FITLIFE\n')
print(f'Имя:        {user_name}')
print(f'Возраст:    {user_age} {age_word}')
print(f'Вес:        {user_weight:.2f} кг')
print(f'Рост:       {user_height:.2f} м')
print(f'ИМТ:        {bmi} ({bmi_category})')
print(f'Норма воды: {water_needed} л в день')
print('\nРасчет окончен. Будьте здоровы!\n')
