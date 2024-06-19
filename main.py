import numpy as np
import skfuzzy as fuzz
from skfuzzy import control

temp = control.Antecedent(np.arange(-40, 40, 1), 'temp')
time = control.Antecedent(np.arange(0, 24, 1), 'time')
clothes = control.Consequent(np.arange(0, 100, 1), 'clothes')

temp.automf(5, names=['Мороз', 'Прохладно', 'Средняя', 'Теплая', 'Жаркая'])
time.automf(3, names=['Рано', 'Полдень', 'Поздно'])
clothes.automf(5, names=['Легкая', 'Средне_легкая', 'Утепленная', 'Теплая', 'Очень_теплая'])

rule1 = control.Rule(temp['Мороз'] & time['Рано'], clothes['Очень_теплая'])
rule2 = control.Rule(temp['Мороз'] & time['Полдень'], clothes['Очень_теплая'])
rule3 = control.Rule(temp['Мороз'] & time['Поздно'], clothes['Очень_теплая'])

rule4 = control.Rule(temp['Прохладно'] & time['Рано'], clothes['Очень_теплая'])
rule5 = control.Rule(temp['Прохладно'] & time['Полдень'], clothes['Теплая'])
rule6 = control.Rule(temp['Прохладно'] & time['Поздно'], clothes['Очень_теплая'])

rule7 = control.Rule(temp['Средняя'] & time['Рано'], clothes['Теплая'])
rule8 = control.Rule(temp['Средняя'] & time['Полдень'], clothes['Утепленная'])
rule9 = control.Rule(temp['Средняя'] & time['Поздно'], clothes['Теплая'])

rule10 = control.Rule(temp['Теплая'] & time['Рано'], clothes['Средне_легкая'])
rule11 = control.Rule(temp['Теплая'] & time['Полдень'], clothes['Легкая'])
rule12 = control.Rule(temp['Теплая'] & time['Поздно'], clothes['Средне_легкая'])

rule13 = control.Rule(temp['Жаркая'] & time['Рано'], clothes['Легкая'])
rule14 = control.Rule(temp['Жаркая'] & time['Полдень'], clothes['Легкая'])
rule15 = control.Rule(temp['Жаркая'] & time['Поздно'], clothes['Легкая'])

cs = control.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15])
css = control.ControlSystemSimulation(cs)


while True:
    chose = input('1 - Одеться\n2 - Выйти\n')

    if chose == '1':
        t = input("Введите текущую температуру за окном: ")
        h = input("Введите время прогулки: ")

        css.input['temp'] = int(t)
        css.input['time'] = int(h)
        css.compute()

        clothes_val = css.output['clothes']

        if(clothes_val < 20):
            print('Я думаю можно одеться легко!')
        elif (clothes_val < 40):
            print('Я думаю вам следует одеть средне-легкую одежду')
        elif (clothes_val < 60):
            print('Я думаю следует одеть утепленную одежду')
        elif (clothes_val < 80):
            print('Я считаю сегодня нужно одеть теплую одежду')
        else:
            print('Я советую одеть очень теплую одежду')

        clothes.view(sim=css)
        input('Нажммите любую кнопку...')
    else:
        break
