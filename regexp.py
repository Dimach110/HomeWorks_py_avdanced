from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

for contact in contacts_list:
  # print(contact)
  # print('vvvvvvvvvvvvvvvvvvvvvvvvvvv')
  pattern = re.compile("\s+")
  result = pattern.findall(contact[0])
  if len(result) > 0:
    new_result = contact[0].split(' ')
    contact[0] = new_result[0]
    contact[1] = new_result[1]
    if len(new_result) > 2:
      contact[2] = new_result[2]
    # print(contact)
    # print("--------------------------")
pprint(contacts_list)




# # TODO 1: выполните пункты 1-3 ДЗ
# # ваш код
#
# # TODO 2: сохраните получившиеся данные в другой файл
# # код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)




# ([А-Я]{1}[а-я]+)(\s|,)([А-Я]{1}[а-я]+)(\s|,)([А-Я]{1}[а-я]+)