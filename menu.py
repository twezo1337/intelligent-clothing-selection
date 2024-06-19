
import rules


while True:
    ch = input('1.Ввести значения2.Выход')
    if ch == '2':
        break
    if ch == '1':
        s = input("Скорость км\ч : ")
        d = input("Расстояние м. : ")
        rules.controller.input['speed'] = int(s)
        rules.controller.input['distance'] = int(d)

        rules.controller.compute()
        print("Управляющее воздействие:", rules.controller.output['action'])
        action_number = rules.controller.output['action']
        # print("Система рекомендует")

        if(action_number <36):
            print("Система рекомендует - " + rules.print_actions[0])
        elif (action_number < 42):
            print("Система рекомендует - " + rules.print_actions[1])
        elif (action_number < 50):
            print("Система рекомендует - " + rules.print_actions[2])
        elif (action_number < 70):
            print("Система рекомендует - " + rules.print_actions[3])
        else:
            print("Система рекомендует - " + rules.print_actions[4])
        rules.action.view(sim=rules.controller)


