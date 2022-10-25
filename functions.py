
import time
from datetime import datetime, timedelta


def getUsersName() -> list[str]:
    users = []
    print("Introduzca el nombre, o los nombres separadons por comas(Nombre1, Nombre2, Nombre3)")
    user_input = input("Nombre/s => ")
    has_end_coma = "," == user_input[-1:]
    if has_end_coma:
        user_input = user_input[0:-1]
    users = user_input.split(',')
    return users


def getWeek() -> int:
    week = 10
    is_valid_week = False
    user_input = ""

    print("Pulse enter si es para la semana actual, sino introduzca el numero de la semana")
    user_input = input("Semana => ")

    if not user_input:
        week = datetime.isocalendar(datetime.today()).week  # mejor online?
    else:
        try:
            week = int(user_input)
        except ValueError:
            print("Error! Debe ser una cifra")
            week = getWeek()

        is_valid_week = week in range(1, 53)

        if not is_valid_week:
            print("Error!! Debe ser del 1 al 52")
            week = getWeek()

    return week


def getDaysOfWeek(n_week) -> list[str]:

    WEEK = n_week - 1  # as it starts with 0 and you want week to start from sunday
    startdate = time.asctime(time.strptime('2022 %d 0' % WEEK, '%Y %W %w'))
    startdate = datetime.strptime(startdate, '%a %b %d %H:%M:%S %Y')
    dates = [startdate.strftime('%d/%m/%Y')]
    for i in range(1, 7):
        day = startdate + timedelta(days=i)
        dates.append(day.strftime('%d/%m/%Y'))

    return dates


def getNextLetter(letter, steps=1) -> str:
    i = ord(letter)

    if(i >= 90):  # 90 is ASCII value of last character of alphabets in uppercase.
        # 65 is ASCII value of first character of alphabets in uppercase.
        i = 65

    else:
        i = i + steps

    return chr(i)


#shift = Day_Shifts(day,)


class Day_Shifts:
    def __init__(self, date, part1_position, part2_position):
        self.date = date
        self.part1 = {"position": part1_position}
        self.part2 = {"position": part2_position}
        self.name = ""
