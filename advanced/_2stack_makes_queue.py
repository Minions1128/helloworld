"""
The following shows that how to use 2 Stacks to implement Queue.
"""

class Stack(object):
	def __init__(self):
		self.val = []
		self.top = 0

	def push(self, key):
		self.val.append(key)
		self.top += 1
		#self.output()

	def pop(self):
		if self.top == 0:
			print "the stack is empty"
			return		
		self.top -= 1
		e = self.val.pop()
		#self.output()
		return e

	def output(self):
		print self.val

	def is_empty(self):
		if self.top == 0:
			return True
		else:
			return False

class Queue(object):
	def __init__(self):
		self.in_stack = Stack()
		self.out_stack = Stack()

	def in_queue(self, key):
		self.in_stack.push(key)

	def out_queue(self):
		if self.out_stack.is_empty():
			if self.in_stack.is_empty():
				print "the queue is empty"
				return
			else:
				while(not self.in_stack.is_empty()):
					temp = self.in_stack.pop()
					self.out_stack.push(temp)
		e = self.out_stack.pop()
		return e

	def output(self):
		print self.out_stack.val[::-1] + self.in_stack.val

	def is_empty(self):
		if self.in_stack.is_empty() and self.out_stack.is_empty():
			return True
		else:
			return False

if __name__ == "__main__":
	a = Queue()
	for i in range(5):
		a.in_queue(i)
		a.output()
	a.out_queue()
	a.output()
	for i in range(100, 105):
		a.in_queue(i)
		a.output()
	while(not a.is_empty()):
		a.out_queue()
		a.output()
