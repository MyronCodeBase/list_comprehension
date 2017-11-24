import random

def list_comprehension():
	a = random.sample(range(30), 10)
	b = [i for i in a if i % 2 == 0]

	print(b)

list_comprehension()
