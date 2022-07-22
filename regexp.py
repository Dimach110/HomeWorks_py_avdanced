from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(type(contacts_list))

for contact in contacts_list:
  # print(contact)
  for text in contact:
    # print(type(text))
    # print(text)
    pattern = re.compile("([А-Я]{1}[а-я]+)")
    result = pattern.findall(text)
    if len(result)>1:
      print(result)

# # TODO 1: выполните пункты 1-3 ДЗ
# # ваш код
#
# # TODO 2: сохраните получившиеся данные в другой файл
# # код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)