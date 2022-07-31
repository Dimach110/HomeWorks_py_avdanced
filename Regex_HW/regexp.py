from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

new_contact_list = []
for contact in contacts_list:
  pattern = re.compile('[А-Я]{1}[а-я]+')
  result = pattern.findall(contact[0])
  if len(result) > 1:
    contact[0] = result[0]
    contact[1] = result[1]
    if len(result) > 2:
      contact[2] = result[2]
  result = pattern.findall(contact[1])
  if len(result) > 1:
    contact[1] = result[0]
    contact[2] = result[1]
  pattern = r"(\+7|7|8)\s*\(?(\d{3})\)?(\s|-)?(\d{3})(\s|-)?(\d{2})(\s|-)?(\d{2})([^,]\s*\(?(доб\.)?\s*(\d{1,4})?)?\)?"
  result = re.sub(pattern, r"+7(\2)\4-\6-\8 \10\11", contact[5])
  contact[5] = result

new_contact_dict = {}
for i, con in enumerate(contacts_list):
  if f'{con[0]} {con[1]}' in new_contact_dict:
    for j, val in enumerate(new_contact_dict[f'{con[0]} {con[1]}']):
      if val != '':
        contacts_list[i][j + 2] = val
    new_contact_dict[f'{con[0]} {con[1]}'] = [con[2], con[3], con[4], con[5], con[6]]
  elif f'{con[0]} {con[1]}' not in new_contact_dict:
    new_contact_dict[f'{con[0]} {con[1]}'] = [con[2], con[3], con[4], con[5], con[6]]

for key, val in new_contact_dict.items():
  contact_l = []
  index1_2 = key.split(' ')
  contact_l.extend(index1_2)
  contact_l.extend(val)
  new_contact_list.append(contact_l)

with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(new_contact_list)




# ([А-Я]{1}[а-я]+)(\s|,)([А-Я]{1}[а-я]+)(\s|,)([А-Я]{1}[а-я]+)


# for con in contacts_list:
#   res = new_contact_dict.setdefault(f'{con[0]} {con[1]}', [con[2], con[3], con[4], con[5], con[6]])
#   if len(new_contact_dict.keys()) > max:
#     max = len(new_contact_dict.keys())
#   elif len(new_contact_dict.keys()) == max:


# попытка работать через словари зашла в никуда
# for contact in contacts_list:
#   new_cont_dict = {}
#   for i, val in enumerate(contact):
#     new_cont_dict[contacts_list[0][i]] = val
#   pattern = re.compile('[А-Я]{1}[а-я]+')
#   result = pattern.findall(contact[0])
#   if len(result) > 1:
#     new_cont_dict['surname'] = result[0]
#     new_cont_dict['firstname'] = result[1]
#     if len(result) == 3:
#       new_cont_dict['lastname'] = result[2]
#   new_contact_list.append(new_cont_dict)
# pprint(new_contact_list, sort_dicts=False)

