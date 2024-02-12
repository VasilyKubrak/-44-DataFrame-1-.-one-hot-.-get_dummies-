import pandas as pd

# Создаем DataFrame
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

# Кодируем в one hot вид
dummies = pd.get_dummies(data['whoAmI'])

# Объединяем исходный DataFrame и кодированный
data = pd.concat([data, dummies], axis=1)

# Удаляем исходный столбец
data = data.drop('whoAmI', axis=1)

# Выводим результат
data.head()
