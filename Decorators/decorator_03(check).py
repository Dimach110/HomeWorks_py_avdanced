from decorator_02 import logger

@logger('log_generator')
def flat_generator(list):
	start = 0
	end = len(list)
	while start < end:
		result = list[start]
		start1 = 0
		while start1 < len(result):
			yield list[start][start1]
			start1 += 1
		start += 1

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]

print('Последовательный вывод всех элементов:')
for item in  flat_generator(nested_list):
    print(item)

print('_'*30)
print('Вывод плоского списка всех элементов:')
flat_list = [item for item in flat_generator(nested_list)]
print(flat_list)