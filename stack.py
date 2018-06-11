class Stack(object):
	"""docstring fos Stack"""
	def __init__(self):
		self.data_list = []

	def init_stack(self):
		self.data_list = []

	def insert(self,data):
		self.data_list.append(data)

	def pop(self):
		if len(self.data_list) == 0:
			return None
		data = self.data_list[-1]
		del self.data_list[-1]
		return data

	def size(self):
		return len(self.data_list)

stack = Stack()
print(stack.size())
stack.insert(1)
stack.insert(2)
stack.insert(3)
print(stack.size())
tail = stack.pop()
print(tail)
tail = stack.pop()
print(tail)
tail = stack.pop()
print(tail)
tail = stack.pop()
print(tail)
