from Row import Row
from Sheet import Sheet

from functions import getDaysOfWeek, getUsersName, getWeek

row = Row("A", 4)
sheet = Sheet()

users = getUsersName()
week = getWeek()
days = getDaysOfWeek(week)

sheet.setStyles()
sheet.setHeader(week, row)
sheet.setContent(days, row)

for i in range(0, len(users)):
    sheet.saveFile(week, users[i])
