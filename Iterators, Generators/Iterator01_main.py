
def my_itaration(my_class):
	my_iter_list = []
	FlatIterator(my_class.my_list[0])
	for item in my_class:
		my_iter_list.extend(item)
	return my_iter_list

class FlatIterator:

	def __init__(self, my_list):
		self.my_list = my_list
	# ставим в start -1, что бы начать с начала списка (далее до возвращения будет прибавлен +1 и получиться 0)
		self.start = -1
		self.end = len(my_list)


	def __iter__(self):
		self.cursor = self.my_list[self.start]
		return self

	def __next__(self):
		self.start = self.start + 1
		if self.start < self.end:
			self.cursor = self.my_list[self.start]
			return self.cursor
		else:
			raise StopIteration

list1 = ['a', 'b', 'c']
nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

my_iterator = FlatIterator(nested_list)
result = my_itaration(my_iterator)
print('Вывод плоского списка всех элементов:')
print(result)
print('_'*50)

print('Последовательный вывод всех элементов:')
for item in result:
	print(item)

