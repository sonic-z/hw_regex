from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

headers = [contacts_list[0]]

def sort_key(e):
    return " ".join(e[0:3])


p_phones = re.compile(r"[\+7|8]+[-|\s|\(]*(\d{3})[-|\s|\)]*(\d{3})[-|\s]?(\d{2})[-|\s]?(\d{2})\s?\(?(\w*\.?)\s*(\d*)\)?")

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

for row in contacts_list[1:]:
    tmp_name = " ".join(row[0:3]).split()
    for i, part in enumerate(tmp_name):
        row[i] = tmp_name[i]
    row[5] = p_phones.sub(r'+7(\1)\2-\3-\4 \5\6', row[5]).strip()


sorted_list = sorted(contacts_list[1:], key=sort_key)
headers.extend(sorted_list)
sorted_list = headers
i = 1
while i < len(sorted_list):
    if sorted_list[i][0] == sorted_list[i-1][0] and sorted_list[i][1] == sorted_list[i-1][1]:
        for j in range(0, len(sorted_list[i])):
            if sorted_list[i][j] and not sorted_list[i-1][j]:
                sorted_list[i-1][j] = sorted_list[i][j]
            if not sorted_list[i][j] and sorted_list[i-1][j]:
                sorted_list[i][j] = sorted_list[i-1][j]
        sorted_list.remove(sorted_list[i])
    i+=1

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
    datawriter.writerows(sorted_list)