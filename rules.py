import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Создаем нечеткие переменные
speed = ctrl.Antecedent(np.arange(0, 101, 1), 'speed')  # Скорость автомобиля от 0 до 100 км/ч
distance = ctrl.Antecedent(np.arange(0, 101, 1), 'distance')  # Расстояние до препятствия в метрах
action = ctrl.Consequent(np.arange(0, 101, 1), 'action')  # Управляющее воздействие (например, торможение) от 0 до 100%

# Определение функций принадлежности для скорости и расстояния
speed['slow'] = fuzz.trimf(speed.universe, [0, 0, 50])
speed['medium'] = fuzz.trimf(speed.universe, [0, 50, 100])
speed['fast'] = fuzz.trimf(speed.universe, [50, 100, 100])

distance['close'] = fuzz.trimf(distance.universe, [0, 0, 50])
distance['medium'] = fuzz.trimf(distance.universe, [0, 50, 100])
distance['far'] = fuzz.trimf(distance.universe, [50, 100, 100])

# Определение функций принадлежности для управляющего воздействия
action['brake'] = fuzz.trimf(action.universe, [0, 0, 50])
action['keep_speed'] = fuzz.trimf(action.universe, [0, 50, 100])
action['accelerate'] = fuzz.trimf(action.universe, [50, 100, 100])

# Правила нечеткой логики
rule1 = ctrl.Rule(speed['slow'] & distance['close'], action['brake'])
rule2 = ctrl.Rule(speed['medium'] & distance['close'], action['brake'])
rule3 = ctrl.Rule(speed['fast'] & distance['close'], action['brake'])
rule4 = ctrl.Rule(speed['slow'] & distance['medium'], action['keep_speed'])
rule5 = ctrl.Rule(speed['medium'] & distance['medium'], action['keep_speed'])
rule6 = ctrl.Rule(speed['fast'] & distance['medium'], action['brake'])
rule7 = ctrl.Rule(speed['slow'] & distance['far'], action['accelerate'])
rule8 = ctrl.Rule(speed['medium'] & distance['far'], action['accelerate'])
rule9 = ctrl.Rule(speed['fast'] & distance['far'], action['accelerate'])

# Создаем систему управления
system = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
controller = ctrl.ControlSystemSimulation(system)

print_actions = ['Лучше затормозить', 'Снизьте скорость','Стоит повернуть',
                 'Можно ехать с прежней скоростью','Лучше увеличить скорость']
