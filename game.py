# импортируем функцию exit из модуля sys для завершения программы
# и фукцию sleep из модуля time, чтобы отложить выполнение последующих строк кода
from sys import exit
from time import sleep

game_name = "Dungeon Masters"

print(f"Welcome to the ***{game_name}***!\n")

print("Please, select character's gender:\n f-female \n m-male \n n-on binary ")
gender = str(input("Gender: ").lower())

if gender == "m":
    gender = "male"
elif gender == "f":
    gender = "female"
elif gender == "n":
    gender = "non-binary"
else:
    print(
        "You didn't give correct character's gender, you can't proceed playing this game, sorry!"
    )
    sleep(1)
    exit()


print(f"You've selected {gender} gender\n")

print("Please, select character's race:\n h-human\n e-elf")
race = str(input("Race: ").lower())

if race == "h":
    race = "human"
elif race == "e":
    race = "elf"
else:
    print(
        "You didn't give correct character's gender, you can't proceed playing this game, sorry!"
    )
    sleep(1)
    exit()

print(f"You've selected {race} race\n")

role = 0  # чтобы pylance не ругался о "role" is possible unbound, т.к. по его мнению role может быть пустым

# мы уверены, что либо race == "human" либо race == "elf" либо программа уже закрылась (по логике кода выше)
if race == "human":
    print("Select character's class:\n 1-warrior\n 2-archer\n 3-priest\n 4-magician")
    role = str(input("Class: "))
    if role == "1":
        role = "warrior"
    elif role == "2":
        role = "archer"
    elif role == "3":
        role = "priest"
    elif role == "4":
        role = "magician"
    else:
        print(
            "You didn't give correct character's class, you can't proceed playing this game, sorry!"
        )
        sleep(1)
        exit()

    print(f"You've selected {role} class\n")

# нам необязательно использовать elif или else
# просто напросто блок if или выполнется или не выполнется, да, можно и так поступать, выглядит аккуратно
if race == "elf":
    print(
        "Select character's class:\n 1-warrior\n 2-archer\n 3-dark sorcerer\n 4-paladin"
    )
    role = input("Class: ")
    if role == "1":
        role = "warrior"
    elif role == "2":
        role = "archer"
    elif role == "3":
        role = "dark sorcerer"
    elif role == "4":
        role = "paladin"
    else:
        print(
            "You didn't give correct character's class, you can't proceed playing this game, sorry!"
        )
        sleep(1)
        exit()

    print(f"You've selected {role} class\n")


name = str(input("Enter character's name: "))

print(
    f"\n***Character's info***\ngender: {gender}\nrace: {race}\nclass: {role}\nname: {name}"
)
