user = True
while user!= 0:
    user = int(input("Enter your age:\nFor exit enter '0':\n"))
    if user == 0:
        break
    elif user < 3:
        print("Ticket is free for you!")
    elif user >= 3 and user <= 12:
        print("Ticket costs $10 for you!")
    elif user > 12:
        print("Ticket costs $15 for you!")
    active = input('Ones again?\n')
    if active != 'no':
        continue
    else:
        break