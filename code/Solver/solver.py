from abc import ABC, abstractmethod

class Sudoku_Solver(ABC):
	def __init__(self):
		self._len_code = 81
		self._result = []
		self._log = False

	def log(self, s):
		if self._log:
			print("Log - " + s)

	def start_posn_of_box(self, x):
		return (x // 3) * 3 

	def pretty_print(self, code, silent=False):
		out = ""
		for r in range(9):
			if r % 3 == 0 and r > 0:
				for i in range(3):
					out += "-" * 7
					if (i != 2):
						out += "+"
				out += "\n"
			for c in range(9):
				if c % 3 == 0 and c > 0:
					out += ' |'
				out += ' ' + code[r * 9 + c]
			out  += "\n"
		if (not silent):
			print(out)
		return out

	def clean(self):
		self._result = []

	@abstractmethod
	def is_okay(self, code, row, col, candidate):
		pass

	@abstractmethod
	def find_all(self, code, row, col):
		pass

	@abstractmethod
	def solve(self, code):
		pass