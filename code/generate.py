# reference Creating a Sudoku Puzzle in https://www.sudokuwiki.org/Sudoku_Creation_and_Grading.pdf
import random
from Solver import Sudoku_Solver_1

class Generator(object):
	def __init__(self):
		self.lst_test = list(list(range(1, 10)))
		self.len_lst = len(self.lst_test)
		self.out = []

	def index_of_not_filled(self, lst):
		out = []
		for i in range(self.len_lst):
			if lst[i] == 0: out.append(i)
		return out

	def check_row_col(self, g, row, col, candidate):
		for i in range(self.len_lst):
			if g[row][i] == candidate or g[i][col] == candidate:
				return False
		return True

	def check_box(self, g, row, col, candidate):
		row_start = row // 3 * 3
		col_start = col // 3 * 3
		for r in range(row_start, row_start + 3):
			for c in range(col_start, col_start + 3):
				if g[r][c] == candidate:
					return False
		return True

	def pretty_print_wrap(self, g, pretty_print=True):
		out = ""
		for r in g:
			out += ''.join(list(map(str, r)))
		if pretty_print:
			Sudoku_Solver_1.pretty_print(out)
		return out

	def remove_node(self):
		pass

	# generate full valid board
	def generate(self):
		self.out = []
		for attempt in range(5):
			g = []
			# init grid
			for i in range(self.len_lst):
				g.append([])
				for j in range(self.len_lst):
					g[i].append(0)

			fail = False
			for r in range(3):
				num_rand = random.sample(self.lst_test, self.len_lst)
				for c in range(self.len_lst):
					for num in num_rand:
						if self.check_row_col(g, r, c, num) and self.check_box(g, r, c, num):
							g[r][c] = num
							num_rand.remove(num)
							break
				if 0 in g[r]:
					fail = True
					break
			if not fail:
				self.out.append(g)
				break

		if self.out == []:
			return []

		"""
		gout = self.pretty_print_wrap(g) # False)
		s = Sudoku_Solver_1()
		result = s.solve(gout)
		"""
		# TODO





		
		



if __name__ == '__main__':
	g = Generator()
	grid = g.generate()



