import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize Profit", pulp.LpMaximize)

# Визначення змінних
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruit', lowBound=0, cat='Integer')

# Додавання обмежень
model += 2 * lemonade + 1 * fruit_juice <= 100 # Обмеження води
model += 1 * lemonade <= 50 # Обмеження цукру
model += 1 * lemonade <= 30 # Обмеження лимонного соку
model += 2 * fruit_juice <= 40 # Обмеження фруктового пюре

# Функція цілі
model += lemonade + fruit_juice, "Profit"

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Виробляти лимонаду:", lemonade.varValue)
print("Виробляти фруктового соку:", fruit_juice.varValue)
